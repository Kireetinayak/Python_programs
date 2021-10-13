import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\\Users\\UC267873\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()