import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#part 1: Desired capabilities
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

#part 3: action on the app
#1 .By using xpath and content-desc
ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')
ele_xpath.click()
time.sleep(2)
#2. By using xpath and resource id
#ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')

#. By using xpath and text and value
#ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]')

#. By using xpath and index
#ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]')

#. By using xpath and class name
ele_xpath2=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys("testappium")


time.sleep(2)
driver.quit()