import re

import pytest

from log import logger


@pytest.fixture(scope="class", autouse=True)
def fresh_page(page):
    print("fresh_page fixture starting....")
    yield
    logger.info("fresh_page fixture ending....")
    page.locator("div").filter(has_text=re.compile(r"^默认公司$")).locator("div").first.click()