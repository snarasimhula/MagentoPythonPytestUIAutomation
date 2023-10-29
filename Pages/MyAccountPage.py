from Pages.BasePage import BasePage


class MyAccountPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)


    def get_MyAccountPage_Title(self, title):
        return self.get_title(title)


