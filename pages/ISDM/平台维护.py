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

@allure.step("全局配置")
def notification_configuration(iframe,page: Page):
    iframe.get_by_text("全局配置").click()
    iframe.get_by_role("tab", name="设备默认视图").click()
    iframe.get_by_role("tab", name="总貌图报警闪烁").click()
    iframe.locator("div").filter(has_text=re.compile(r"^设备参数备份$")).first.click()
    iframe.get_by_role("tab", name="管理驾驶舱").click()
    iframe.get_by_role("button", name="保 存").click()
    iframe.get_by_role("tab", name="设备参数备份").click()
    iframe.get_by_role("button", name="保 存").click()
    iframe.get_by_role("tab", name="总貌图报警闪烁").click()
    iframe.get_by_text("不闪烁").click()
    iframe.get_by_text("闪烁", exact=True).click()
    iframe.get_by_text("邮箱配置设备默认视图总貌图报警闪烁设备参数备份管理驾驶舱").click()
    iframe.get_by_role("tab", name="设备默认视图").click()
    iframe.get_by_role("tab", name="邮箱配置").click()
    iframe.get_by_role("button", name="保 存").click()


@allure.step ("ECS-700机柜组态配置")
def operate_cabinet (iframe: Page, page: Page):
    iframe.get_by_role ("button", name="search 搜索").click ()
    iframe.get_by_role ("button", name="clear 重置").click ()
    iframe.get_by_role ("button", name="plus-circle 新增").click ()
    iframe.get_by_label ("机柜名称").click ()
    iframe.get_by_label ("机柜名称").fill ("333")
    iframe.get_by_role ("button", name="取 消").click ()
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 导出机柜数据").click ()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.locator ("#rc_select_0").click ()
    iframe.locator (".ant-select-item-option-content").first.click ()
    iframe.get_by_role ("button", name="search 搜索").click ()


@allure.step("诊断项模板配置")
def template_operations(iframe,page):
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("模板名称").click()
    iframe.get_by_label("模板名称").fill("33333")
    iframe.get_by_role("button", name="添加诊断项").click()
    iframe.get_by_text("添加子项").click()
    iframe.get_by_label("新增").get_by_text("删除").nth(1).click()
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()
    iframe.get_by_text("诊断项模板：搜索重置").click()
    iframe.get_by_placeholder("请输入").click()
    iframe.get_by_placeholder("请输入").fill("33333")
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()


@allure.step("设备字段配置")
def set_field_configuration(frame: Page, page: Page):
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()
    frame.locator("#rc_select_0").click()
    frame.get_by_text("字符串").click()
    frame.get_by_placeholder("请输入").click()
    frame.get_by_placeholder("请输入").fill("33333")
    frame.locator("#rc_select_1").click()
    frame.get_by_text("是", exact=True).click()
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()
    frame.get_by_role("button", name="plus-circle 新增").click()
    frame.get_by_label("字段名称").click()
    frame.get_by_label("字段名称").fill("3333")
    frame.get_by_label("字段类型").click()
    frame.get_by_text("字符串").nth(1).click()
    frame.get_by_label("展示顺序").click()
    frame.get_by_label("展示顺序").fill("222")
    frame.get_by_label("长度限制").click()
    frame.get_by_label("长度限制").fill("111")
    frame.locator("div:nth-child(7) >.ant-form-item >.ant-row >.ant-col >.ant-form-item-control-input").click()
    frame.get_by_label("显示查询").check()
    frame.get_by_label("是否唯一").check()


@allure.step ("设备型号配置")
def Device_model_configuration (frame_content: Page, page: Page):
    frame_content.get_by_role ("button", name="sync 同步数据").click ()
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_content.get_by_role ("button", name="search 搜索").click ()
    frame_content.get_by_role ("button", name="clear 重置").click ()
    frame_content.locator (".ant-checkbox-input").first.check ()
    frame_content.locator (".ant-checkbox-input").first.uncheck ()


@allure.step ("机柜间配置")
def cabinet_room_operations (frame_content: Page, page: Page):
    frame_content.get_by_role ("button", name="plus-circle 新增").click ()
    frame_content.get_by_label ("机柜间名称").click ()
    frame_content.get_by_label ("机柜间名称").fill ("33333")
    frame_content.get_by_label ("机柜间温度位号").click ()
    frame_content.get_by_label ("机柜间温度位号").fill ("333")
    frame_content.get_by_label ("机柜间湿度位号").click ()
    frame_content.get_by_label ("机柜间湿度位号").fill ("333333")
    frame_content.get_by_label ("备注").click ()
    frame_content.get_by_label ("备注").fill ("3333")
    frame_content.get_by_role ("button", name="取 消").click ()
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_content.locator (".ant-checkbox-input").first.check ()
    frame_content.locator (".ant-checkbox-input").first.uncheck ()

