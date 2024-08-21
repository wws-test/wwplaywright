# !/usr/bin/python3
# -*- coding: utf-8 -*-
from idlelib.debugger_r import frametable

import allure
import pytest

from pages.电池阀 import  *





@allure.feature("电磁阀在线诊断")
@allure.step("电磁阀在线诊断-设置算法")
def test_set_algorithm(pytestconfig, login_goto_project):
    login_goto_project.page.locator("span[title='电磁阀诊断']").click()
    login_goto_project.page.locator("span[title='电磁阀在线诊断']").click()
    with allure.step("进入frame"):
        frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    with allure.step("点击饼图"):
        frame_locator.locator("canvas").click()
    with allure.step("点击设置表头"):
        select_table_header(frame_locator)
        unselect_table_header(frame_locator)
    with allure.step("设置算法"):
        select_setting_management(frame_locator)
        select_algorithm_setting(frame_locator)
        select_important_setting(frame_locator)




@pytest.mark.parametrize("algorithm_name", ["乙烯装置", "06XSOV_11001_5", "机器学习分类算法", "正常"])
@allure.step("电磁阀在线诊断-查询导出")
def test_set_management(pytestconfig, login_goto_project, algorithm_name):
    login_goto_project.page.locator("span[title='电磁阀诊断']").click()
    login_goto_project.page.locator("span[title='电磁阀在线诊断']").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    solenoid_search(frame_locator,algorithm_name)
    download_report(frame_locator,login_goto_project.page)


@allure.step("电磁阀在线诊断-详情页面")
def test_detail_page(pytestconfig, login_goto_project):
    login_goto_project.page.locator("span[title='电磁阀诊断']").click()
    login_goto_project.page.locator("span[title='电磁阀在线诊断']").click()
    frame_locator = login_goto_project.page.frame_locator("iframe[name=\"supos-tab-framework-1\"]")
    with allure.step("点击第二个详情"):
        logger.info("点击详情")
        frame_locator.locator("(//a[@class='model-pages-solenoid-components-solenoid-table-index-linkStyle'])[2]").click()
















# def test_login_success(page, pytestconfig):
#     if base_url := pytestconfig.getoption("base_url"):
#         logger.info(f"命令行传入参数，base_url={base_url}")
#     else:
#         default_url = "http://10.30.76.150:8080"
#         base_url = default_url
#         login_page = LoginPage(page, base_url=base_url)
#         login_page.login("wwtest", "Supcon@1209")

