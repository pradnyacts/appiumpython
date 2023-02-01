import pytest
from SeleniumFrameworkcloud.Base.BasePage import BaseClass
from SeleniumFrameworkcloud.Base.DriverClass import WebDriverClass
import time
import SeleniumFrameworkcloud.Configurationfiles.DeviceConfig as dc

#rename to run local as DriverClasscloud.py
@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()

    #driver = driver1.getWebDriver("chrome")
    driver=driver1.cloudDriver(dc.platformName,dc.bName,dc.bVersion)
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
