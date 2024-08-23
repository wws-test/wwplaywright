from playwright.sync_api import Page, expect



def assert_element_exists(selector):

    expect(selector).to_be_visible()

def assert_element_not_exists( selector):

    expect(selector).to_be_hidden()

def assert_element_text( selector: str, text: str):

    expect(selector).to_have_text(text)

def assert_element_contains_text( selector: str, text: str):
    expect(selector).to_contain_text(text)

def assert_element_attribute( selector, attribute: str, value: str):

    expect(selector).to_have_attribute(attribute, value)

def assert_element_value(selector, value):

    expect(selector).to_have_value(value)




# 示例使用
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto('https://example.com')

#     assertions = PlaywrightAssertions(page)
#     assertions.assert_element_exists('h1')
#     assertions.assert_element_text('h1', 'Example Domain')
#     assertions.assert_url('https://example.com')

#     browser.close()