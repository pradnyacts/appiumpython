from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("C:\Drivers\chromedriver"), options=options)

driver.get("http://www.dummypoint.com/Actions.html")
assert "Selenium Template" in driver.title
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

ele = wait.until(ec.presence_of_element_located((By.LINK_TEXT,"Form")))

# Import the ActionChains Class

# 1. Create the object for ActionChains class
actions = ActionChains(driver)


# 2. Double click Operation
#actions.double_click(ele).perform()



# 3. Right click Operation
actions.context_click().perform()
actions.context_click(ele).perform()


time.sleep(5)
driver.quit()
