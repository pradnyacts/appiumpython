from appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

from datetime import datetime
caps = {}
caps['appiumVersion'] = '1.17.1'
caps['appium:deviceName'] = 'Google Pixel 3a XL GoogleAPI Emulator'
caps['platformName'] = 'Android'
caps['appium:platformVersion'] = '10.0'
caps['appium:app'] = 'storage:filename=Android_Demo_App.apk' # The filename of the mobile app

url = "https://oauth-pradnyawhatsapp-2034b:3a421996-7481-4900-8c4f-3999ae8580a4@ondemand.us-west-1.saucelabs.com:443/wd/hub"

driver=webdriver.Remote(url,caps,keep_alive=True)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue"))
ele.click()

time.sleep(4)
driver.quit()