# !/usr/bin/python3
# -*- coding: utf-8 -*-
from idlelib.debugger_r import frametable

import allure
import pytest

from pages.ISDM.驾驶舱地图 import *


def navigate_to_solenoid_diagnosis_page(page: PageWrapper):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入智能驾驶舱")
        page.switch_to_main_frame()
        page.get_by_title("首页").click()
        page.get_by_text("仪控设备状态监测系统").click()
        page.locator("#menu").get_by_text("总貌地图").click()
    return page


@allure.story("驾驶舱项目点击")
def test_set_management( login_goto_project, ):
    page = navigate_to_solenoid_diagnosis_page(login_goto_project)
    page.switch_to_frame("iframe[name=\"supos-tab-framework-1\"]")
    select_setting_management_p(login_goto_project)



def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.get_by_title("首页").click()
