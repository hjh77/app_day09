from base.base import Base
from page.page_elements import PageElements


class PageAddress(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击第一个联系人
    def click_first_linkman(self):
        self.click_ele(PageElements.address)

    # 定位返回数据
    def results_text(self):
        results = self.find_eles(PageElements.linkman_name_result)
        return [i.text for i in results]
