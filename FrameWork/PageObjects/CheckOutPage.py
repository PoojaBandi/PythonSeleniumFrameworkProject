from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self,driver):
        self.driver = driver

    elems = (By.XPATH, "//div[@class='card h-100']")
    cardText = (By.XPATH, "div/h4/a")
    AddButton = (By.XPATH, "div/button")
    confirmButton = (By.XPATH, "//a[contains(text(),'Checkout')]")

    def getCards(self):
        return self.driver.find_elements(*CheckOut.elems)

    def getCardText(self):
        return self.driver.find_element(*CheckOut.cardText)

    def getAddButton(self):
        return self.driver.find_element(*CheckOut.AddButton)

    def getConfirmButton(self):
        return self.driver.find_element(*CheckOut.confirmButton)

