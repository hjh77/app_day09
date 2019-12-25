from base.base import Base
from page.page_elements import PageElements


class PageEdit(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击编辑
    def click_address_linkman(self):
        self.click_ele(PageElements.edit)
