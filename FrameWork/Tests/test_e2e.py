from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from FrameWork.PageObjects.CheckOutPage import CheckOut
from FrameWork.PageObjects.ConfrmPage import ConfirmPage
from FrameWork.PageObjects.HomePage import HomePage
from FrameWork.PageObjects.Purchase import Purchase
from FrameWork.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(4)
        homePageObj = HomePage(self.driver)
        homePageObj.shopItems().click()

        checkOutObj = CheckOut(self.driver)
        log.info("getting all cards")
        cards = checkOutObj.getCards()
        cardText = ''
        for card in cards:
            cardText = card.find_element(By.XPATH, "div/h4/a").text
            log.info(cardText)
            if cardText == 'Blackberry':
                card.find_element(By.XPATH, "div/button").click()
                break

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
        checkOutObj.getConfirmButton().click()
        confirmPageObj = ConfirmPage(self.driver)

        ProductName = confirmPageObj.getProductText().text

        assert ProductName == "Blackberry"

        # self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        confirmPageObj.getCkkOutBtn().click()

        purchasePageObj = Purchase(self.driver)
        log.info("Entering country name 'un' for suggestions")
        purchasePageObj.getCountryTxtBox().send_keys("un")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']")))
        self.waitforElementPresence(By.XPATH, "//div[@class='suggestions']")
        purchasePageObj.getUsText().click()
        purchasePageObj.getChkBox().click()
        purchasePageObj.getPurchaseBtn().click()

        SuccessText = purchasePageObj.getAlert().text

        assert "Success!" in SuccessText
