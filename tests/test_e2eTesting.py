import time
from selenium.webdriver.common.by import By
from pageObjects import PurchasePage
from pageObjects.CheckOutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.PurchasePage import Purchase
from utilities.BaseClass import BaseClass


class Testing1(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver) #object creation and driver passing
        purchasePageButton = Purchase(self.driver)

        checkout = homePage.shopItems()
        log.info("Getting all cart items")

        checkout.getProducts()

        for phones in checkout.getProducts():
            product_name = checkout.productionSelection(phones).text
            if product_name == "Blackberry":
                checkout.cartButton(phones).click()

            log.info(product_name)

        checkout.coButton().click()

        purchasePageButton.cartCheckout().click()

        purchasePageButton.enterLocation()

        log.info("Enter Country name as ind")

        self.verifyPresence("India")

        purchasePageButton.clickLocation()

        purchasePageButton.agree()

        self.driver.find_element(By.XPATH,"//input[@class= 'btn btn-success btn-lg']").click()

        successMessage = self.driver.find_element(By.XPATH,"//div[@class = 'alert alert-success alert-dismissible']").text

        log.info("Text received is " + successMessage)

        assert "Success! Thank you!" in successMessage

        time.sleep(2)