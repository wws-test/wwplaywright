# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure

from common.assertion import assert_element_exists
from common.datafake import fake
from log import logger
from playwright.sync_api import Page, expect


@allure.step("未匹配OPC AE")
def select_setting_management(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").first.click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_role("button", name="setting 列配置").click()
    frame_locator.get_by_role("button", name="取 消").click()
    frame_locator.get_by_role("button", name="setting 列配置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="确 认").click()


@allure.step("工厂模型")
def select_knowledge_classification(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").first.click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 模板下载").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_role("button", name="link 智能绑定").click()
    frame_locator.get_by_role("button", name="确 定").click()

@allure.step("通知配置")
def select_device_ledger(frame: Page, page: Page):
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 全量导出").first.click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 模板下载").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="plus-circle 新增").click()
    frame.get_by_label("策略名称").click()
    frame.get_by_label("策略名称").fill(fake.pystr())
    frame.locator(".ant-select-selection-overflow").first.click()
    frame.locator(".ant-select-item-option-content").first.click()
    frame.get_by_label("新增").locator("div").filter(has_text=re.compile(r"^发送范围$")).click()
    frame.locator("#rangeType").click()
    frame.get_by_text("人员", exact=True).click()
    frame.get_by_label("Close", exact=True).click()
    frame.get_by_text("策略名称：搜索重置").click()
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()