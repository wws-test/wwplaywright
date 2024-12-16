
def select_option_in_iframe(iframe, selector, option_text):
    try:

        # 确保下拉框是可见且可以交互的
        dropdown = iframe.locator(selector)
        dropdown.wait_for(state='visible')
        dropdown.click()

        # 等待选项出现，并点击特定文本的选项
        option = iframe.get_by_text(option_text)
        option.wait_for(state='visible')
        option.click()

        print(f"成功选择了选项: {option_text}")
    except Exception as e:
        print(f"选择选项时出错: {e}")