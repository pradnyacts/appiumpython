from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:/Drivers/chromedriver/geckodriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()