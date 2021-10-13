import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
def init_Chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    print("---------------Set up--------------------")
    yield

    ch_driver.close()

@pytest.fixture(scope="class")
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    print("---------------Set up--------------------")
    yield
    ff_driver.close()

@pytest.mark.usefixtures("init_Chrome_driver")
class base_ch_test:
    pass

class Test_ch_test(base_ch_test):

    def test_ch_google_test(self):
        self.driver.get("http://www.google.com")
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.google.com")
        assert self.driver.title =="Google"

@pytest.mark.usefixtures("init_ff_driver")
class base_ff_test:
    pass

class Test_ff_test(base_ff_test):

    def test_ff_google_test(self):
        self.driver.get("http://www.google.com")
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.google.com")
        assert self.driver.title =="Google"