@allure.step ("通道配置")
def smart_bind_operation (iframe: Page, page: Page):
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.get_by_role ("button", name="plus-circle 新增").click ()
    iframe.get_by_label ("卡件位号").click ()
    iframe.get_by_label ("卡件位号").fill ("33333")
    iframe.get_by_role ("button", name="添加通道").click ()
    iframe.get_by_role ("button", name="添加通道").click ()
    iframe.get_by_role ("button", name="取 消").click ()
    iframe.get_by_role ("button", name="link 智能绑定").click ()
    iframe.locator ("#rc_select_0").click ()
    iframe.locator ("#rc_select_0").fill ("11")
    iframe.get_by_role ("button", name="search 搜索").click ()
    iframe.get_by_role ("button", name="clear 重置").click ()

@allure.step("机柜配置")
def cabinet_operations(frame: Page, page: Page):
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="sync 同步").click()
    frame.get_by_role("button", name="plus-circle 新增").click()
    frame.get_by_label("机柜名称").click()
    frame.get_by_label("机柜名称").fill("333")
    frame.get_by_label("机柜类型").click()
    frame.get_by_label("机柜类型").fill("333")
    frame.get_by_label("机柜温度位号").click()
    frame.get_by_label("机柜温度位号").fill("33")
    frame.get_by_label("机柜湿度位号").click()
    frame.get_by_label("机柜湿度位号").fill("33")
    frame.get_by_label("仪表电源位号").click()
    frame.get_by_label("仪表电源位号").fill("33")
    frame.get_by_label("温控器位号").click()
    frame.get_by_label("温控器位号").fill("33")
    frame.get_by_role("button", name="取 消").click()
    frame.get_by_placeholder("请输入").click()
    frame.get_by_placeholder("请输入").fill("333")
    frame.get_by_text("机柜：搜索重置").click()
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()
    frame.locator("._head-cell-block_187e9_71").click()
    frame.locator("._head-cell-block_187e9_71").click()


@allure.step("设备组配置")
def operate_device_ledger(frame: Page, page: Page):
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame.get_by_role("button", name="plus-circle 新增").click()
    frame.get_by_label("设备组").click()
    frame.get_by_label("设备组").fill("3333")
    frame.get_by_role("button", name="取 消").click()
    frame.get_by_placeholder("请输入").click()
    frame.get_by_placeholder("请输入").fill("3333")
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()
    frame.locator(".ant-checkbox-wrapper").first.click()
    frame.locator(".ant-checkbox-input").first.uncheck()

@allure.step("控制系统配置")
def control_system_operations(iframe: Page, page: Page):
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("控制系统名称").click()
    iframe.get_by_label("控制系统名称").fill("333")
    iframe.get_by_label("控制系统类型").click()
    iframe.locator(".ant-select-item-option-content").first.click()
    iframe.get_by_label("工厂模型").click()
    iframe.get_by_label("工厂模型").fill("3333")
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_placeholder("请输入").click()
    iframe.get_by_placeholder("请输入").fill("3333")
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()
    iframe.locator("#rc_select_0").click()
    iframe.get_by_text("控制系统名称：控制系统类型：请选择").click()
    iframe.get_by_role("button", name="clear 重置").click()
    iframe.locator(".ant-checkbox-input").first.check()
    iframe.locator(".ant-checkbox-input").first.uncheck()
    iframe.locator(".ant-btn").first.click()
    iframe.locator(".ant-btn").first.click()

