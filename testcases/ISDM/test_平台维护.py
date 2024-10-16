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


@allure.step("全局配置")
def test_global_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("全局配置").click()
    notification_configuration(frame_locator,login_goto_project.page)



@allure.step("ECS-700机柜组态配置")
def test_ecs_700_cabinet_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("ECS-700组态配置").click()
    operate_cabinet(frame_locator,login_goto_project.page)




@allure.story("诊断项模板配置")
def test_diagnosis_item_template_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("诊断项模板配置").click()
    template_operations(frame_locator,login_goto_project.page)

@allure.story("设备字段配置")
def test_field_management(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("设备字段配置").click()
    set_field_configuration(frame_locator,login_goto_project.page,PageDownload)


@allure.story("设备型号配置")
def test_device_model_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("设备型号配置").click()
    Device_model_configuration(frame_locator,login_goto_project.page)


@allure.story("机柜间配置")
def test_cabinets_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("机柜间配置").click()
    cabinet_room_operations(frame_locator,login_goto_project.page)



@allure.story("通道配置")
def test_channel_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("通道配置").click()
    smart_bind_operation(frame_locator,login_goto_project.page)


@allure.story("机柜配置")
def test_cabinet_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("机柜配置").click()
    cabinet_operations(frame_locator,login_goto_project.page)



@allure.story("设备组配置")
def test_device_group_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("设备组配置").click()
    operate_device_ledger(frame_locator,login_goto_project.page)


@allure.story("控制系统配置")
def test_control_system_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("控制系统配置").click()
    control_system_operations(frame_locator,login_goto_project.page)




@allure.story("阀门报警配置")
def test_valve_alarm_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门报警配置").click()
    valve_alarm_configuration(frame_locator,login_goto_project.page)


@allure.story("开停工配置")
def test_start_stop_configuration(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("开停工配置").click()
    selectstart_stop_configuration(frame_locator,login_goto_project.page)



@allure.story("报警通知过滤")
def test_alarm_notification_filtering(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("报警通知过滤").click()
    alarm_notification_filtering(frame_locator,login_goto_project.page)

@allure.story("报警过滤")
def test_alarm_filtering(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("报警过滤").click()
    alarm_filtering(frame_locator,login_goto_project.page)


@allure.story("报警拦截器")
def test_alarm_interceptor(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("报警拦截器").click()
    Alarm_blocker(frame_locator,login_goto_project.page)


@allure.story("消息触发器")
def test_message_trigger(pytestconfig, login_goto_project,):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("消息触发器").click()
    message_trigger_p(frame_locator,login_goto_project.page)
    message_trigger_report_operations(frame_locator,login_goto_project.page)
    Message_trigger_start_shutdown(frame_locator,login_goto_project.page)


@allure.story("设备组任务")
def test_device_group_task(pytestconfig, login_goto_project):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("设备组任务").click()
    Device_GroupTask(frame_locator,login_goto_project.page)

@allure.story("阀门小开度配置")
def test_valve_small_opening_configuration(pytestconfig, login_goto_project,PageDownload):
    frame_locator = navigate_to_solenoid_diagnosis_page(login_goto_project)
    login_goto_project.page.get_by_text("阀门小开度配置").click()
    Valve_opening_configuration(frame_locator,login_goto_project.page,PageDownload)



def test_teardown_module(login_goto_project):
    logger.info("fresh_page fixture ending....")
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()















