import logging
import os
import tempfile
import time
import allure
from playwright.sync_api import Page, FrameLocator
import contextlib

logger = logging.getLogger(__name__)


class PageWrapper:
    def __init__(self, page: Page):
        self.page = page
        self.current_frame = None
        self._record_enabled = True

    @contextlib.contextmanager
    def disable_recording(self):
        original_state = self._record_enabled
        self._record_enabled = False
        try:
            yield
        finally:
            self._record_enabled = original_state

    def _get_target(self):
        """获取当前操作的目标（页面或框架）"""
        if self.current_frame:
            return self.current_frame.first
        return self.page

    def _record_action(self, description: str, func, *args, **kwargs):
        # 如果记录功能未启用，则直接执行函数
        if not self._record_enabled:
            return func(*args, **kwargs)

        # 记录开始时间
        start_time = time.perf_counter()
        logger.debug(f"Starting action: {description}")

        # 使用allure���录步骤
        with allure.step(description):
            result = func(*args, **kwargs)

        # 记录结束时间
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        logger.debug(f"Action '{description}' completed. Raw elapsed time: {elapsed_time}")

        # 使用更精确的格式化，显示更多小数位
        formatted_time = f"{elapsed_time:.6f}"

        # 使用allure记录步骤耗时
        allure.attach(
            body=f"Action '{description}' took {formatted_time} seconds.",
            name=f"Action Time: {description}",
            attachment_type=allure.attachment_type.TEXT,
        )

        # 如果时间太短，添加一个注释
        if elapsed_time < 0.001:
            logger.warning(
                f"Action '{description}' completed very quickly ({formatted_time} seconds). This might indicate a potential issue.")
            allure.attach(
                body="This action completed very quickly. Please verify if it executed as expected.",
                name=f"Warning: Quick Execution for {description}",
                attachment_type=allure.attachment_type.TEXT,
            )

        return result

    def switch_to_frame(self, selector: str):
        """切换到指定的 iframe"""
        self.current_frame = self.page.frame_locator(selector)

    def screenshot(self, name=None, full_page=False, timeout=5000):
        """
        捕获页面或当前帧的截图。

        :param name: 截图的名称，如果未提供，将使用默认名称
        :param full_page: 是否捕获整个页面，默认为False
        :param timeout: 等待页面加载的超时时间（毫秒）
        :return: bytes 类型的截图数据
        """
        if name is None:
            name = f"Screenshot_{time.time()}"

        # 记录当前页面状态
        logger.info(f"当前页面 URL: {self.page.url}")
        logger.info(f"当前页面标题: {self.page.title()}")
        logger.info(f"当前上下文中的页面数量: {len(self.page.context.pages)}")
        
        # 确保页面在前台
        self.page.bring_to_front()
        
        target = self._get_target()
        
        try:
            # 等待页面加载完成
            self.page.wait_for_load_state("networkidle", timeout=timeout)
            
            # 等待所有动画完成
            self.page.evaluate("""
                () => new Promise((resolve) => {
                    const interval = setInterval(() => {
                        const animations = document.getAnimations();
                        if (animations.length === 0) {
                            clearInterval(interval);
                            resolve();
                        }
                    }, 100);
                    setTimeout(() => {
                        clearInterval(interval);
                        resolve();
                    }, 1000);
                })
            """)
            
            # 检查页面是否可见
            if not self.page.is_visible("body"):
                logger.warning("页面 body 元素不可见")
                
            # 直接返回截图数据，不保存到文件
            screenshot_data = target.screenshot(
                full_page=full_page,
                type='png',
                animations='disabled'  # 禁用动画，避免截图时的闪烁
            )
            
            if not screenshot_data:
                logger.error("截图数据为空")
            else:
                logger.info(f"成功获取截图，大小: {len(screenshot_data)} 字节")
                
            return screenshot_data
            
        except Exception as e:
            logger.error(f"截图失败: {str(e)}", exc_info=True)
            # 记录更多调试信息
            try:
                logger.error(f"页面内容: {self.page.content()[:500]}...")  # 只记录前500个字符
            except:
                pass
            return None

    def switch_to_main_frame(self):
        """切换回主框架"""
        self.current_frame = None

    def click(self, selector: str):
        """普通点击方法，不记录时间"""
        target = self._get_target()
        return target.click(selector)

    def click_with_timing(self, selector: str):
        """带时间记录的点击方法"""
        target = self._get_target()
        return self._record_action(f"Click element '{selector}'", target.click, selector)

    def locator(self, selector: str):
        target = self._get_target()
        locator = target.locator(selector)
        return LocatorWrapper(locator, self)

    def get_by_text(self, text: str, **kwargs):
        target = self._get_target()
        locator = target.get_by_text(text, **kwargs)
        return LocatorWrapper(locator, self)

    def get_by_role(self, role: str, **kwargs):
        target = self._get_target()
        locator = target.get_by_role(role, **kwargs)
        return LocatorWrapper(locator, self)

    def get_by_label(self, label: str, **kwargs):
        target = self._get_target()
        locator = target.get_by_label(label, **kwargs)
        return LocatorWrapper(locator, self)

    def get_by_placeholder(self, placeholder: str, **kwargs):
        target = self._get_target()
        locator = target.get_by_placeholder(placeholder, **kwargs)
        return LocatorWrapper(locator, self)

    def __getattr__(self, name):
        return getattr(self.page, name)


class LocatorWrapper:
    def __init__(self, locator, page_wrapper):
        self._locator = locator
        self._page_wrapper = page_wrapper

    def click_with_timing(self):
        return self._page_wrapper._record_action(f"Click element", self._locator.click)

    def click(self):
        return self._locator.click()

    def get_by_text(self, text: str, **kwargs):
        locator = self._locator.get_by_text(text, **kwargs)
        return LocatorWrapper(locator, self._page_wrapper)

    def locator(self, selector: str):
        locator = self._locator.locator(selector)
        return LocatorWrapper(locator, self._page_wrapper)

    # 添加其他定位方法，如 get_by_role, get_by_label 等

    def __getattr__(self, name):
        # 对于未定义的方法，我们返回原始 locator 的方法
        attr = getattr(self._locator, name)
        if callable(attr):
            # 如果是方法，我们包装它以返回 LocatorWrapper
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                if hasattr(result, 'click'):  # 假设有 click 方法的对象是 Locator
                    return LocatorWrapper(result, self._page_wrapper)
                return result

            return wrapper
        return attr
