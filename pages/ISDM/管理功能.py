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

@allure.step("现存报警")
def select_existing_alarm(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").click()
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").fill("阀门")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").press("Enter")
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
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").click()
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").fill("阀门")
    frame_locator.get_by_placeholder("支持按 数据源类型，设备类别，厂区，装置").press("Enter")
    frame_locator.get_by_role("button", name="close-circle").click()
    frame_locator.get_by_role("button", name="search 搜索").click()


@allure.step("KPI-联锁投用率")
def select_duo_branch(frame: Page, page: Page):
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_text("历史记录").click()
    frame.get_by_text("联锁监控").click()
    frame.get_by_role("button", name="search 搜索").nth(1).click()
    frame.get_by_role("button", name="clear 重置").nth(1).click()
    frame.get_by_role("button", name="search 搜索").first.click()
    frame.get_by_role("button", name="clear 重置").first.click()
    frame.get_by_text("历史记录").click()
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()

@allure.step("KPI-设备报警KPI")
def select_device_alarm_kpi(frame: Page, page: Page):
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
        frame.get_by_text("报警总数").click()
        frame.get_by_text("总报警率").click()
        frame.locator("canvas").nth(1).click(position={"x": 140, "y": 93})
        frame.locator("canvas").nth(1).click(position={"x": 358, "y": 203})
        frame.locator("canvas").nth(1).click(position={"x": 524, "y": 226})

@allure.step("KPI-厂商KPI")
def select_control_system_kpi(frame_locator: Page):
    frame_locator.locator("canvas").first.click(position={"x":239,"y":92})
    frame_locator.locator("canvas").nth(1).click(position={"x":228,"y":69})
    frame_locator.locator("canvas").nth(2).click(position={"x":144,"y":79})
    frame_locator.locator("canvas").nth(1).click(position={"x":126,"y":84})
    frame_locator.locator("canvas").first.click(position={"x":253,"y":127})
    frame_locator.locator("canvas").nth(3).click(position={"x":193,"y":119})
    frame_locator.locator("canvas").nth(4).click(position={"x":579,"y":14})
    frame_locator.locator("canvas").nth(4).click(position={"x":542,"y":10})
    frame_locator.locator("canvas").nth(4).click(position={"x":480,"y":12})

@allure.step("KPI-装置KPI")
def select_device_kpi(frame: Page):
    frame.get_by_role("button", name="close-circle").click()
    frame.locator(".ant-picker").click()
    frame.get_by_text("本月").click()
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()

@allure.step("KPI-智能仪表台账统计")
def select_smart_meter_statistics(frame_locator: Page, page: Page):
    with page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.locator("canvas").first.click(position={"x":239,"y":92})
    frame_locator.locator("canvas").nth(1).click(position={"x":228,"y":69})
    frame_locator.locator("canvas").nth(2).click(position={"x":144,"y":79})
    frame_locator.locator("canvas").nth(1).click(position={"x":126,"y":84})
    frame_locator.locator("canvas").first.click(position={"x":253,"y":127})
    frame_locator.locator("canvas").nth(3).click(position={"x":193,"y":119})
    frame_locator.locator("canvas").nth(4).click(position={"x":87,"y":225})
    frame_locator.locator("canvas").nth(4).click(position={"x":141,"y":228})
    frame_locator.locator("canvas").nth(4).click(position={"x":220,"y":229})
    frame_locator.locator("canvas").nth(4).click(position={"x":319,"y":225})
    frame_locator.locator("canvas").nth(4).click(position={"x":384,"y":228})
    frame_locator.locator("canvas").nth(4).click(position={"x":464,"y":224})
    frame_locator.locator("canvas").nth(4).click(position={"x":539,"y":228})

@allure.step("KPI-数字化巡检")
def select_digital_inspection(frame2: Page, page: Page):
    frame2.get_by_role("button", name="搜 索").click()
    frame2.locator(".ant-select-selector").first.click()
    frame2.locator(".ant-select-selector").first.click()
    frame2.get_by_role("button", name="redo 重置").click()
    frame2.get_by_role("button", name="setting 列配置").click()
    frame2.get_by_role("button", name="取 消").click()

@allure.step("周月报表")
def select_weekly_monthly_report(frame: Page, page: Page):

    frame.get_by_text("周报").click()
    frame.get_by_title("月报").click()
    frame.get_by_role("button", name="search 搜索").click()
    page.wait_for_timeout(2000)
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").first.click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="info-circle 报表简述").click()
    frame.get_by_label("Close", exact=True).click()

    frame.get_by_role("tab", name="报警等级分布").click()
    frame.get_by_text("周报").click()
    frame.get_by_text("月报", exact=True).click()
    frame.get_by_role("button", name="search 搜索").click()
    page.wait_for_timeout(2000)
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").first.click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="info-circle 报表简述").click()
    frame.get_by_label("Close", exact=True).click()

    frame.get_by_role("tab", name="全厂报警完好率").click()
    frame.get_by_text("周报").click()
    frame.get_by_text("月报", exact=True).click()
    frame.get_by_role("button", name="search 搜索").click()
    page.wait_for_timeout(2000)
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").first.click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="info-circle 报表简述").click()
    frame.get_by_label("Close", exact=True).click()

    frame.get_by_role("tab", name="每日报警设备数").click()
    frame.get_by_text("周报").click()
    frame.get_by_text("月报", exact=True).click()
    frame.get_by_role("button", name="search 搜索").click()
    page.wait_for_timeout(2000)
    with page.expect_download() as download_info:
        frame.get_by_role("button", name="download 导出").first.click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="info-circle 报表简述").click()
    frame.get_by_label("Close", exact=True).click()
