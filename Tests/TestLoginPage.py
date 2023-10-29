import pytest
from selenium import webdriver

from Config.properties import TestProperties
from Pages.HomePage import HomePage
from Tests.TestBase import TestBase


class TestLoginPage(TestBase):
    def test_SignIn_title(self):
        self.homePage = HomePage(self.driver)
        loginPage = self.homePage.click_sign_in_link()
        title = loginPage.get_LoginPage_Title(TestProperties.loginPageTitle)
        assert title == TestProperties.loginPageTitle
        loginPage.do_signIn("snara123@yahoo.com","Qwerty12*")



