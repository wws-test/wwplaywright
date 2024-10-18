import re

import allure

from common.assertion import assert_element_exists
from log import logger
from playwright.sync_api import Page, expect


@allure.step("通知配置")
def select_device_ledger(iframe: Page, page: Page):
    iframe.locator("div").filter(has_text=re.compile(r"^健康\(.*\)$")).click()
    iframe.locator("div").filter(has_text=re.compile(r"^报警\(.*\)$")).click()
    iframe.locator("div").filter(has_text=re.compile(r"^警告\(.*\)$")).click()
    iframe.locator("div").filter(has_text=re.compile(r"^危险\(.*\)$")).click()
    iframe.locator("div").filter(has_text=re.compile(r"^关注\(.*\)$")).click()
    iframe.locator("#rc_select_1").click()
    iframe.get_by_text("大机组").click()
    iframe.locator("#rc_select_2").click()
    iframe.get_by_title("J").locator("div").click()

@allure.step("组态配置")
def configuration_configuration(iframe: Page, page: Page):
    iframe.get_by_role("button", name="查 询").click()
    iframe.get_by_role("button", name="重 置").click()
    iframe.locator("a").click()
    iframe.get_by_text("启用").click()
    iframe.get_by_role("button", name="redo 刷新").click()
    iframe.get_by_role("button", name="查 询").click()
    iframe.get_by_role("button", name="重 置").click()
    iframe.get_by_role("tab", name="门限配置").click()
    iframe.get_by_role("button", name="展开 down").click()
    iframe.get_by_role("button", name="查 询").click()
    iframe.get_by_role("button", name="重 置").click()
    iframe.get_by_role("button", name="redo 刷新").click()
    iframe.get_by_role("button", name="delete 删除").click()
    iframe.get_by_role("button", name="plus 新增").click()
    new_frame = iframe.get_by_label("新增")
    new_frame.get_by_role("button", name="查 询").click()
    new_frame.get_by_role("button", name="重 置").click()
    iframe.get_by_role("button", name="取 消").click()
    iframe.get_by_role("button", name="复制到").click()


@allure.step("执行查询操作")
def perform_query(frame,page):
    frame.get_by_placeholder("支持按设备名称、故障部位、诊断结论的模糊查询").click()
    frame.get_by_placeholder("支持按设备名称、故障部位、诊断结论的模糊查询").fill("2222")
    frame.get_by_role("button", name="search").click()
    frame.get_by_role("button", name="close-circle").click()
    frame.get_by_role("button", name="search").click()
    frame.get_by_role("button", name="search").dblclick()