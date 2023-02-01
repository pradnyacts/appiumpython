from selenium import webdriver

import SeleniumFrameworkcloud.Utilities.CustonLogger as cl
import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)


class WebDriverClass:
    log = cl.customLogger()
    sauce_username = "oauth-pradnyawhatsapp-2034b"
    sauce_access_key = "3a421996-7481-4900-8c4f-3999ae8580a4"

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)
            self.log.info("Chrome Driver is initializing")
        # elif browserName == "safari":
        #     driver = webdriver.Safari()
        #     self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver")
            self.log.info("FireFox Driver is initializing")

        return driver

    def cloudDriver(self,pname,bName,bVersion):
        SauceOptions = {
            'name': 'Dummy Point Test in Mac',
            'build': 'Dummypoint Regression Test',
            'screenResolution': '1024x768',
            'username': self.sauce_username,
            'accessKey': self.sauce_access_key,
            # tags to filter test reporting.
            'tags': ['instant-sauce', 'pytest', 'module4'],
        }

        capabilities = {
            'browserName': bName,
            'browserVersion': bVersion,
            'platformName': pname,
            'sauce:options': SauceOptions

        }
        url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
        driver = webdriver.Remote(command_executor=url, desired_capabilities=capabilities, keep_alive=True)
        return driver
