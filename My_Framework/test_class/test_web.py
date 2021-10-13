
import  pytest
from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Ie(IEDriverManager().install())
   # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    assert driver.title== "Google"
    driver.close()

def test_facebook():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    assert  driver.title=="facebook"
    driver.close()

def test_insta():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    assert driver.title=="Instagram"
    driver.close()

def test_99():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.99acres.com/")
    driver.maximize_window()
    assert driver.title=="99acres.com"
    driver.close()