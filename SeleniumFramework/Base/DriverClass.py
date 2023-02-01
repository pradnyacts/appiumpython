from selenium import webdriver

import SeleniumFramework.Utilities.CustonLogger as cl
import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
class WebDriverClass:
    log = cl.customLogger()

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
