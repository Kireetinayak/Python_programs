import pytest
from  selenium import webdriver

driver = webdriver


def test_Setup(self):
    self.driver.Chrome(executable_path="C:/Users/UC267873/PycharmProjects/Programs/Selenium_Project/chromedriver.exe")
    self.driver.maximize_window()

    self.driver.get("https://www.saucedemo.com/")
    self.driver.find_element_by_id("user-name").send_keys("standard_user")
    self.driver.find_element_by_name("password").send_keys("secret_sauce")
    self.driver.find_element_by_xpath("//input[@type='submit']").click()

    print(self.driver.current_url)
    print(self.driver.title)

    item1 = self.driver.find_element_by_xpath("//a[@id='item_4_title_link']/div")
    print(item1.text)
    item1.click()
    item1_value = self.driver.find_element_by_xpath("//div[@class='inventory_details_price']").text
    print(item1_value)
    self.driver.close()
