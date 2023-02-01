from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

ele = driver.find_elements(By.CLASS_NAME,"section-header")

for menu in ele:
    print(menu.text)

time.sleep(5)
driver.quit()