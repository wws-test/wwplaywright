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
        expect(frame_locator.get_by_text("调节阀名称")).to_be_visible()
        expect(frame_locator.get_by_text("区域")).to_be_visible()
        expect(frame_locator.get_by_text("描述", exact=True)).to_be_visible()
        expect(frame_locator.get_by_text("设备厂商")).to_be_visible()
        expect(frame_locator.get_by_text("设备类型")).to_be_visible()
        expect(frame_locator.get_by_text("诊断结果", exact=True)).to_be_visible()
        expect(frame_locator.get_by_label("诊断时间")).to_be_visible()
        expect(frame_locator.get_by_label("重要程度")).to_be_visible()
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
        frame_locator.get_by_placeholder("支持按调节阀名称、区域、描述、设备厂商、设备类型、诊断结果、诊断描述的模糊查询").click()

        frame_locator.get_by_placeholder("支持按调节阀名称、区域、描述、设备厂商、设备类型、诊断结果、诊断描述的模糊查询").fill("SVP-V2")
        frame_locator.locator("button").nth(2).click()
    except Exception as e:
        logger.error(f"搜索时发生错误: {e}")

@allure.step("选中表头")
def select_table_header(frame_locator):
    logger.info("选中表头")
    try:
        frame_locator.locator('.model-pages-home-table-index-operate').click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[1]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[2]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[3]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[4]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[5]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[6]").click()
        frame_locator.locator("(//span[@class='ant-checkbox']//input)[7]").click()
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
        frame_locator.get_by_title("死区").locator("img").click()
        frame_locator.get_by_title("粘滞程度").get_by_role("paragraph").click()
        frame_locator.get_by_title("偏离程度").get_by_role("paragraph").click()
        frame_locator.get_by_title("跟踪性能").get_by_role("paragraph").click()
        frame_locator.get_by_title("堵塞/冲刷系数").click()
        frame_locator.get_by_text("有效诊断").click()
        frame_locator.get_by_text("无效诊断").click()
        frame_locator.get_by_text("待观察").click()
        frame_locator.locator("#pride_regulating_report_group_4 canvas").click()
        frame_locator.locator("#pride_regulating_report_group_4 canvas").click()
        frame_locator.locator("#pride_regulating_report_group_4 canvas").click()
        frame_locator.locator("#pride_regulating_report_group_4 canvas").click()
        frame_locator.locator("#pride_regulating_report_group_4 canvas").click()
        frame_locator.locator("#pride_regulating_report_group_4 div").filter(has_text=re.compile(r"^堵塞/冲刷系数$")).click()
        frame_locator.get_by_label("redo").locator("svg").click()
        frame_locator.get_by_text("一天").click()
        frame_locator.get_by_text("一周").click()
        frame_locator.get_by_text("一月").click()
        with page.expect_download() as download_info:
            frame_locator.get_by_role("button", name="导出报告").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
        return download.path()
    except Exception as e:
        logger.error(f"导出诊断报告时发生错误: {e}")

@allure.step("设备详情页面")
def device_details_page(frame_locator):
    logger.info("进入设备详情页面")
    try:
        frame_locator.get_by_text("一小时").click()
        frame_locator.get_by_text("一天").click()
        frame_locator.get_by_text("一周").click()
        frame_locator.get_by_text("一月").click()
        frame_locator.get_by_title("历史统计").get_by_role("paragraph").click()
        frame_locator.locator("(//p[@class='model-pages-detail-diag-list-index-diagMore'])[2]").click()


    except Exception as e:
        logger.error(f"进入设备详情页面时发生错误: {e}")
