# !/usr/bin/python3
# -*- coding: utf-8 -*-
import allure

from common.mpw import PageWrapper
from pages.ISDM.平台维护 import  *

def navigate_to_solenoid_diagnosis_page(page: PageWrapper):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入维护功能")
        page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        page.get_by_text("仪控设备状态监测系统").click()
        page.locator("#menu").get_by_text("平台维护").click()
        page.locator("#menu").get_by_text("系统组态").click()
        page.get_by_text("基础配置").click()
    return page


@allure.step("通知配置")
def test_knowledge_classification(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("通知配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    select_device_ledger_P(page)




@allure.story("机柜间配置")
def test_cabinets_configuration(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("机柜间配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    cabinet_room_operations_P(page)


@allure.story("机柜配置")
def test_cabinet_configuration(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("机柜配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    cabinet_operations_p(page)



@allure.story("报警过滤")
def test_alarm_filtering(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("报警过滤").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    alarm_filtering_p(page)


@allure.story("控制系统配置+固定了机柜D1")
def test_control_system_configuration(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("控制系统配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    control_system_operations_p(page)




@allure.story("阀门报警配置")
def test_valve_alarm_configuration(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("阀门报警配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    valve_alarm_configuration_p(page)



def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()















