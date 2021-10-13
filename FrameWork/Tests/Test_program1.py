from selenium import webdriver
def teste2e2():
    driver=webdriver.Chrome(executable_path="C:\\Users\\UC267873\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    print("Tittle is ",driver.title)
    driver.quit()