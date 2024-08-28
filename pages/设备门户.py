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


@allure.step("打开配置管理")
def select_setting_management(frame_locator):
    logger.info("打开配置管理")
    frame_locator.get_by_role("button", name="配置管理").click()
    with allure.step("非选中设置重要度"):
        frame_locator.get_by_role("button", name="设置重要度").click()
        # 等待元素出现
        order_sent = frame_locator.get_by_text("请先选择内容，再点击“设置重要度”")
        order_sent.wait_for()
        assert_element_exists(order_sent)
    with allure.step("全选取消"):
        frame_locator.get_by_label("Select all").check()
        frame_locator.get_by_text("取消选择").click()





@allure.step("设备门户操作")
def device_portal_operation(frame_locator, page: Page):
    logger.info("设备门户开始操作")
    try:
        frame_locator.get_by_text("已授权设备").click()
        frame_locator.locator("(//input[@class='ant-checkbox-input'])[2]").click() #选中 已授权设备第一个
        frame_locator.get_by_role("button", name="移除授权").click()
        #切换到待变更设备
        frame_locator.get_by_text("待变更设备", exact=True).click()
        frame_locator.locator("(//input[@class='ant-checkbox-input'])[2]").click()
        frame_locator.get_by_role("button", name="取 消").click()
        #切换到全部设备
        frame_locator.get_by_text("全部设备").click()
        frame_locator.get_by_role("button", name="更新列表").click()
        frame_locator.get_by_role("button", name="取消所有变更").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="导 出").click()
        download = download_info.value
        logger.info(f"导出{download.suggested_filename}")
        return download.path()


    except Exception as e:
        logger.error(f"选中表头时发生错误: {e}")
