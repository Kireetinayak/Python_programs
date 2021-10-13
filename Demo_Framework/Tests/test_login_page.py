import pytest

from Config.config import Test_data
from Pages.login_page import Login_Page
from Tests.test_base import Base_test


class Test_Login(Base_test):

    def test_loginpage_title(self):
        self.loginpage=Login_Page(self.driver)
        title=Login_Page.get_loginpage_title(Test_data.LOGIN_PAGE_TITLE)
        assert title== Test_data.LOGIN_PAGE_TITLE


    def test_loginPage_url(self):
        self.loginpage=Login_Page(self.driver)
        url=Login_Page.get_page_url()
        print(url)

    def test_get_login(self):
        self.loginpage=Login_Page(self.driver)
        Login_Page.login_page()


