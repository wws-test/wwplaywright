# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure
from log import logger
from playwright.sync_api import Page


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
# class SolenoidPage:
#     def __init__(self, page: Page, base_url: str):
#         self.page = page
#         self.base_url = base_url
#
#     # 定义页面元素
#     def Solenoid_menu_1(self):
#         return self.page.locator("span[title='电磁阀诊断']")
#
#     def Solenoid_menu_2(self):
#         return self.page.locator("span[title='电磁阀在线诊断']")
#
#     def Solenoid_frame_locator(self):
#         frame_locator = self.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
#         return  frame_locator
#
#     # 定义操作
#     @allure.step("进入电磁阀诊断页面")
#     def Solenoid_menu(self):
#         self.page.goto(self.base_url+"/#/hellow")
#         self.Solenoid_menu_1().click()
#         self.Solenoid_menu_2().click()
#         frame_locator = self.Solenoid_frame_locator()
#         select_setting_management(frame_locator)
#         select_algorithm_setting(frame_locator)un


