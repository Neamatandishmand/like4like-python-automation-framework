from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class Like4like_Home_page(BaseDriver):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        super().__init__(driver)

