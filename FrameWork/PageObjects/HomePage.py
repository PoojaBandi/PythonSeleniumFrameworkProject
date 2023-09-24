from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    email = (By.XPATH, "//div[@class='form-group']/input[@name='email']")
    password = (By.XPATH, "//div[@class='form-group']/input[@type='password']")
    chkBox = (By.XPATH, "//input[@id='exampleCheck1']")
    genderDropdown = (By.ID, "exampleFormControlSelect1")
    RadioBtn = (By.ID, "inlineRadio1")
    dateInput = (By.XPATH, "//div[@class='form-group']/input[@name='bday']")
    submitBtn = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CLASS_NAME, "alert")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def nameTextBox(self):
        return self.driver.find_element(*HomePage.name)

    def emailTextBox(self):
        return self.driver.find_element(*HomePage.email)

    def PasswordTextBox(self):
        return self.driver.find_element(*HomePage.password)

    def CheckBox(self):
        return self.driver.find_element(*HomePage.chkBox)

    def genderDropDwn(self):
        return self.driver.find_element(*HomePage.genderDropdown)

    def RadioButton(self):
        return self.driver.find_element(*HomePage.RadioBtn)

    def DateInput(self):
        return self.driver.find_element(*HomePage.dateInput)

    def Submit(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)



