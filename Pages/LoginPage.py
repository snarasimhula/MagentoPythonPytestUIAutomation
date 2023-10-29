from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_EMAIL_ID = (By.XPATH, "//*[@id='email']")
    LOGIN_PASSWORD = (By.XPATH, "//*[@id='pass']")
    SIGN_BUTTON = (By.XPATH, "(//span[contains(text(),'Sign In')])[1]")

    def __int__(self, driver):
        super().__init__(driver)

    def get_LoginPage_Title(self, title):
        return self.get_title(title)

    def do_signIn(self, email, password):
        self.do_send_keys(self.LOGIN_EMAIL_ID, email)
        self.do_send_keys(self.LOGIN_PASSWORD, password)
        self.do_click(self.SIGN_BUTTON)
