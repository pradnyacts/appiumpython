from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template" in driver.title
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()

time.sleep(5)
driver.quit()