@allure.step("阀门报警配置")
def valve_alarm_configuration(frame_content: Page, page: Page):
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_content.get_by_placeholder("请输入").click()
    frame_content.get_by_placeholder("请输入").fill("3333")
    frame_content.get_by_role("button", name="search 搜索").click()
    frame_content.get_by_role("button", name="clear 重置").click()
    frame_content.get_by_role("button", name="plus-circle 新增").click()
    frame_content.get_by_label("阀门报警任务").click()
    frame_content.get_by_label("阀门报警任务").fill("3333")
    frame_content.get_by_label("设备").click()
    frame_content.get_by_label("设备").fill("3333333")
    frame_content.get_by_label("报警方式").click()
    frame_content.get_by_text("主动").click()
    frame_content.locator("#unit").click()
    frame_content.get_by_text("时", exact=True).click()
    frame_content.locator("#time").click()
    frame_content.locator("#time").fill("3")
    frame_content.get_by_label("报警", exact=True).click()
    frame_content.get_by_role("button", name="取 消").click()
    frame_content.get_by_placeholder("请输入").click()
    frame_content.get_by_placeholder("请输入").fill("3333")
    frame_content.get_by_role("button", name="search 搜索").click()
    frame_content.get_by_role("button", name="clear 重置").click()


@allure.step("开停工配置")
def selectstart_stop_configuration(iframe: Page, page: Page):
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("启用").click()
    iframe.get_by_label("启用").click()
    iframe.get_by_label("位号").click()
    iframe.get_by_label("位号").fill("3333333333333333333")
    iframe.get_by_role("button", name="取 消").click()
    iframe.locator(".ant-select-selector").first.click()
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()

@allure.step("报警通知过滤")
def alarm_notification_filtering(frame_content: Page, page: Page):
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_content.get_by_role("button", name="plus-circle 新增").click()
    frame_content.get_by_label("过滤策略").click()
    frame_content.get_by_label("过滤策略").fill("33333")
    frame_content.get_by_role("button", name="添加过滤器").click()
    frame_content.get_by_role("button", name="添加过滤器").click()
    frame_content.get_by_label("新增").get_by_text("删除").nth(1).click()
    frame_content.get_by_role("button", name="取 消").click()
    frame_content.get_by_placeholder("请输入").click()
    frame_content.get_by_placeholder("请输入").fill("33333")
    frame_content.get_by_role("button", name="search 搜索").click()
    frame_content.get_by_role("button", name="clear 重置").click()
    frame_content.locator(".ant-checkbox-input").first.check()
    frame_content.locator(".ant-checkbox-input").first.uncheck()

@allure.step("报警过滤")
def alarm_filtering(frame_content: Page, page: Page):
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame_content.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_content.get_by_role("button", name="plus-circle 新增").click()
    frame_content.get_by_label("过滤策略").click()
    frame_content.get_by_label("过滤策略").fill("33333")
    frame_content.get_by_role("button", name="添加过滤器").click()
    frame_content.get_by_role("button", name="添加过滤器").click()
    frame_content.get_by_label("新增").get_by_text("删除").nth(1).click()
    frame_content.get_by_role("button", name="取 消").click()
    frame_content.get_by_placeholder("请输入").click()
    frame_content.get_by_placeholder("请输入").fill("33333")
    frame_content.get_by_role("button", name="search 搜索").click()
    frame_content.get_by_role("button", name="clear 重置").click()
    frame_content.locator(".ant-checkbox-input").first.check()
    frame_content.locator(".ant-checkbox-input").first.uncheck()

@allure.step("报警拦截器")
def Alarm_blocker(iframe: Page, page: Page):
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("过滤策略").click()
    iframe.get_by_label("过滤策略").fill("3333")
    iframe.get_by_label("报警等级").click()
    iframe.get_by_text("故障").click()
    iframe.get_by_role("button", name="添加过滤器").click()
    iframe.get_by_role("button", name="添加过滤器").click()
    iframe.get_by_label("新增").get_by_text("删除").nth(1).click()
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_placeholder("请输入").click()
    iframe.get_by_placeholder("请输入").fill("3333")
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()

@allure.step("消息触发器-报警")
def message_trigger_p(iframe: Page, page: Page):
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("名称").click()
    iframe.get_by_label("名称").fill("3333")
    iframe.get_by_label("报警事件").click()
    iframe.get_by_label("报警事件").fill("3333")
    iframe.get_by_label("报警等级").click()
    iframe.get_by_title("故障").click()
    iframe.get_by_label("发送方式").click()
    iframe.get_by_text("定时").click()
    iframe.locator(".ant-picker-input").click()
    iframe.get_by_text("此刻").click()
    iframe.get_by_label("触发次数").click()
    iframe.get_by_label("触发次数").fill("333")
    iframe.locator("#triggerTime").click()
    iframe.locator("#triggerTime").fill("333")
    iframe.locator("#triggerTime").click()
    iframe.locator("#triggerTimeUnit").click()
    iframe.get_by_title("小时").click()
    iframe.locator("#rangeStart").click()
    iframe.locator("#rangeStart").fill("33")
    iframe.locator("#rangeEnd").click()
    iframe.locator("#rangeEnd").fill("333")
    iframe.locator("#rangeUnit").click()
    iframe.get_by_text("小时").nth(2).click()
    iframe.locator("#expireTime").click()
    iframe.locator("#expireTime").fill("333")
    iframe.locator("#expireUnit").click()
    iframe.get_by_text("小时").nth(4).click()
    iframe.get_by_role("button", name="取 消").click()
    iframe.locator(".ant-checkbox-input").first.check()
    iframe.locator(".ant-checkbox-input").first.uncheck()



