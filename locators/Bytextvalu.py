
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
# ele_text=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ENTER SOME VALUE")')
# ele_text.click()
ele_text=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ENTER SOME VALUE")')
ele_text.click()



