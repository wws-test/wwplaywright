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



@allure.step("校验表头")
def check_table_header(frame_locator):
    logger.info("校验表头")
    try:
        expect(frame_locator.get_by_text("装置名称")).to_be_visible()
        expect(frame_locator.get_by_text("变送器名称")).to_be_visible()
        expect(frame_locator.get_by_text("重要程度")).to_be_visible()
        expect(frame_locator.get_by_text("工况")).to_be_visible()
        expect(frame_locator.get_by_text("描述", exact=True)).to_be_visible()
        expect(frame_locator.get_by_text("诊断结果", exact=True)).to_be_visible()
        expect(frame_locator.get_by_label("诊断时间")).to_be_visible()
        expect(frame_locator.get_by_label("诊断描述")).to_be_visible()

    except Exception as e:
        logger.error(f"校验表头时发生错误: {e}")




@allure.step("选中第一个设置重要度-B")
def select_important_setting(frame_locator):
    frame_locator.locator("(//input[@type='checkbox'])[2]").click()
    with allure.step("设置重要度B"):
        frame_locator.get_by_role("button", name="设置重要度").click()
        frame_locator.locator("(//div[@class='model-layouts-index-importanceContent']//p)[2]").click()



@allure.step("下载报告")
def download_report(frame_locator,page):
    try:
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="导出报告").click()
        download = download_info.value
        logger.info(f"下载报告{download.suggested_filename}")
        return download.path()
    except Exception as e:
        logger.error(f"下载报告时发生错误: {e}")
        return None

@allure.step("查询")
def solenoid_search(frame_locator):
    logger.info("开始搜索")
    try:
        frame_locator.get_by_placeholder("支持按装置名称、变送器名称、描述、设备厂商、设备类型、诊断结果、诊断描述的模糊查询").click()

        frame_locator.get_by_placeholder("支持按装置名称、变送器名称、描述、设备厂商、设备类型、诊断结果、诊断描述的模糊查询").fill("EJA-NEXT")
        frame_locator.locator("button").nth(2).click()
    except Exception as e:
        logger.error(f"搜索时发生错误: {e}")


    except Exception as e:
        logger.error(f"选中表头时发生错误: {e}")


@allure.step("取消选中表头")
def unselect_table_header(frame_locator):
    logger.info("取消选中表头")
    try:
        frame_locator.locator('.model-pages-solenoid-components-solenoid-table-index-operator_style').click()
        frame_locator.get_by_role("button", name="重 置").click()
    except Exception as e:
        logger.error(f"取消选中表头时发生错误: {e}")

@allure.step("历史诊断页面-导出诊断报告")
def export_report(iframe_locator,page):
    logger.info("导出诊断报告")
    try:
        iframe_locator.locator("(//div[@class='ant-tabs-tab-btn'])[3]").click() # 切换到历史诊断页面
        iframe_locator.locator("(//div[@class='model-pages-detail-history-index-table_operate']//a)[1]").click() #点击具体详情
        iframe_locator.get_by_text("点击扫二维码").click()
        iframe_locator.get_by_text("×").click()
        iframe_locator.get_by_text("有效诊断").click()
        iframe_locator.get_by_role("button", name="确 定").click()
        iframe_locator.get_by_text("无效诊断").click()
        iframe_locator.get_by_role("button", name="确 定").click()
        with page.expect_download() as download_info:
            iframe_locator.get_by_role("button", name="导出报告").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
        return download.path()
    except Exception as e:
        logger.error(f"导出诊断报告时发生错误: {e}")

@allure.step("设备详情页面")
def device_details_page(frame_locator):
    logger.info("进入设备详情页面")
    try:
        frame_locator.get_by_role("tab", name="设备详情").click()
        frame_locator.get_by_role("button", name="plus 添加事件").click()
        frame_locator.get_by_role("button", name="取 消").click()
        frame_locator.get_by_role("button", name="eye 事件预览").click()
        frame_locator.get_by_role("button", name="关 闭").click()
        frame_locator.get_by_label("引压管堵塞综合指标").uncheck()
        frame_locator.get_by_label("设备健康度").uncheck()
        frame_locator.get_by_text("点击扫二维码").click()
        frame_locator.get_by_text("×").click()

    except Exception as e:
        logger.error(f"进入设备详情页面时发生错误: {e}")

@allure.step("自分析页面")
def self_analysis_page(frame_locator):
    logger.info("进入自分析页面")
    try:
        frame_locator.get_by_text("自分析").click()
        frame_locator.get_by_placeholder("开始日期").click()
        frame_locator.locator("(//td[@class='ant-picker-cell ant-picker-cell-in-view']//div)[1]").click()
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.get_by_placeholder("结束日期").click()
        # frame_locator.locator("(//button[contains(@class,'ant-btn ant-btn-primary')]//span)[2]").click()
        frame_locator.locator("//button[@class='ant-btn ant-btn-primary']").click()
        locator = frame_locator.locator("text=指标总览")
        locator.wait_for(timeout=100000)  # 等待最多 10 秒
        logger.info("断言指标总览")
        with allure.step("断言指标总览"):
            assert_element_exists(locator)
    except Exception as e:
        logger.error(f"进入自分析页面时发生错误: {e}")


@allure.step("实时数据页面")
def real_time_data(iframe_locator):
    logger.info("进入实时数据页面")
    try:
        iframe_locator.get_by_role("tab", name="实时数据").click()
        iframe_locator.get_by_text("实时", exact=True).click()
        iframe_locator.get_by_text("一天").click()
        iframe_locator.get_by_text("一周").click()
        iframe_locator.get_by_text("一月").click()
    except Exception as e:
        logger.error(f"进入实时数据页面时发生错误: {e}")