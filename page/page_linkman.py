from base.base import Base
from page.page_elements import PageElements


class PageLinkman(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 输入name
    def send_linkman_name(self, text):
        self.send_ele(PageElements.input_name, text)

    # 点击返回
    def go_back_linkman(self):
        self.click_ele(PageElements.back_linkman)
