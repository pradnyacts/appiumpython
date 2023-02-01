
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
ele_id=driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
ele_id.click()

"""
Part 1:
1. Create a Dictionary variable desired_caps = {} and assign appium desired capabilities to it, 
in the form of key value pair

Part 2:
Create the object for webdriver class, to access all the methods in Webdriver class and
pass the localhost and port number in the form of url to connect to appium server and "desired_caps" dictionary variable

"""