# !/usr/bin/python3
# -*- coding: utf-8 -*-import pytest
import os
from urllib.parse import urlparse

import pytest
import allure
from log import logger
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
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
def page(pytestconfig):
    with sync_playwright() as p:
        logger.info("page session fixture starting....")
        # browser = p.chromium.launch( headless=False, timeout=5_000) #slow_mo=500,
        browser = p.chromium.launch( headless=False, timeout=5_000,args=['--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36']) #slow_mo=500,
        context = browser.new_context(viewport={ 'width': 1920, 'height': 1080 })
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield page
        logger.info("page session fixture closing.......")
        logger.info("stop tracing...")
        context.tracing.stop(path="trace.zip")
        browser.close()

# @pytest.fixture(scope="session")
def auth_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, timeout=50_000)
        logger.info("使用auth.json文件恢复登录状态")
        base_path = os.path.dirname(os.path.realpath(__file__))
        context = browser.new_context(
            storage_state=os.path.join(base_path, "auth.json"),
            viewport={"width": 1620, "height": 1080},
        )
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield page
        logger.info("page session fixture closing.......")
        context.tracing.stop(path="trace.zip")
        browser.close()


def _login(page, pytestconfig):
    if base_url := pytestconfig.getoption("host"):
        logger.info(f"命令行传入参数，base_url={base_url}")
    else:
        default_url = "http://10.30.76.33:8080"
        logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
        base_url = default_url

    login_page = LoginPage(page, base_url=base_url)
    logger.info("开始登录.......")
    login_page.login("wwtest", "Supcon@1209#")
    return login_page


# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="function")
def login(page, pytestconfig):
    yield _login(page, pytestconfig)


# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="session")
def login_goto_project(page, pytestconfig):
    yield _login(page, pytestconfig)




def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action="store",
        default="http://10.30.76.33:8080/",
        help="base URL for login page",
    )
    logger.info("添加命令行参数 host")


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
                with allure.step('添加失败截图...'):
                    screenshot = page.screenshot()
                    allure.attach(screenshot, name="失败截图", attachment_type=allure.attachment_type.PNG)
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

        # 循环遍历每个按钮名称并下载报告
        for name in button_names:
            download_report(name)

    return trigger_shutdown