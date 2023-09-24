from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    productText = (By.XPATH, "//div[@class='media-body']/h4")
    chkButton =(By.XPATH, "//button[contains(text(),'Checkout')]")

    def getProductText(self):
        return self.driver.find_element(*ConfirmPage.productText)

    def getCkkOutBtn(self):
        return self.driver.find_element(*ConfirmPage.chkButton)
