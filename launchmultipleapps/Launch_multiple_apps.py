import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('C:/Users/pradn/OneDrive/Documents/app/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

#part 2: "Webdriver object"
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(5)
driver.start_activity("com.android.vending","com.android.vending.AssetBrowserActivity")
time.sleep(5)
driver.start_activity("com.code2lead.kwad","com.code2lead.kwad.MainActivity")
driver.quit()
