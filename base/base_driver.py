import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver



    def element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        free = wait.until(EC.element_to_be_clickable((locator_type,locator))).click()
        return free


    def login(self, locator_type, locator):
        self.driver.find_element(locator_type, locator).click()

    def username(self,locator_type, locator, UserName):
        user = self.driver.find_element(locator_type,locator)
        user.send_keys(UserName)

    def password(self,locator_type, locator, password):
        passw = self.driver.find_element(locator_type,locator)
        passw.send_keys(password)

    def submit_button(self,locator_type, locator):
        submit_b = self.driver.find_element(locator_type,locator)
        submit_b.click()


    def like4like_login(self,User,Passw):
            self.username(By.XPATH, "//input[@id='username']", User)
            self.log.warning("the username is entered ")
            self.password(By.XPATH, "//input[@id='password']", Passw)
            self.log.warning("the username is entered ")

            self.submit_button(By.XPATH, "//span[@class='button medium orange cursor']")
            self.log.warning("the submit button hit")

    def like4like_logout(self):
        chain = ActionChains(self.driver)
        chain.move_to_element(self.driver.find_element(By.XPATH, "//a[@title='User Profile']")).perform()
        logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        time.sleep(5)
        logout.click()


