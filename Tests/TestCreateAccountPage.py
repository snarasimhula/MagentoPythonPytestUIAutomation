import pytest
import random

from Config.properties import TestProperties
from Pages.HomePage import HomePage
from Tests.TestBase import TestBase


class TestCreateAccount(TestBase):


    def test_createAccountPage_tile(self):
        self.homePage = HomePage(self.driver)
        createAccountPage = self.homePage.click_create_account_link()
        title = createAccountPage.get_CreateAccountPage_Title(TestProperties.createAccountPageTitle)
        assert title == TestProperties.createAccountPageTitle
        myAccountPage = createAccountPage.create_account("sriranjani","Narasimhula","snara"+str(random.random())+"@yahoo.com","Qwerty12*","Qwerty12*")
        myAccountPTitle =myAccountPage.get_MyAccountPage_Title(TestProperties.myAccountPageTitle)
        assert myAccountPTitle == TestProperties.myAccountPageTitle
