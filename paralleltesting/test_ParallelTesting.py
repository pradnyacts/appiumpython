
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

#part 1: Desired capabilities
def deviceDriver(deviceID,sysport):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'Pixel'
    desired_caps['udid'] = deviceID
    desired_caps['systemPort'] = sysport
    desired_caps['app'] = ('C:/Users/pradn/OneDrive/Documents/app/Android_Demo_App.apk')
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    #part 2: "Webdriver object"
    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    return driver
def enterText(driver):
    #part 3: action on the app
    ele_id=driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    time.sleep(2)
    ele_clasname=driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText").send_keys("Testappium")
    driver.quit()

def test_deviceTest():
    d1=deviceDriver("emulator-5554",8200)
    d2 = deviceDriver("emulator-5556", 8201)
    enterText(d1)
    enterText(d2)





