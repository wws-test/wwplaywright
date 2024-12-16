# !/usr/bin/python3
# -*- coding: utf-8 -*-
import time

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure

from common.mpw import PageWrapper
from log import logger
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: PageWrapper, base_url: str):
        self.page = page
        self.base_url = base_url

    # 定义页面元素
    def username_input(self):
        return self.page.locator("#userName")

    def password_input(self):
        return self.page.locator("#password")

    def submit_button(self):
        return self.page.locator("button")

    def tips(self):
        return self.page.get_by_role("button", name="确定")
    # 定义操作
    @allure.step("打开登录页面，填写账号密码")
    def login(self, username: str, password: str):
        with self.page.disable_recording():
            logger.info(f"打开登录页面: {self.base_url + '/login/#/login'}，填写账号密码")
            self.page.goto(self.base_url)
            self.username_input().fill(username)
            self.password_input().fill(password)
            logger.info("点击登录按钮")
            self.submit_button().click()
            time.sleep(2)
            if self.tips().is_visible():
                self.tips().click()
                logger.info("登录成功")
            else:
                logger.info("登录成功")



