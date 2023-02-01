from appium import webdriver
class Driver:

    def getDriverMethod(self):
        # part 1: Desired capabilities
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = ('C:/Users/pradn/OneDrive/Documents/app/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        # part 2: "Webdriver object"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

