from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

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

element = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Is Displayed : ", element.is_displayed())
print("Is Enabled : ", element.is_enabled())
print("Is selected : ", element.is_selected())
print("Size : ", element.size)
print("Location : ", element.location)
