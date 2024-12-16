# !/usr/bin/python3
# -*- coding: utf-8 -*-import pytest
import datetime
import json
import os
import uuid
from urllib.parse import urlparse

import pytest
import allure

from common.mpw import PageWrapper
from log import logger
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from functools import wraps
import time
# @Author: 花菜
# @File: conftest.py
# @Time : 2024/1/13 00:42
# @Email: lihuacai168@gmail.com


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }

def extract_domain(url_string):
    parsed_url = urlparse(url_string)
    return parsed_url.netloc

# @pytest.fixture(scope="session")
# def page(pytestconfig):
#     with sync_playwright() as p:
#         data = datetime.datetime.now().strftime('%Y%m%d%H%M')
#         logger.info("page session fixture starting....")
#         # browser = p.chromium.launch( headless=False, timeout=5_000) #slow_mo=500,
#         browser = p.chromium.launch(headless=False, timeout=5_000, args=[
#             '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'])  #slow_mo=500,
#         context = browser.new_context(viewport={'width': 1920, 'height': 1080})
#         page = context.new_page()
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         # 将 Playwright 的 Page 封装到 PageWrapper 中
#         wrapped_page = PageWrapper(page)
#         yield wrapped_page
#         logger.info("page session fixture closing.......")
#         logger.info("stop tracing...")
#         # 获取当前工作目录
#         BASEDIR = os.getcwd()
#         # 定义 trace.zip 的保存路径
#         trace_dir = os.path.join(BASEDIR, "traces")
#         if not os.path.exists(trace_dir):
#             os.makedirs(trace_dir)
#         trace_path = os.path.join(trace_dir, f"trace_{data}.zip")
#         # 保存 trace.zip 文件
#         context.tracing.stop(path=trace_path)
#         browser.close()


@pytest.fixture(scope="session")
def browser(pytestconfig):
    with sync_playwright() as p:
        logger.info("Browser session starting...")

        try:
            headless = pytestconfig.getoption("--headless", default=False)
            browser_name = os.environ.get("BROWSER", "chromium")

            browser = getattr(p, browser_name).launch(
                headless=headless,
                timeout=5000,
                args=[
                    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36']
            )

            yield browser

        except Exception as e:
            logger.error(f"Error during browser setup: {str(e)}")
            raise

        finally:
            logger.info("Browser session closing...")
            if browser:
                browser.close()
            logger.info("Browser session closed")


@pytest.fixture
def page(browser, request):
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    wrapped_page = PageWrapper(page)

    # 开始跟踪
    data = datetime.datetime.now().strftime('%Y%m%d%H%M')
    test_name = request.node.name

    if os.environ.get("ENABLE_TRACING", "false").lower() == "true":
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield wrapped_page

    # 停止跟踪并保存
    if os.environ.get("ENABLE_TRACING", "false").lower() == "true":
        BASEDIR = os.getcwd()
        trace_dir = os.path.join(BASEDIR, "traces")
        os.makedirs(trace_dir, exist_ok=True)
        trace_path = os.path.join(trace_dir, f"trace_{test_name}_{data}.zip")
        try:
            context.tracing.stop(path=trace_path)
            logger.info(f"Trace for test '{test_name}' saved to {trace_path}")
        except Exception as e:
            logger.error(f"Error saving trace for test '{test_name}': {str(e)}")

    context.close()

def _login(page: PageWrapper, base_url: str, passwd: str):
    login_page = LoginPage(page, base_url=base_url)
    logger.info("开始登录.......")
    login_page.login("admin", passwd)
    return login_page

# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="session")
def login_goto_project(browser, pytestconfig):
    if base_url := pytestconfig.getoption("host"):
        logger.info(f"命令行传入参数，base_url={base_url}")
    else:
        default_url = "http://10.30.76.33:8080"
        logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
        base_url = default_url

    if passwd := pytestconfig.getoption("passwd"):
        logger.info(f"命令行传入参数，username={passwd}")
    else:
        default_passwd = "Supos1304!"
        passwd = default_passwd

    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    wrapped_page = PageWrapper(page)

    login_page = _login(wrapped_page, base_url, passwd)

    yield wrapped_page

    context.close()


# def _login(page, pytestconfig):
#     if base_url := pytestconfig.getoption("host"):
#         logger.info(f"命令行传入参数，base_url={base_url}")
#     else:
#         default_url = "http://10.30.76.33:8080"
#         logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
#         base_url = default_url
#     if passwd := pytestconfig.getoption("passwd"):
#         logger.info(f"命令行传入参数，username={passwd}")
#     else:
#         default_passwd = "Supos1304!"
#         passwd = default_passwd
#     login_page = LoginPage(page, base_url=base_url)
#     logger.info("开始登录.......")
#     login_page.login("admin", passwd)
#     return login_page
#
#
#
#
# # 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
# @pytest.fixture
# def login_goto_project(page, pytestconfig):
#     yield _login(page, pytestconfig)


def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action="store",
        default="http://10.30.76.33:8080/",
        help="base URL for login page",
    )
    logger.info("添加命令行参数 host")
    parser.addoption(
        "--passwd",
        action="store",
        #Yanfa@1304/Supcon@1304
        default="Supcon@1304",
        help="Username for login",
    )
    logger.info("添加命令行参数 username")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item: 表示当前正在执行的测试用例对象
    :param call: 表示测试用例的执行状态（setup、call、teardown）
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()

    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = f" ({item.funcargs['tmpdir']})"
            else:
                extra = ""
            f.write(f"{rep.nodeid}{extra}\n")

        # 添加allure报告截图
        try:
            page = item.funcargs.get('page')
            if page and isinstance(page, Page):
                with allure.step('添加测试用例失败截图...'):
                    screenshot = page.screenshot()
                    allure.attach(screenshot,
                                  name=f"测试用例失败_{item.name}",
                                  attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"截图失败: {str(e)}")


