from selenium.webdriver.common.by import By


class Purchase:

    def __init__(self,driver):
        self.driver = driver

    CountryTxtBox = (By.ID, "country")
    UStext = (By.LINK_TEXT, "United States of America")
    chkBox = (By.XPATH, "//label[@for = 'checkbox2']")
    purchaseBtn = (By.XPATH, "//input[@value = 'Purchase']")
    DropdwnSuggestions = (By.XPATH, "//div[@class='suggestions']")
    alert = (By.CLASS_NAME, "alert-success")

    def getCountryTxtBox(self):
        return self.driver.find_element(*Purchase.CountryTxtBox)

    def getUsText(self):
        return self.driver.find_element(*Purchase.UStext)

    def getChkBox(self):
        return self.driver.find_element(*Purchase.chkBox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*Purchase.purchaseBtn)

    def getSuggestionsDropdwn(self):
        return self.driver.find_element(*Purchase.DropdwnSuggestions)

    def getAlert(self):
        return self.driver.find_element(*Purchase.alert)
