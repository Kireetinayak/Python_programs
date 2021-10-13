from selenium import webdriver
import pytest
import time
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

driver = None
@pytest.fixture(scope="module")
def init_method():
    global driver
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    yield
    driver.close()

@pytest.mark.usefixtures("init_method")
def test_App_title():
    assert driver.title == "Swag Labs"

@pytest.mark.usefixtures("init_method")
def test_App_URl(init_method):
    print(driver.current_url)
