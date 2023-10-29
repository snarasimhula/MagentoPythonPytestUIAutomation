from Config.properties import TestProperties
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

from Pages.CreateAccountPage import CreateAccountPage
from Pages.LoginPage import LoginPage


class HomePage(BasePage):
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")
    SIGN_IN_LINK = (By.XPATH, "(//a[contains(text(),'Sign In')])[1]")

    def __int__(self, driver):
        super().__init__(driver)



    def get_HomePage_Title(self, title):
        return self.get_title(title)

    def is_Create_Account_Link_Exist(self):
        return self.is_visible(self.CREATE_ACCOUNT_LINK)

    def click_create_account_link(self):
        self.do_click(self.CREATE_ACCOUNT_LINK)
        return CreateAccountPage(self.driver)

    def click_sign_in_link(self):
        self.do_click(self.SIGN_IN_LINK)
        return LoginPage(self.driver)