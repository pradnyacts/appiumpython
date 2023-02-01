from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(1)

#driver.find_element(By.ID,"user_input").send_keys("Code2Lead")
#driver.find_element(By.CLASS_NAME,"entertext").send_keys("Code2Lead_ClassName")
#driver.find_element(By.NAME,"textbox").send_keys("Code2Lead_Name")
#driver.find_element(By.TAG_NAME,"input").send_keys("Code2Lead_TagName")
#driver.find_element(By.LINK_TEXT,"Form").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"For").click()

time.sleep(1)
driver.quit()