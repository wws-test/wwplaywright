# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure

from common.mpw import PageWrapper
from log import logger
from playwright.sync_api import Page, expect


@allure.step("驾驶舱")
def select_setting_management(frame_locator: Page, page: Page):
    with allure.step("大屏"):
        frame_locator.get_by_role("button", name="报 警").click()
        frame_locator.get_by_label('实时报警历史报警搁置配置').get_by_text("历史报警", exact=True).click()
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

@allure.step("石化")
def select_setting_management_p(page: PageWrapper):
    page.get_by_role("textbox").fill("茂名石化")
    page.get_by_role("textbox").press("Enter")
    page.get_by_text("茂名石化").click_with_timing()


