import pytest
from selenium import webdriver

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")

class Base_class:
    pass

class Test_Hub(Base_class):
    @pytest.mark.parametrize("username, password",
        [("standard_user","secret_sauce"),
             ("locked_out_user","secret_sauce"),
             ("problem_user","secret_sauce")])

    def test_login(self, username,password):
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)