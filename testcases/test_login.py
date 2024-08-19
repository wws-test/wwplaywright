# !/usr/bin/python3
# -*- coding: utf-8 -*-
import allure
from playwright.async_api import expect

from log import logger
from pages.login_page import LoginPage


# @Author: 花菜
# @File: test_login.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com


# 测试
@allure.feature("测试登录成功")
@allure.step("login")
def test_login(page, pytestconfig, is_goto_project_detail=False):
    if base_url := pytestconfig.getoption("base_url"):
        logger.info(f"命令行传入参数，base_url={base_url}")
    else:
        default_url = "http://10.30.76.150:8080/"
        logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
        base_url = default_url

    login_page = LoginPage(page, base_url=base_url)

    login_page.login("admin", "Yanfa@1304")
    if is_goto_project_detail:
        logger.info("登录并进入项目详情")
        login_page.switch2project_base()
        login_page.enter_project_detail()
    return login_page


