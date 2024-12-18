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
from pages.login_page import LoginPage1
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import tempfile
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
    login_page = LoginPage1(page, base_url=base_url)
    logger.info("开始登录.......")
    login_page.login1("admin", passwd)
    return login_page

# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="session")
def login_goto_pro(browser, pytestconfig):
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

    # 创建新的上下文，并设置关闭未使用页面的选项
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        no_viewport=True,  # 禁用视口限制
    )
    
    # 创建新页面并包装
    page = context.new_page()
    wrapped_page = PageWrapper(page)
    
    # 执行登录
    login_page = _login(wrapped_page, base_url, passwd)
    
    try:
        yield wrapped_page
    finally:
        # 清理所有页面，只保留主页面
        for p in context.pages:
            if p != page:  # 不关闭主页面
                try:
                    p.close()
                except:
                    pass
        
        # 返回到首页
        try:
            page.goto(base_url)
        except:
            pass
            
        # 关闭上下文
        context.close()


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
