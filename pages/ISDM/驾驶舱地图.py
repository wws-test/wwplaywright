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


@allure.step("驾驶舱")
def select_setting_management(frame_locator: Page, page: Page):
    with allure.step("大屏"):
        frame_locator.get_by_role("button", name="报 警").click()
        frame_locator.get_by_text("历史报警").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="download 导出").click()
            download = download_info.value
            logger.info(f"下载报告{download.suggested_filename}")
        frame_locator.get_by_text("搁置配置").click()
        frame_locator.get_by_role("tab", name="设备").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="download 导出").click()
            download = download_info.value
            logger.info(f"下载报告{download.suggested_filename}")
        frame_locator.get_by_text("实时报警").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="download 导出").click()
            download = download_info.value
            logger.info(f"下载报告{download.suggested_filename}")





