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

@allure.step("阀门-报警")
def select_alarm_management(frame_locator: Page):
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()


@allure.step("阀门-历史报警")
def select_history_alarm_management(frame_locator: Page):
    frame_locator.locator(".ant-select-selection-overflow").click()
    frame_locator.get_by_title("恢复").locator("div").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()

@allure.step("阀门-调节阀预测")
def select_adjust_management(frame_locator: Page):
    frame_locator.locator(".ant-btn").first.click()
    frame_locator.locator(".ant-btn").first.click()
    frame_locator.locator("#rc_select_0").click()
    frame_locator.locator(".ant-select-selection-overflow").first.click()
    frame_locator.get_by_title("Draeger").locator("div").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.get_by_text("预测报表").click()
    frame_locator.locator("div").filter(has_text=re.compile(r"^月$")).click()
    frame_locator.locator("div").filter(has_text=re.compile(r"^年$")).click()
    frame_locator.get_by_text("实时诊断").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.get_by_text("历史诊断").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()

@allure.step("阀门-阀门小开度监测")
def select_small_opening_management(frame_locator: Page):
    frame_locator.locator("#rc_select_0").click()
    frame_locator.locator("//div[@title='报警']//div[1]").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.get_by_role("button", name="setting 列配置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="确 认").click()
    frame_locator.get_by_text("实时报警").click()
    frame_locator.get_by_text("历史报警").click()
    frame_locator.get_by_text("搁置配置").click()
    frame_locator.get_by_role("tab", name="设备").click()
    frame_locator.get_by_text("实时报警").click()

@allure.step("现场仪表-现场仪表监测")
def select_small_opening_detection_management(frame_locator: Page):
    frame_locator.locator("#rc_select_0").click()
    frame_locator.get_by_text("环保仪表").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.get_by_text("历史报警").click()
    frame_locator.locator("#rc_select_2").click()
    frame_locator.get_by_text("仪表", exact=True).click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.get_by_text("搁置配置").click()
    frame_locator.get_by_role("tab", name="设备").click()
    frame_locator.get_by_text("实时状态").click()

@allure.step("现场仪表-设备在线状态监测")
def select_device_management(frame_locator_3: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator_3.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")

    frame_locator_3.get_by_text("历史报警").click()
    frame_locator_3.get_by_text("搁置配置").click()
    frame_locator_3.locator("div").filter(has_text=re.compile(r"^报警设备$")).nth(3).click()
    frame_locator_3.get_by_role("tab", name="设备").click()


@allure.step("现场仪表-设备在线状态监测")
def device_online_status_management(frame_locator_3: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator_3.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")

    frame_locator_3.get_by_text("历史报警").click()
    frame_locator_3.get_by_text("搁置配置").click()
    frame_locator_3.get_by_role("tab", name="设备").click()

@allure.step("现场仪表-设备在线状态监测")
def fixed_alarm_management(frame_locator_3: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator_3.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator_3.get_by_text("实时报警").click()
    frame_locator_3.get_by_text("历史报警").click()
    frame_locator_3.get_by_text("搁置配置").click()
    frame_locator_3.get_by_role("tab", name="设备").click()
