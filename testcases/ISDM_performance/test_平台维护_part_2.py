# !/usr/bin/python3
# -*- coding: utf-8 -*-
import allure

from pages.ISDM.平台维护 import *


def navigate_to_solenoid_diagnosis_page(page: PageWrapper):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入维护功能")
        page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        page.get_by_text("仪控设备状态监测系统").click()
        page.locator("#menu").get_by_text("平台维护").click()
        page.locator("#menu").get_by_text("系统组态").click()
    return page


@allure.story("位号管理")
def test_set_management(login_goto_project):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.locator("#menu").get_by_text("位号配置").click()
    page.get_by_text("位号配置").nth(1).click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    bit_number_configuration_p(page)


@allure.story("数据源管理")
def test_datamanager_management(login_goto_project):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.locator("#menu").get_by_text("位号配置").click()
    page.get_by_text("数据源管理").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    set_data_source_p(page)


@allure.story("UA诊断项配置")
def test_idm_diagnosis_item_configuration(login_goto_project):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.locator("#menu").get_by_text("IDM配置").click()
    page.get_by_text("UA诊断项配置").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    add_idm_diagnosis_item_configuration_p(page)


@allure.story("联锁回路管理")
def test_self_control_circuit_management(login_goto_project):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.locator("#menu").get_by_text("联锁投用率配置").click()
    page.get_by_text("联锁回路管理").click()
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    add_self_control_circuit_management_p(page)


def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
