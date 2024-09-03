# !/usr/bin/python3
# -*- coding: utf-8 -*-
from idlelib.debugger_r import frametable


from pages.设备门户 import   *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    """导航到电磁阀在线诊断页面，并返回框架定位符"""
    with allure.step("导航到变送器诊断页面"):
        login_goto_project.page.get_by_text("设备门户").click()
        login_goto_project.page.get_by_text("授权管理").click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
        frame_locator.get_by_text("授权管理").click() # 点击返回按钮

    return frame_locator

@allure.step("变送器在线诊断-查询导出")
def test_set_management(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    device_portal_operation(frame_locator,login_goto_project.page)



def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()














# def test_login_success(page, pytestconfig):
#     if base_url := pytestconfig.getoption("base_url"):
#         logger.info(f"命令行传入参数，base_url={base_url}")
#     else:
#         default_url = "http://10.30.76.150:8080"
#         base_url = default_url
#         login_page = LoginPage(page, base_url=base_url)
#         login_page.login("wwtest", "Supcon@1209")