@allure.step("消息触发器报表操作")
def message_trigger_report_operations(frame: Page, page: Page):
    frame.get_by_text("报表").click()
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 全量导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        frame.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")

    frame.get_by_role("button", name="plus-circle 新增").click()
    frame.get_by_label("名称").click()
    frame.get_by_label("名称").fill("333")
    frame.get_by_role("button", name="取 消").click()
    frame.get_by_placeholder("请输入").click()
    frame.get_by_placeholder("请输入").fill("3333")
    frame.get_by_role("button", name="search 搜索").click()
    frame.get_by_role("button", name="clear 重置").click()
    frame.locator("._head-cell-block_187e9_71").click()
    frame.locator(".ant-checkbox-input").first.uncheck()


@allure.step("消息触发器开停工操作")
def Message_trigger_start_shutdown(iframe: Page, page: Page):
    iframe.get_by_text("开停工").click()
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 导出").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    with page.expect_download() as download_info:
        iframe.get_by_role ("button", name="download 模板下载").click ()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    iframe.get_by_placeholder("请输入").click()
    iframe.get_by_placeholder("请输入").fill("33333")
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("名称").click()
    iframe.get_by_label("名称").fill("3333")
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_label("", exact=True).first.check()
    iframe.get_by_label("", exact=True).first.uncheck()


@allure.step("设备组任务")
def Device_GroupTask(content_frame,page):
    try:
        with allure.step('点击新增按钮'):
            content_frame.get_by_role("button", name="plus-circle 新增").click()
        with allure.step('点击任务名称输入框并输入内容'):
            content_frame.get_by_label("任务名称").click()
            content_frame.get_by_label("任务名称").fill("333")
        with allure.step('点击启用按钮两次'):
            content_frame.get_by_label("启用").click()
            content_frame.get_by_label("启用").click()
        with allure.step('点击取消按钮'):
            content_frame.get_by_role("button", name="取 消").click()
        with allure.step('点击特定任务文本并进行后续操作'):
            content_frame.get_by_text("任务名称：搜索重置").click()
            content_frame.locator(".ant-input-suffix").click()
            content_frame.get_by_placeholder("请输入").fill("333")
            content_frame.get_by_role("button", name="search 搜索").click()
            content_frame.get_by_role("button", name="clear 重置").click()
    except Exception as e:
        allure.attach(page.screenshot(), name='错误截图', attachment_type=allure.attachment_type.PNG)
        raise e



@allure.step("阀门小开度配置")
def Valve_opening_configuration(iframe: Page, page: Page,PageDownload):
    # 定义需要点击的按钮名称列表
    button_names = ["download 导出", "download 模板下载"]

    # 使用 fixture 函数，并传入按钮名称列表
    PageDownload(iframe, button_names)
    iframe.get_by_role("button", name="plus-circle 新增").click()
    iframe.get_by_label("设备名称").click()
    iframe.get_by_label("设备名称").fill("333333")
    iframe.get_by_label("行程位号").click()
    iframe.get_by_label("行程位号").fill("3333333333333")
    iframe.get_by_placeholder("阈值低限（含此值）").click()
    iframe.get_by_placeholder("阈值低限（含此值）").fill("33333333")
    iframe.get_by_placeholder("阈值高限（含此值）").click()
    iframe.get_by_placeholder("阈值高限（含此值）").fill("33333333333333")
    iframe.locator("#time").click()
    iframe.locator("#time").fill("33")
    iframe.locator("#unit").click()
    iframe.get_by_text("小时", exact=True).click()
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_role("button", name="search 搜索").click()
    iframe.get_by_role("button", name="clear 重置").click()
    iframe.locator("._head-cell-block_187e9_71").click()
    iframe.locator(".ant-checkbox-input").first.uncheck()