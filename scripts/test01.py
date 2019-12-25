import os

import pytest, sys

sys.path.append(os.getcwd())
from base.page_in import PageIn

from base.getDriver import get_driver


class TestCase:
    def setup_class(self):
        self.driver = get_driver("Android", "5.1", "com.android.contacts", ".activities.PeopleActivity")
        self.page = PageIn(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def click_num1(self):
        self.page.page_add().click_first_linkman()

    @pytest.mark.parametrize("text", ["aaaa", "bbbb", "cccc"])
    def test01(self, text):
        self.page.page_edit().click_address_linkman()
        self.page.page_link().send_linkman_name(text)
        self.page.page_link().go_back_linkman()
        assert text in self.page.page_add().results_text()
