from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('C:/Users/pradn/OneDrive/Documents/app/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps['noReset'] = True
#['fullReset'] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
