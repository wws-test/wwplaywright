import logging
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

    def _record_action(self, description: str, func, *args, **kwargs):
        if not self._record_enabled:
            return func(*args, **kwargs)

        start_time = time.perf_counter()
        logger.debug(f"Starting action: {description}")

        with allure.step(description):
            result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        logger.debug(f"Action '{description}' completed. Raw elapsed time: {elapsed_time}")

        # 使用更精确的格式化，显示更多小数位
        formatted_time = f"{elapsed_time:.6f}"

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
        self.current_frame = self.page.frame_locator(selector)

    def switch_to_main_frame(self):
        self.current_frame = None

    def fill(self, selector: str, text: str):
        target = self.current_frame or self.page
        return self._record_action(f"Fill element '{selector}' with text '{text}'", target.fill, selector, text)

    def press(self, selector: str, key: str):
        target = self.current_frame or self.page
        return self._record_action(f"Press key '{key}' on element '{selector}'", target.press, selector, key)

    def click(self, selector: str):
        """
        普通点击方法，不记录时间。
        """
        target = self.current_frame or self.page
        return target.click(selector)

    def click_with_timing(self, selector: str):
        """
        带时间记录的点击方法。
        """
        target = self.current_frame or self.page
        return self._record_action(f"Click element '{selector}'", target.click, selector)

    def locator(self, selector: str):
        target = self.current_frame or self.page
        locator = target.locator(selector)
        return LocatorWrapper(locator, self)

    def get_by_text(self, text: str, **kwargs):
        target = self.current_frame or self.page
        locator = target.get_by_text(text, **kwargs)
        return LocatorWrapper(locator, self)

        # 同样修改其他定位方法

    def get_by_role(self, role: str, **kwargs):
        target = self.current_frame or self.page
        locator = target.get_by_role(role, **kwargs)
        return LocatorWrapper(locator, self)

    def get_by_label(self, label: str, **kwargs):
        target = self.current_frame or self.page
        locator = target.get_by_label(label, **kwargs)
        return LocatorWrapper(locator, self)

    def get_by_placeholder(self, placeholder: str, **kwargs):
        target = self.current_frame or self.page
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
