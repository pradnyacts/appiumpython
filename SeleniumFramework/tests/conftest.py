import pytest
from SeleniumFramework.Base.BasePage import BaseClass
from SeleniumFramework.Base.DriverClass import WebDriverClass
import time

#rename to run local as DriverClasscloud.py
@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()

    driver = driver1.getWebDriver("chrome")
    #driver=driver1.cloudDriver()
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
