

from FrameWork.PageObjects.HomePage import HomePage
from FrameWork.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.nameTextBox().send_keys("pooja")
        homePage.emailTextBox().send_keys("pooja@gmail.com")
        homePage.PasswordTextBox().send_keys("pooja")
        homePage.CheckBox().click()

        self.selectOptionByText(homePage.genderDropDwn(), "Female")
        homePage.RadioButton().click()
        homePage.DateInput().send_keys("09-09-2023")
        homePage.Submit().click()

        text = homePage.getAlert().text
        log.info(text)
        assert "Success" in text













