from selenium.webdriver.common.by import By


class Earn_Credits():
    def __init__(self,driver):
        self.driver = driver

    def select_feature(self,locator_type, locator):
        self.driver.implicitly_wait(30)
        select_twitter_like = self.driver.find_element(locator_type,locator)
        select_twitter_like.click()

        #  hit the like button


    def like_button(self, locator_type, locator):
        like_button = self.driver.find_element(locator_type, locator)
        like_button.click()
        self.driver.implicitly_wait(50)
