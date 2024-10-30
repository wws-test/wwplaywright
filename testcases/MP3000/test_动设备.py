import allure

from pages.MP3000.动设备 import *

def navigate_to_solenoid_diagnosis_page(login_goto_project):
    with allure.step("导航到动设备页面"):
        logger.info("进入监测与预警")
        login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
        login_goto_project.page.get_by_text("动设备振动监测与预警").click()
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")

    return frame_locator


@allure.step("动设备在线监测")
def test_set_management(pytestconfig, login_goto_project,):
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
    login_goto_project.page.get_by_text("动设备振动监测与预警").click()
    login_goto_project.page.locator("#menu").get_by_text("动设备在线监测").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    select_device_ledger(frame_locator,login_goto_project.page)

@allure.step("动设备报警组态配置")
def test_Online_monitoring_equipment(pytestconfig, login_goto_project,):
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
    login_goto_project.page.get_by_text("动设备振动监测与预警").click()
    login_goto_project.page.locator("#menu").get_by_text("动设备报警组态配置").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    configuration_configuration(frame_locator,login_goto_project.page)

@allure.step("动设备机泵诊断")
def test_Dynamic_equipment(pytestconfig, login_goto_project,):
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
    login_goto_project.page.get_by_text("动设备机泵诊断").click()
    login_goto_project.page.locator("#menu").get_by_text("机泵在线监测").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    perform_query(frame_locator,login_goto_project.page)

@allure.step("动设备机泵诊断")
def test_Dynamic_equipment1(pytestconfig, login_goto_project,):
    login_goto_project.page.locator("//div[@id='root']/div[1]/section[1]/header[1]/div[1]/div[1]").click()
    login_goto_project.page.get_by_text("动设备机组诊断").click()
    login_goto_project.page.locator("#menu").get_by_text("机组在线监测").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    perform_query(frame_locator,login_goto_project.page)