@pytest.fixture
def PageDownload(page: Page):
    def trigger_shutdown(iframe, button_names):
        # 定义一个内部函数来处理下载逻辑
        def download_report(button_name):
            with page.expect_download() as download_info:
                iframe.get_by_role("button", name=button_name).click()
                download = download_info.value
                logger.info(f"下载诊断报告{download.suggested_filename}")

        iframe.get_by_role("button", name="search 搜索").click()
        iframe.get_by_role("button", name="clear 重置").click()

        # 循环遍历每个按钮名称并下载报告
        for name in button_names:
            download_report(name)

    return trigger_shutdown


# @pytest.fixture(scope="function", autouse=True)
# def capture_requests(page, request):
#     """
#     捕获接口错误请求并记录到日志，包含更详细的上下文信息
#     自动记录页面操作，无需手动调用
#     """
#     # 记录当前测试用例信息
#     test_name = request.node.name
#
#     # 存储最近的页面操作
#     last_action = {"description": "测试开始"}
#
#     def on_console(msg):
#         """记录控制台消息"""
#         if msg.type == "error":
#             logger.error(f"Console Error in {test_name}: {msg.text}")
#
#     def wrap_action(original_func, action_name):
#         """包装原始方法，添加自动记录功能"""
#
#         def wrapper(*args, **kwargs):
#             selector = args[0] if len(args) > 0 else kwargs.get('selector', '')
#             last_action["description"] = f"{action_name} -> {selector}"
#             logger.debug(f"页面操作: {last_action['description']}")
#             return original_func(*args, **kwargs)
#
#         return wrapper
#
#     # 自动包装常用的页面操作方法
#     original_click = page.click
#     original_fill = page.fill
#     original_type = page.type
#     original_press = page.press
#     original_check = page.check
#     original_uncheck = page.uncheck
#     original_select_option = page.select_option
#     original_dblclick = page.dblclick
#     original_hover = page.hover
#
#     # 替换原始方法为包装后的方法
#     page.click = wrap_action(original_click, "点击")
#     page.fill = wrap_action(original_fill, "填写")
#     page.type = wrap_action(original_type, "输入")
#     page.press = wrap_action(original_press, "按键")
#     page.check = wrap_action(original_check, "勾选")
#     page.uncheck = wrap_action(original_uncheck, "取消勾选")
#     page.select_option = wrap_action(original_select_option, "选择选项")
#     page.dblclick = wrap_action(original_dblclick, "双击")
#     page.hover = wrap_action(original_hover, "悬停")
#
#     def on_request_failed(request):
#         """处理请求失败事件"""
#         failure_info = {
#             "url": request.url,
#             "method": request.method,
#             "failure": request.failure,
#             "headers": request.headers,
#             "post_data": request.post_data if request.method == "POST" else None
#         }
#
#         error_msg = f"""
# 请求失败详情:
# 测试用例: {test_name}
# 最近操作: {last_action['description']}
# URL: {failure_info['url']}
# 方法: {failure_info['method']}
# 失败原因: {failure_info['failure']}
# 请求头: {failure_info['headers']}
# POST数据: {failure_info['post_data']}
#         """
#         logger.error(error_msg)
#
#         # 添加到 allure 报告
#         allure.attach(
#             error_msg,
#             name=f"API请求失败_{test_name}_{failure_info['url'].split('/')[-1]}",
#             attachment_type=allure.attachment_type.TEXT
#         )
#
#         # 在请求失败时自动截图，使用更具体的名称
#         try:
#             screenshot = page.screenshot()
#             allure.attach(
#                 screenshot,
#                 name=f"API请求失败时的页面状态_{test_name}_{failure_info['url'].split('/')[-1]}",
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             logger.error(f"截图失败: {str(e)}")
#
#     # 监听页面事件
#     page.on("console", on_console)
#     page.on("requestfailed", on_request_failed)
#
#     yield page
#
#     # 恢复原始方法
#     page.click = original_click
#     page.fill = original_fill
#     page.type = original_type
#     page.press = original_press
#     page.check = original_check
#     page.uncheck = original_uncheck
#     page.select_option = original_select_option
#     page.dblclick = original_dblclick
#     page.hover = original_hover
#
#     # 清理监听器
#     page.remove_listener("console", on_console)
#     page.remove_listener("requestfailed", on_request_failed)

