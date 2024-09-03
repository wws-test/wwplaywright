# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure

from common.assertion import assert_element_exists
from log import logger
from playwright.sync_api import Page, expect


@allure.step("报警列表")
def select_setting_management(frame_locator: Page, page: Page):
    with allure.step("报警列表"):
        frame_locator.get_by_text("历史报警").click()
        frame_locator.get_by_text("搁置配置").click()
        frame_locator.get_by_role("tab", name="设备").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="download 导出").click()
            download = download_info.value
            logger.info(f"下载报告{download.suggested_filename}")


@allure.step("预测性维护")
def select_maintenance_management(frame_locator: Page):
    frame_locator.get_by_placeholder("请输入").click()
    frame_locator.get_by_placeholder("请输入").fill("控制")
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()

    frame_locator.locator("#rc_select_0").click()
    frame_locator.locator("(//div[@class='ant-select-item-option-content'])[1]").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()

    frame_locator.get_by_text("控制系统：机柜：请选择搜索重置").click()




