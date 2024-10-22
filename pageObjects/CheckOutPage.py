from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class = 'card h-100']")
    names = (By.XPATH, "div/h4/a")
    addToCart = (By.XPATH, "div/button")
    coButtonclick = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def productionSelection(self,phones):
        return phones.find_element(*CheckoutPage.names)

    def cartButton(self,phones):
        return phones.find_element(*CheckoutPage.addToCart)

    def coButton(self):
        return self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")

