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


@allure.step("知识标签")
def select_setting_management(frame_locator: Page, page: Page):
    frame_locator.get_by_role("button", name="plus-circle 新增").click()
    frame_locator.get_by_label("标签名称").click()
    frame_locator.get_by_label("标签名称").fill("111")
    frame_locator.get_by_role("button", name="确 定").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    frame_locator.locator("div").filter(has_text=re.compile(r"^1111编辑删除$")).locator("span").nth(3).click()
    frame_locator.get_by_role("button", name="确 定").click()


@allure.step("知识分类")
def select_knowledge_classification(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()

@allure.step("设备台账")
def select_device_ledger(frame_locator: Page, page: Page):
    frame_locator.get_by_role("tab", name="装置").click()
    frame_locator.get_by_role("tab", name="工厂模型").click()
    frame_locator.get_by_role("button", name="plus-circle 新增").click()
    frame_locator.get_by_label("设备号", exact=True).click()
    frame_locator.get_by_label("设备号", exact=True).fill("test")
    frame_locator.get_by_label("模式状态").click()
    frame_locator.get_by_text("缺省").click()
    frame_locator.get_by_label("设备名称").click()
    frame_locator.get_by_label("设备名称").fill("test")
    frame_locator.get_by_label("设备身份码").click()
    frame_locator.get_by_role("button", name="取 消").click()
    frame_locator.locator(".ant-checkbox-input").first.check()
    frame_locator.locator(".ant-checkbox-input").first.uncheck()
    frame_locator.get_by_role("button", name="setting 列配置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="重 置").click()
    frame_locator.get_by_role("button", name="取 消").click()
    frame_locator.get_by_text("接线箱").click()
    frame_locator.get_by_text("转速系统", exact=True).click()
    frame_locator.get_by_text("服务器", exact=True).click()

@allure.step("现存报警")
def select_existing_alarm(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息，平台确认人，故障原因，处理方式，处理人 字").click()
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息，平台确认人，故障原因，处理方式，处理人 字").fill("阀门")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息，平台确认人，故障原因，处理方式，处理人 字").press("Enter")
    frame_locator.get_by_role("button", name="close-circle").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_text("搁置配置").click()
    frame_locator.get_by_role("tab", name="设备").click()
    frame_locator.get_by_text("实时报警").nth(1).click()

@allure.step("历史报警")
def select_his_alarm(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息 字段的模糊搜索").click()
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息 字段的模糊搜索").fill("阀门")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置，设备名称，事件源信息，报警事件，厂商，设备型号，现场操作用户，平台确认信息 字段的模糊搜索").press("Enter")
    frame_locator.get_by_role("button", name="close-circle").click()
    frame_locator.get_by_role("button", name="search 搜索").click()