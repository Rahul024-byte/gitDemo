from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from soupsieve import select

from pageObjects.CheckOutPage import CheckoutPage


class HomePage:



    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@type = 'password']")
    click = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type = 'submit']")
    message = (By.CLASS_NAME, "alert")
    gender = (By.ID, "exampleFormControlSelect1")
    radiobutton = (By.CSS_SELECTOR, "#inlineRadio1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # * is used to serialize the tuple
        checkout = CheckoutPage(self.driver)  # object creation and driver passing
        return checkout

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheck(self):
        return self.driver.find_element(*HomePage.click)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radiobutton)