# @pytest.fixture(scope="function", autouse=True)
# def capture_requests(page, request):
#     """
#     捕获接口错误请求并记录到日志，包含更详细的上下文信息
#     自动记录页面操作，无需手动调用
#     """
#     # 记录当前测试用例信息
#     test_name = request.node.name
#
#     # 存储最近的页面操作
#     last_action = {"description": "测试开始"}
#
#     def on_console(msg):
#         pass
#
#     def wrap_action(original_func, action_name):
#         """包装原始方法，添加自动记录功能"""
#
#         def wrapper(*args, **kwargs):
#             selector = args[0] if len(args) > 0 else kwargs.get('selector', '')
#             last_action["description"] = f"{action_name} -> {selector}"
#             logger.debug(f"页面操作: {last_action['description']}")
#             return original_func(*args, **kwargs)
#
#         return wrapper
#
#     # 自动包装常用的页面操作方法
#     original_click = page.click
#     original_fill = page.fill
#     original_type = page.type
#     original_press = page.press
#     original_check = page.check
#     original_uncheck = page.uncheck
#     original_select_option = page.select_option
#     original_dblclick = page.dblclick
#     original_hover = page.hover
#
#     # 替换原始方法为包装后的方法
#     page.click = wrap_action(original_click, "点击")
#     page.fill = wrap_action(original_fill, "填写")
#     page.type = wrap_action(original_type, "输入")
#     page.press = wrap_action(original_press, "按键")
#     page.check = wrap_action(original_check, "勾选")
#     page.uncheck = wrap_action(original_uncheck, "取消勾选")
#     page.select_option = wrap_action(original_select_option, "选择选项")
#     page.dblclick = wrap_action(original_dblclick, "双击")
#     page.hover = wrap_action(original_hover, "悬停")
#
#     def on_request_failed(request):
#         """处理请求失败事件"""
#         # 获取请求的path
#         url_path = request.url.split('/')[-1]
#
#         # 过滤条件：忽略以 'currentUser' 结尾的请求和以 '.js' 结尾的请求
#         if url_path == "currentUser" or url_path.endswith(".js") or url_path.endswith(".css"):
#             return
#
#         failure_info = {
#             "url": request.url,
#             "method": request.method,
#             "failure": request.failure,
#             "headers": request.headers,
#             "post_data": request.post_data if request.method == "POST" else None
#         }
#
#         error_msg = f"""
#         请求失败详情:
#         测试用例: {test_name}
#         最近操作: {last_action['description']}
#         URL: {failure_info['url']}
#         方法: {failure_info['method']}
#         失败原因: {failure_info['failure']}
#         请求头: {failure_info['headers']}
#         POST数据: {failure_info['post_data']}
#         """
#         logger.error(error_msg)
#
#         # 添加到 allure 报告
#         allure.attach(
#             error_msg,
#             name=f"API请求失败_{test_name}_{failure_info['url'].split('/')[-1]}",
#             attachment_type=allure.attachment_type.TEXT
#         )
#
#         # 在请求失败时自动截图，使用更具体的名称
#         try:
#             screenshot = page.screenshot()
#             allure.attach(
#                 screenshot,
#                 name=f"API请求失败时的页面状态_{test_name}_{failure_info['url'].split('/')[-1]}",
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             logger.error(f"截图失败: {str(e)}")
#
#     # 监听页面事件
#     page.on("console", on_console)
#     page.on("requestfailed", on_request_failed)
#
#     yield page
#
#     # 恢复原始方法
#     page.click = original_click
#     page.fill = original_fill
#     page.type = original_type
#     page.press = original_press
#     page.check = original_check
#     page.uncheck = original_uncheck
#     page.select_option = original_select_option
#     page.dblclick = original_dblclick
#     page.hover = original_hover
#
#     # 清理监听器
#     page.remove_listener("console", on_console)
#     page.remove_listener("requestfailed", on_request_failed)
