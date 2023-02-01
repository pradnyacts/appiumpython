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

#part 3: action on the app :find_elements   :multiple elements

ele=driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
for x in ele:
    print(x.text)
for x in ele:
    button=x.text
    if button=="ScrollView":
        x.click()
        break
time.sleep(2)
driver.quit()



