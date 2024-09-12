# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pages.ISDM.平台维护 import  *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入维护功能")
        login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        login_goto_project.page.get_by_text("仪控设备状态监测系统").click()
        login_goto_project.page.locator("#menu").get_by_text("平台维护").click()
        login_goto_project.page.locator("#menu").get_by_text("系统组态").click()
        login_goto_project.page.get_by_text("基础配置").click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")

    return frame_locator



@allure.step("工厂模型")
def test_set_management(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("工厂模型配置").click()
    select_knowledge_classification(frame_locator,login_goto_project.page)

@allure.step("通知配置")
def test_knowledge_classification(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("通知配置").click()
    select_device_ledger(frame_locator,login_goto_project.page)



















def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()















