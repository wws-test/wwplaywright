# !/usr/bin/python3
# -*- coding: utf-8 -*-
from idlelib.debugger_r import frametable


from pages.ISDM.控制系统 import  *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入状态检测")
        login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        login_goto_project.page.get_by_text("仪控设备状态监测系统").click()
        login_goto_project.page.get_by_text("状态监测", exact=True).click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    return frame_locator


@allure.step("驾驶舱项目-控制系统-报警列表")
def test_set_management(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("控制系统").click()
    login_goto_project.page.get_by_text("报警列表").click()
    select_setting_management(frame_locator,login_goto_project.page)


@allure.step("驾驶舱项目-控制系统-预测性维护")
def test_predictive_maintenance(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("控制系统").click()
    login_goto_project.page.get_by_text("预测性维护").click()
    select_maintenance_management(frame_locator)


@allure.step("驾驶舱项目-阀门-报警列表")
def test_valve_alarm_list(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门").click()
    login_goto_project.page.get_by_text("报警列表").click()
    select_alarm_management(frame_locator)


@allure.step("驾驶舱项目-阀门-历史报警")
def test_valve_history_alarm(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门").click()
    login_goto_project.page.get_by_text("历史报警").click()
    select_history_alarm_management(frame_locator)


@allure.step("驾驶舱项目-阀门-调节阀预测")
def test_valve_adjust_predict(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门").click()
    login_goto_project.page.get_by_text("调节阀预测").click()
    select_adjust_management(frame_locator)


@allure.step("驾驶舱项目-阀门-阀门小开度监测")
def test_valve_small_opening_detection(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门").click()
    login_goto_project.page.get_by_text("阀门小开度监测").click()
    select_small_opening_management(frame_locator)


@allure.step("驾驶舱项目-现场仪表-智能仪表监测")
def test_smart_meter_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("现场仪表").click()
    login_goto_project.page.get_by_text("智能仪表监测").click()
    select_small_opening_detection_management(frame_locator)


@allure.step("驾驶舱项目-现场仪表-设备在线状态监测")
def test_device_online_status_monitoring(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("现场仪表").click()
    login_goto_project.page.get_by_text("设备在线状态监测").click()
    select_device_management(frame_locator,login_goto_project.page)


@allure.step("驾驶舱项目-计量仪表-报警列表")
def test_meter_alarm_list(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("计量仪表").click()
    login_goto_project.page.get_by_text("报警列表").click()
    device_online_status_management(frame_locator,login_goto_project.page)

@allure.step("驾驶舱项目-固定式报警器-报警列表")
def test_fixed_alarm_list(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("固定式报警器").click()
    login_goto_project.page.get_by_text("报警列表").click()
    fixed_alarm_management(frame_locator,login_goto_project.page)



@allure.step("驾驶舱项目-辅助检测-红外温度检测")
def test_red_alarm_management(pytestconfig,login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("辅助检测").click()
    login_goto_project.page.get_by_text("红外温度检测").click()






















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

