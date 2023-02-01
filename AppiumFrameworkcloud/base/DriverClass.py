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
    def getcloudDriver(self,pVersion,pName):
        caps = {}
        caps['platformName'] = pName
        caps['appium:app'] = 'storage:filename=Android_Demo_App.apk'  # The filename of the mobile app
        caps['appium:deviceName'] = 'Google Pixel 3a XL GoogleAPI Emulator'
        caps['appium:platformVersion'] = pVersion
        caps['appium:automationName'] = 'UiAutomator2'
        caps['sauce:options'] = {}
        caps['sauce:options']['appiumVersion'] = '1.17.1'
        caps['sauce:options']['build'] = 'v1.1'
        caps['sauce:options']['name'] = 'appium android test framework'

        url = "https://oauth-pradnyawhatsapp-2034b:3a421996-7481-4900-8c4f-3999ae8580a4@ondemand.us-west-1.saucelabs.com:443/wd/hub"

        # url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"

        driver = webdriver.Remote(url, caps, keep_alive=True)
        return driver


