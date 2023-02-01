from SeleniumFramework.Base.DriverClass import WebDriverClass
from SeleniumFramework.Pages.ContctFormPage import ContactForm
import SeleniumFramework.Utilities.CustonLogger as cl
import time
from SeleniumFramework.Base.BasePage import BaseClass
wd=WebDriverClass()
driver=wd.getWebDriver("chrome")
bp=BaseClass(driver)
bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
cf=ContactForm(driver)
cf.clickContactForm()
time.sleep(2)
cf.verifyFormPage()
cf.enterName()
cf.enterEmail()
cf.enterMessage()
cf.enterCaptha()
cf.clickOnPostButton()


# ele=bp.isElementDisplayed("user_input","id")
# print(ele)
# bp.sendText("testweb","user_input","id")
# bp.clickOnElement("Form","link")

time.sleep(2)
driver.quit()
