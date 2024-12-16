# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pages.ISDM.管理功能 import  *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入管理功能")
        login_goto_project.page.get_by_title("首页").click()
        login_goto_project.page.get_by_text("仪控设备状态监测系统").click()
        login_goto_project.page.locator("#menu").get_by_text("管理功能").click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    return frame_locator

@allure.step("知识库-知识标签")
def test_set_management(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("知识库").click()
    login_goto_project.page.get_by_text("知识标签").click()
    select_setting_management(frame_locator,login_goto_project.page)

@allure.step("知识库-知识库")
def test_knowledge_classification(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("知识库").click()
    login_goto_project.page.get_by_text("知识库").nth(2).click()
    select_knowledge_classification(frame_locator,login_goto_project.page)

@allure.step("开停工监测")
def test_workshop_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("开停工监测").click()
    with login_goto_project.page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")


@allure.step("冗余仪表偏差报警")
def test_workshop1_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("冗余仪表偏差报警").click()
    frame_locator.get_by_role("button", name="search 搜索").click()
    frame_locator.get_by_role("button", name="clear 重置").click()
    with login_goto_project.page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
        download = download_info.value
        logger.info(f"下载诊断报告{download.suggested_filename}")
    frame_locator.get_by_text("历史报警").click()
    with login_goto_project.page.expect_download() as download_info:
        frame_locator.get_by_role("button", name="download 导出").click()
    download = download_info.value
    logger.info(f"下载诊断报告{download.suggested_filename}")


@allure.step("设备台账")
def test_workshop2_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("设备台账").click()
    select_device_ledger(frame_locator,login_goto_project.page)



@allure.step("现存报警")
def test_workshop3_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("报警", exact=True).click()
    login_goto_project.page.get_by_text("现存报警").click()
    select_existing_alarm(frame_locator,login_goto_project.page)

@allure.step("历史报警")
def test_workshop4_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("报警", exact=True).click()
    login_goto_project.page.get_by_text("历史报警").click()
    select_his_alarm(frame_locator,login_goto_project.page)



@allure.step("联锁投用率")
def test_workshop5_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("联锁投用率").click()
    select_duo_branch(frame_locator,login_goto_project.page)


@allure.step("设备报警KPI")
def test_workshop6_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("设备报警KPI").click()
    select_device_alarm_kpi(frame_locator,login_goto_project.page)


@allure.step("厂商KPI")
def test_workshop7_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("厂商KPI").click()
    select_control_system_kpi(frame_locator)

@allure.step("装置KPI")
def test_workshop8_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("装置KPI").click()
    select_device_kpi(frame_locator)



@allure.step("智能仪表台账统计")
def test_workshop9_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("智能仪表台账统计").click()
    select_smart_meter_statistics(frame_locator,login_goto_project.page)



@allure.step("数字化巡检")
def test_workshop10_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("KPI", exact=True).click()
    login_goto_project.page.get_by_text("数字化巡检").click()
    select_digital_inspection(frame_locator,login_goto_project.page)



@allure.step("周月报表")
def test_workshop11_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("周月报表").click()
    select_weekly_monthly_report(frame_locator,login_goto_project.page)

def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.page.get_by_title("首页").click()














# def test_login_success(page, pytestconfig):
#     if base_url := pytestconfig.getoption("base_url"):
#         logger.info(f"命令行传入参数，base_url={base_url}")
#     else:
#         default_url = "http://10.30.76.150:8080"
#         base_url = default_url
#         login_page = LoginPage(page, base_url=base_url)
#         login_page.login("wwtest", "Supcon@1209")

