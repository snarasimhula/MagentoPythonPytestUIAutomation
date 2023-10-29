from Config.properties import TestProperties
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Pages.MyAccountPage import MyAccountPage


class CreateAccountPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='lastname']")
    EMAIL = (By.XPATH, "//input[@id='email_address']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='password-confirmation']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@title='Create an Account']")

    def __int__(self, driver):
        super().__init__(driver)


    def get_CreateAccountPage_Title(self, title):
        return self.get_title(title)

    def create_account(self, firstName, lastName, email, password, confirmPassword):
        self.do_send_keys(self.FIRST_NAME, firstName)
        self.do_send_keys(self.LAST_NAME, lastName)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, confirmPassword)
        self.do_click(self.CREATE_ACCOUNT_BUTTON)
        return MyAccountPage(self.driver)

