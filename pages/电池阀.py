# !/usr/bin/python3
# -*- coding: utf-8 -*-

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


@allure.step("选中第一个设置算法-面积法")
def select_algorithm_setting(frame_locator):
    locator = frame_locator.locator("xpath=/html/body/div[1]/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/label/span/input")
    locator.click()
    logger.info("设置算法")
    frame_locator.get_by_role("button", name="设置算法").click()
    logger.info("选中第一个设置算法-机器学习分类算法")
    frame_locator.get_by_role("menuitem", name="机器学习分类算法").locator("a").click()





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
#         select_algorithm_setting(frame_locator)


