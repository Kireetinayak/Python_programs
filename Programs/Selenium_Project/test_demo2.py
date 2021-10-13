from  selenium import webdriver



driver = webdriver.Chrome(executable_path="C:/Users/UC267873/PycharmProjects/Programs/Selenium_Project/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_name("password").send_keys("secret_sauce")
driver.find_element_by_xpath("//input[@type='submit']").click()

print(driver.current_url)
print(driver.title)
frames = driver.find_elements_by_tag_name("frame")
print(frames)

try:
    for i in range(frames):
     print(i)
except:
    print("Not found frames")
item1 = driver.find_element_by_xpath("//a[@id='item_4_title_link']/div")
print(item1.text)
item1.click()
item1_value = driver.find_element_by_xpath("//div[@class='inventory_details_price']").text
print(item1_value)
link = driver.find_elements_by_tag_name("a")
for i in link:
    print(i.get_attribute("href"))

driver.close()

