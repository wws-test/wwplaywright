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
    frame_locator.get_by_role("button", name="setting 配置管理").click()
    with allure.step("非选中设置算法"):
        frame_locator.get_by_role("button", name="设置算法").click()
        # 等待元素出现
        order_sent = frame_locator.locator("div").filter(has_text=re.compile(r"^请先选择内容，再点击\"设置算法\"$")).nth(3)
        order_sent.wait_for()
    with allure.step("全选取消"):
        frame_locator.get_by_label("Select all").check()
        frame_locator.get_by_text("取消选择").click()
    with allure.step("切换条数"):
        frame_locator.get_by_text("条/页").click()
        frame_locator.get_by_text("100 条/页").click()
        frame_locator.get_by_label("Select all").check()


@allure.step("校验表头")
def check_table_header(frame_locator):
    logger.info("校验表头")
    try:
        expect(frame_locator.get_by_text("装置名称")).to_be_visible()
        expect(frame_locator.get_by_text("电磁阀名称")).to_be_visible()
        expect(frame_locator.get_by_text("重要程度")).to_be_visible()
        expect(frame_locator.get_by_text("健康度")).to_be_visible()
        expect(frame_locator.get_by_text("诊断结果", exact=True)).to_be_visible()
        expect(frame_locator.get_by_text("诊断时间")).to_be_visible()
        expect(frame_locator.get_by_label("诊断描述")).to_be_visible()
    except Exception as e:
        logger.error(f"校验表头时发生错误: {e}")


@allure.step("选中第一个设置算法-面积法")
def select_algorithm_setting(frame_locator):
    locator = frame_locator.locator("xpath=/html/body/div[1]/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/label/span/input")
    locator.click()
    logger.info("设置算法")
    frame_locator.get_by_role("button", name="设置算法").click()
    logger.info("选中第一个设置算法-机器学习分类算法")
    frame_locator.get_by_role("menuitem", name="机器学习分类算法").locator("a").click()
    frame_locator.locator(".ant-notification-notice-close").click()

@allure.step("选中第一个设置重要度-A")
def select_important_setting(frame_locator):
    locator = frame_locator.locator("xpath=/html/body/div[1]/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/label/span/input")
    locator.click()
    with allure.step("设置重要度B"):
        frame_locator.get_by_role("button", name="设置重要度").click()
        frame_locator.get_by_role("menuitem", name="B").locator("a").click()



@allure.step("下载报告")
def download_report(frame_locator,page):
    try:
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="upload 导出报告").click()

        download = download_info.value
        logger.info(f"下载报告{download.suggested_filename}")
        return download.path()
    except Exception as e:
        logger.error(f"下载报告时发生错误: {e}")
        return None

@allure.step("查询")
def solenoid_search(frame_locator, test):
    logger.info("开始搜索")
    try:
        frame_locator.get_by_placeholder("支持按装置名称、电磁阀名称、电磁阀类型、诊断算法、诊断结果、诊断描述字段的模糊查询").click()
        frame_locator.get_by_placeholder('支持按装置名称、电磁阀名称、电磁阀类型、诊断算法、诊断结果、诊断描述字段的模糊查询').fill(test)
        frame_locator.locator("div").filter(has_text=re.compile(r"^搜索：$")).locator("button").click()
    except Exception as e:
        logger.error(f"搜索时发生错误: {e}")

