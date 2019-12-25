from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def find_ele(self, loca, timeout=5, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loca))

    # 定位多个元素
    def find_eles(self, loca, timeout=5, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loca))

    # 点击
    def click_ele(self, loca, timeout=5, poll_frequency=1):
        self.find_ele(loca, timeout, poll_frequency).click()

    # 输入
    def send_ele(self, loca, text, timeout=5, poll_frequency=1):
        send_name = self.find_ele(loca, timeout, poll_frequency)
        send_name.click()
        send_name.send_keys(text)
