import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):

        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        # logger.debug("This is Debug level")
        # logger.info("This is info level")
        # logger.warning("This is warning level")
        # logger.error("This is error level")
        # logger.critical("This is critical level")
        return logger

    def verifyPresence(self, text):

        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionsByVal(self, locator, val):
        DD = Select(locator)
        DD.select_by_index(val)
