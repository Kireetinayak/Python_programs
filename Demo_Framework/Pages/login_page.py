from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Base_Page import Base_Page
from Config.config import Test_data

class Login_Page(Base_Page):
    # locators
    USER_NAME_textfileld=(By.ID,"user-name")
    PASSWORD_textfield=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"login-button")
    #SING_UP_LINK=

    """Constructor of the page"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(Test_data.BASE_URL)

    """ Page Methods """
    def get_loginpage_title(self,title):
        return self.get_title(title)

    def get_page_url(self,url):
        return self.current_url(url)

    def login_page(self,username,password):
        self.do_send_keys(self.USER_NAME_textfileld,username)
        self.do_send_keys(self.PASSWORD_textfield,password)
        self.do_click(self.LOGIN_BUTTON)