@allure.step("选中表头")
def select_table_header(frame_locator):
    logger.info("选中表头")
    try:
        frame_locator.locator('.model-pages-solenoid-components-solenoid-table-index-operator_style').click()
        frame_locator.get_by_label("电流类型").check()
        frame_locator.get_by_label("波形基线").check()
        frame_locator.get_by_label("诊断算法").check()
        frame_locator.get_by_label("快照时长").check()
        frame_locator.get_by_label("工况").check()
        frame_locator.get_by_label("电磁阀类型").check()
        frame_locator.get_by_role("button", name="确 定").click()
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
def export_report(frame_locator,page):
    logger.info("导出诊断报告")
    try:
        frame_locator.get_by_text("历史诊断").click()
        logger.info("选择第一个诊断报告，进入报告页面")
        frame_locator.locator("(//a[@class='model-pages-history-diagnosis-index-linkStyle'])[1]").click()
        frame_locator.get_by_role("button", name="check 有效诊断").click()
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.get_by_role("button", name="close 无效诊断").click()
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.get_by_role("button", name="eye 待观察").click()
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.locator("div").filter(has_text=re.compile(r"^健康度粘滞漏电$")).locator("svg").first.click()
        frame_locator.locator(".model-components-checkbox-comp-index-checkbox_style").first.click()
        frame_locator.locator("div").filter(has_text=re.compile(r"^健康度粘滞漏电$")).locator("svg").nth(1).click()
        frame_locator.locator("div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style").first.click()
        frame_locator.locator("div").filter(has_text=re.compile(r"^健康度粘滞漏电$")).locator("svg").nth(2).click()
        frame_locator.locator("div:nth-child(3) > .model-components-checkbox-comp-index-checkbox_style").first.dblclick()
        frame_locator.locator("div").filter(has_text=re.compile(r"^健康度粘滞漏电$")).locator("svg").nth(1).click()
        frame_locator.locator("div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style").first.dblclick()
        frame_locator.locator("div:nth-child(3) > .model-pages-item-comp-index-item_layout > .model-pages-item-comp-index-header_layout > .model-pages-item-comp-index-suffix_box > div > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").first.click()
        frame_locator.locator("div:nth-child(3) > .model-pages-item-comp-index-item_layout > .model-pages-item-comp-index-header_layout > .model-pages-item-comp-index-suffix_box > div > .model-components-checkbox-comp-index-checkbox_style").first.click()
        frame_locator.locator("div:nth-child(3) > .model-pages-item-comp-index-item_layout > .model-pages-item-comp-index-header_layout > .model-pages-item-comp-index-suffix_box > div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(3) > .model-pages-item-comp-index-item_layout > .model-pages-item-comp-index-header_layout > .model-pages-item-comp-index-suffix_box > div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(7) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.get_by_text("一周").click()
        frame_locator.get_by_text("一月").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="upload 导出报告").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
        return download.path()
    except Exception as e:
        logger.error(f"导出诊断报告时发生错误: {e}")

@allure.step("实时数据页面")
def real_time_data(frame_locator):
    logger.info("进入实时数据页面")
    try:
        frame_locator.get_by_text("实时数据").click()
        frame_locator.get_by_text("实时", exact=True).click()
        frame_locator.get_by_text("四小时").click()
        frame_locator.get_by_text("一天").click()
        frame_locator.get_by_text("一周").click()
        frame_locator.locator(".model-components-checkbox-comp-index-checkbox_style").first.click()
        frame_locator.locator(".model-components-checkbox-comp-index-checkbox_style").first.click()
        frame_locator.locator("div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(2) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(3) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(3) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(4) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(4) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(5) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(5) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(6) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(6) > .model-components-checkbox-comp-index-checkbox_style").click()
        frame_locator.locator("div:nth-child(7) > .model-components-checkbox-comp-index-checkbox_style > .anticon > svg").click()
        frame_locator.locator("div:nth-child(7) > .model-components-checkbox-comp-index-checkbox_style").click()
    except Exception as e:
        logger.error(f"进入实时数据页面时发生错误: {e}")

@allure.step("设备详情页面")
def device_details_page(frame_locator):
    logger.info("进入设备详情页面")
    try:
        frame_locator.get_by_text("设备详情").click()
        frame_locator.locator("a").filter(has_text="添加事件").click()
        frame_locator.get_by_label("事件类型").click()
        frame_locator.get_by_text("更换").click()
        frame_locator.locator(".ant-picker-input").click()
        frame_locator.get_by_text("此刻").click()
        frame_locator.locator("(//div[@class='ant-modal-footer']//button)[2]").click()
        frame_locator.locator("a").filter(has_text="查看事件").click()
        frame_locator.get_by_label("查看事件").locator("a").first.click()
        frame_locator.get_by_role("textbox", name="事件描述 :").click()
        frame_locator.get_by_role("textbox", name="事件描述 :").fill("222")
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.get_by_label("查看事件").locator("a").nth(1).click()
        frame_locator.get_by_role("button", name="确 定").click()
        frame_locator.get_by_label("Close", exact=True).click()

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
        frame_locator.locator("(//button[contains(@class,'ant-btn ant-btn-primary')]//span)[2]").click()
        frame_locator.get_by_role("button", name="暂无图片 开始诊断").click()
        locator = frame_locator.locator("text=诊断结果")
        locator.wait_for(timeout=100000)  # 等待最多 10 秒
        logger.info("断言诊断结果")
        with allure.step("断言诊断结果"):
            assert_element_exists(locator)
    except Exception as e:
        logger.error(f"进入自分析页面时发生错误: {e}")