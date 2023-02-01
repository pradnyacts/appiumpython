from appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

saucelab_username="oauth-pradnyawhatsapp-2034b"
saucelab_accesskey="3a421996-7481-4900-8c4f-3999ae8580a4"

# caps = {}
# caps['appiumVersion'] = "1.17.1"
# caps['deviceName'] = "Google Pixel 3a XL GoogleAPI Emulator"
# caps['deviceOrientation'] = "portrait"
# caps['platformVersion'] = "10.0"
# caps['platformName'] = "Android"
# caps['app'] = "storage:filename=Android_Demo_App.apk"
# caps['name']="Android Test"
# caps['build']="Version 1.1"
# caps['tags']=['v3','v4']
# caps['username']=saucelab_username
# caps['accesskey']=saucelab_accesskey
from datetime import datetime
caps = {}
caps['platformName'] = 'Android'
caps['appium:app'] = 'storage:filename=Android_Demo_App.apk' # The filename of the mobile app
caps['appium:deviceName'] = 'Google Pixel 3a XL GoogleAPI Emulator'
caps['appium:platformVersion'] = '10.0'
caps['appium:automationName'] = 'UiAutomator2'
caps['sauce:options'] = {}
caps['sauce:options']['appiumVersion'] = '1.17.1'
caps['sauce:options']['build'] = 'v1.1'
caps['sauce:options']['name'] = 'android test'

url = "https://oauth-pradnyawhatsapp-2034b:3a421996-7481-4900-8c4f-3999ae8580a4@ondemand.us-west-1.saucelabs.com:443/wd/hub"


#url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"

driver =webdriver.Remote(url,caps,keep_alive=True)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])


ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue"))
ele.click()

time.sleep(4)
driver.quit()