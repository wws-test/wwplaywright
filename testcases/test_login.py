# !/usr/bin/python3
# -*- coding: utf-8 -*-
import allure


from pages.电池阀 import  select_setting_management, select_algorithm_setting





@allure.feature("电磁阀在线诊断")
@allure.step("电磁阀在线诊断-设置算法")
def test_login(pytestconfig, login_goto_project):
    login_goto_project.page.locator("span[title='电磁阀诊断']").click()
    login_goto_project.page.locator("span[title='电磁阀在线诊断']").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    select_setting_management(frame_locator)
    select_algorithm_setting(frame_locator)


# def test_login_success(page, pytestconfig):
#     if base_url := pytestconfig.getoption("base_url"):
#         logger.info(f"命令行传入参数，base_url={base_url}")
#     else:
#         default_url = "http://10.30.76.150:8080"
#         base_url = default_url
#         login_page = LoginPage(page, base_url=base_url)
#         login_page.login("wwtest", "Supcon@1209")