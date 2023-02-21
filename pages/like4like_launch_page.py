import logging

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.custom_logger import custLogger


class LaunchPage(BaseDriver):
    log = custLogger.cuslogger(loglevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clicklogin(self):
        login = self.driver.find_element(By.XPATH, "//a[@title='Login ']")
        login.click()
        self.log.debug("hit the login button")