# !/usr/bin/python3
# -*- coding: utf-8 -*-
from idlelib.debugger_r import frametable

import allure

from common.mpw import PageWrapper
from pages.ISDM.控制系统 import  *

def navigate_to_solenoid_diagnosis_page(page: PageWrapper):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入状态检测")
        page.switch_to_main_frame()
        page.get_by_title("首页").click()
        page.get_by_text("仪控设备状态监测系统").click()
        page.get_by_text("状态监测", exact=True).click()
    return page

def navigate_to_solenoid_diagnosis_page1(page: PageWrapper):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入管理功能")
        page.switch_to_main_frame()
        page.get_by_title("首页").click()
        page.get_by_text("仪控设备状态监测系统").click()
        page.locator("#menu").get_by_text("管理功能").click()
    return page


@allure.story("驾驶舱项目-控制系统-报警列表")
def test_set_management1( login_goto_project: PageWrapper):
    navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.get_by_text("控制系统",exact=True).click()
    login_goto_project.get_by_text("报警列表",exact=True).click_with_timing()


@allure.story("驾驶舱项目-控制系统-预测性维护")
def test_predictive_maintenance1( login_goto_project: PageWrapper):
    navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.get_by_text("控制系统").click()
    login_goto_project.get_by_text("预测性维护").click_with_timing()


@allure.story("驾驶舱项目-阀门-调节阀预测")
def test_valve_adjust_predict1(login_goto_project: PageWrapper):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.get_by_text("阀门").click()
    page.locator("#menu").get_by_text("调节阀预测").click_with_timing()

@allure.story("现存报警")
def test_workshop3_monitoring( login_goto_project,):
    page = navigate_to_solenoid_diagnosis_page1(login_goto_project)
    page.get_by_text("报警", exact=True).click()
    page.get_by_text("现存报警").click_with_timing()


@allure.story("历史报警")
def test_workshop4_monitoring( login_goto_project,):
    page = navigate_to_solenoid_diagnosis_page1(login_goto_project)
    page.get_by_text("报警", exact=True).click()
    page.get_by_text("历史报警").click_with_timing()


@allure.story("开停工监测")
def test_workshop_monitoring(login_goto_project,):
    page = navigate_to_solenoid_diagnosis_page1(login_goto_project)
    page.get_by_text("开停工监测").click_with_timing()


@allure.story("冗余仪表偏差报警")
def test_workshop1_monitoring(login_goto_project,):
    page = navigate_to_solenoid_diagnosis_page1(login_goto_project)
    page.get_by_text("冗余仪表偏差报警").click_with_timing()


@allure.story("设备台账")
def test_workshop2_monitoring( login_goto_project,):
    page = navigate_to_solenoid_diagnosis_page1(login_goto_project)
    page.get_by_text("设备台账").click_with_timing()

def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.get_by_title("首页").click()








