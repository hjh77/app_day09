from page.page_address import PageAddress
from page.page_edit import PageEdit
from page.page_linkman import PageLinkman


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    def page_add(self):
        return PageAddress(self.driver)

    def page_edit(self):
        return PageEdit(self.driver)

    def page_link(self):
        return PageLinkman(self.driver)
