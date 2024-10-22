import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.testHomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self , getData):

        homepage = HomePage(self.driver)
        log = self.getLogger()

        homepage.getName().send_keys(getData["firstName"])
        log.info("Frist name is " +getData["firstName"])
        homepage.getEmail().send_keys(getData["secondName"])
        homepage.getPassword().send_keys("12345678")
        homepage.getCheck().click()
        homepage.getSubmit().click()
        self.selectOptionsByVal(homepage.getGender(), 1)
        homepage.getRadio().click()

        data = homepage.getMessage().text
        assert "Success" in data

        self.driver.refresh()

        time.sleep(2)

    @pytest.fixture(params= HomePageData.getTestData("Test2"))
    def getData(self, request):
        return request.param

