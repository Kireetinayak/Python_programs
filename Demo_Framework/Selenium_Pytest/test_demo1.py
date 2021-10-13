import time
from selenium import webdriver
import  pytest

from selenium import webdriver
#from webdriver.manager.chrome import ChromeDriverManager
def test_weblogin():
    driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    assert driver.title == "Swag Labs"
    time.sleep(2)
    driver.close()

def test_weblogin2():
    driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
    driver.get('https://www.google.com/')
    driver.implicitly_wait(10)
    assert driver.title == "Google"
    time.sleep(2)
    driver.close()

def test_weblogin3():
    driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(10)
    assert driver.title == "'Facebook - ಲ...ಅಥವಾ ಸೈನ್ ಅಪ್"
    time.sleep(2)
    driver.close()