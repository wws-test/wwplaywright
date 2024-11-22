# !/usr/bin/python3
# -*- coding: utf-8 -*-
import allure

from pages.ISDM.平台维护 import  *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    with allure.step("导航到仪控设备状态检查系统页面"):
        logger.info("进入维护功能")
        login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        login_goto_project.page.get_by_text("仪控设备状态监测系统").click()
        login_goto_project.page.locator("#menu").get_by_text("平台维护").click()
        login_goto_project.page.locator("#menu").get_by_text("系统组态").click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")

    return frame_locator



@allure.step("位号管理")
def test_set_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("位号配置").nth(1).click()
    bit_number_configuration(frame_locator,login_goto_project.page,PageDownload)


@allure.step("数据源管理")
def test_instrument_management(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("数据源管理").click()
    set_data_source(frame_locator,login_goto_project.page)

@allure.step("用户分组权限")
def test_instrument_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("用户分组权限").click()
    add_user_group(frame_locator,login_goto_project.page,PageDownload)


@allure.step("AE策略")
def test_ae_strategy(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("AE策略").click()
    add_strategy(frame_locator,login_goto_project.page)

@allure.step("报警抑制")
def test_alarm_suppress(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("报警抑制").click()
    add_alarm_suppress(frame_locator,login_goto_project.page)

@allure.step("位号类别")
def test_bit_category(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("位号配置").click()
    login_goto_project.page.get_by_text("位号类别").click()
    add_bit_category(frame_locator,login_goto_project.page)


@allure.step("IDM诊断项配置")
def test_idm_diagnosis_item_configuration(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("IDM配置").click()
    login_goto_project.page.get_by_text("IDM诊断项配置").click()
    add_idm_diagnosis_item_configuration(frame_locator,login_goto_project.page)
@allure.step("IDM同步数据")
def test_idm_synchronization_data(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("IDM配置").click()
    login_goto_project.page.get_by_text("IDM数据同步").click()

@allure.step("IDM绑定")
def test_idm_binding(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("IDM配置").click()
    login_goto_project.page.get_by_text("IDM绑定").click()
    add_idm_binding(frame_locator,login_goto_project.page)

@allure.step("报警字典")
def test_alarm_configuration(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("统计配置").click()
    login_goto_project.page.get_by_text("报警字典").click()
    add_alarm_configuration(frame_locator,login_goto_project.page ,PageDownload)



@allure.step("自控回路模式")
def test_self_control_circuit_mode(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("自控率配置").click()
    login_goto_project.page.get_by_text("自控回路模式").click()
    add_self_control_circuit_mode(frame_locator,login_goto_project.page)


@allure.step("自控回路剔除")
def test_self_control_circuit_exclusion(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("自控率配置").click()
    login_goto_project.page.get_by_text("自控回路剔除").click()
    add_self_control_circuit_exclusion(frame_locator,login_goto_project.page, PageDownload)


@allure.step("自控回路管理")
def test_self_control_circuit_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("自控率配置").click()
    login_goto_project.page.get_by_text("自控回路管理").click()
    add_self_control_circuit_management(frame_locator,login_goto_project.page,PageDownload)

@allure.step("联锁回路模式")
def test_lock_circuit_mode(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("联锁投用率配置").click()
    login_goto_project.page.get_by_text("联锁回路模式").click()
    add_self_control_circuit_mode(frame_locator,login_goto_project.page)


@allure.step("联锁回路剔除")
def test_lock_circuit_exclusion(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("联锁投用率配置").click()
    login_goto_project.page.get_by_text("联锁回路剔除").click()
    add_self_control1_circuit_exclusion(frame_locator,login_goto_project.page, PageDownload)


@allure.step("冗余联锁管理")
def test_redundancy_lock_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("联锁投用率配置").click()
    login_goto_project.page.get_by_text("冗余联锁管理").click()
    add_redundancy_lock_management(frame_locator,login_goto_project.page,PageDownload)



@allure.step("冗余联锁设备剔除")
def test_redundancy_lock_device_exclusion(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("联锁投用率配置").click()
    login_goto_project.page.get_by_text("冗余联锁设备剔除").click()
    add_self_control2_circuit_exclusion(frame_locator,login_goto_project.page,PageDownload)



@allure.step("联锁回路管理")
def test_lock_circuit_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.locator("#menu").get_by_text("联锁投用率配置").click()
    login_goto_project.page.get_by_text("联锁回路管理").click()
    add_lock_circuit_management(frame_locator,login_goto_project.page,PageDownload)


















def test_idm_data_source_configuration(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)










def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()















