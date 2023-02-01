from selenium import webdriver

import SeleniumFramework.Utilities.CustonLogger as cl
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

    def cloudDriver(self):
        SauceOptions = {
            'name': 'Dummy Point Test FrameWork',
            'build': 'Version 1',
            'screenResolution': '1280x768',
            'username': self.sauce_username,
            'accessKey': self.sauce_access_key,
            # tags to filter test reporting.
            'tags': ['Framework', 'pytest', 'module4'],
        }

        capabilities = {
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'platformName': 'macOS 10.15',
            'sauce:options': SauceOptions
        }
