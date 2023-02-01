"""
An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to
find any element (or elements) not immediately available.

"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)
driver.implicitly_wait(10)

driver.find_element(By.ID,"user_input").send_keys("Code2Lead")


time.sleep(5)
driver.quit()