import unittest
import pytest

from AppiumFrameworkcloud.base.DriverClass import Driver
import AppiumFrameworkcloud.utilities.CustomLogger as cl
from AppiumFrameworkcloud.base.BasePage import BasePage
from AppiumFrameworkcloud.pages.ContactUsFormPage import ContactForm
@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactforTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf=ContactForm(self.driver)


    @pytest.mark.run(order=2)
    def test_enterdatainform(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()


    @pytest.mark.run(order=1)
    def test_openContactForm(self):
        cl.allureLogs("app launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()

