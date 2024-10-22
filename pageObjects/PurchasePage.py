
from selenium.webdriver.common.by import By


class Purchase:

    def __init__(self, driver):
        self.driver = driver

    purchaseCheckout = (By.XPATH, "//button[@class = 'btn btn-success']")
    country = (By.ID, "country")
    countrySelected = (By.LINK_TEXT,"India")
    terms =  (By.XPATH,"//div[@class= 'checkbox checkbox-primary']/label")

    def cartCheckout(self):
        return self.driver.find_element(By.XPATH,"//button[@class = 'btn btn-success']")

    def enterLocation(self):
        return self.driver.find_element(By.ID, "country").send_keys("Ind")

    def clickLocation(self):
        return self.driver.find_element(By.LINK_TEXT,"India").click()

    def agree(self):
        return self.driver.find_element(By.XPATH,"//div[@class= 'checkbox checkbox-primary']/label").click()