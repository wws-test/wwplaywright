# !/usr/bin/python3
# -*- coding: utf-8 -*-import pytest
import os
from urllib.parse import urlparse

import pytest

from log import logger
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

# @Author: 花菜
# @File: conftest.py
# @Time : 2024/1/13 00:42
# @Email: lihuacai168@gmail.com



def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action="store",
        default="http://10.30.76.150:8080/",
        help="base URL for login page",
    )
    logger.info("添加命令行参数 host")
    parser.addoption("--wtrace" , default= False, action="store_true", help="启用 Playwright 的追踪功能")
    logger.info("添追踪功能")


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
        browser = p.chromium.launch(headless=False, timeout=5_000)
        context = browser.new_context()
        page = context.new_page()

        if pytestconfig.getoption("wtrace"):
            context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

        logger.info("page session fixture closing.......")
        base_url = pytestconfig.getoption("base_url") or "http://10.30.76.150:8080/"
        domain = extract_domain(base_url).replace(".", "_")

        if pytestconfig.getoption("wtrace"):
            logger.info("stop tracing...")
            context.tracing.stop(path=f"{domain}_trace.zip")
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
    if base_url := pytestconfig.getoption("base_url"):
        logger.info(f"命令行传入参数，base_url={base_url}")
    else:
        default_url = "http://10.30.76.150:8080"
        logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
        base_url = default_url

    login_page = LoginPage(page, base_url=base_url)
    logger.info("开始登录.......")
    login_page.login("wwtest", "Supcon@1209")
    return login_page


# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="function")
def login(page, pytestconfig):
    yield _login(page, pytestconfig)


# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="session")
def login_goto_project(page, pytestconfig):
    yield _login(page, pytestconfig)


