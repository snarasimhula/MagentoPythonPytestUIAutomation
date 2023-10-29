from Config.properties import TestProperties
from Pages.HomePage import HomePage
from Tests.TestBase import TestBase


class TestHomePage(TestBase):

     def test_signin_link_visible(self):
         self.homePage = HomePage(self.driver)
         flag = self.homePage.is_Create_Account_Link_Exist()
         assert flag
     def test_homePage_tile(self):
         self.homePage = HomePage(self.driver)
         title = self.homePage.get_title(TestProperties.homePageTitle)
         assert title == TestProperties.homePageTitle




        
        

