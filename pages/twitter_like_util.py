import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class Twitter_Like_Util(BaseDriver):
    def __init__(self,driver):
        self.driver = driver
    def like_tweet(self,parent_handle,TwitterUsername,TwitterPassword):

        all_handler = self.driver.window_handles
        for handle in all_handler:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.driver.implicitly_wait(10)
                time.sleep(5)
                BaseDriver.login(self,By.XPATH, "//span[text()='Log in']")
                self.driver.implicitly_wait(100)

                BaseDriver.username(self,By.XPATH, "//input[@name='text']",TwitterUsername)

                BaseDriver.submit_button(self, By.CSS_SELECTOR,
                                         "div[role='button'] div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")

                self.driver.implicitly_wait(100)
                BaseDriver.password(self,By.XPATH, "//input[@name='password']",TwitterPassword)

                BaseDriver.submit_button(self,By.CSS_SELECTOR,"div[role='button'] div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")

                self.driver.implicitly_wait(300)
                time.sleep(30)
                BaseDriver.submit_button(self,By.XPATH, "//div//div[@data-testid='like']")

                self.driver.implicitly_wait(100)
                # like.click()
                time.sleep(5)
                print("one tweet liked!")
                self.driver.implicitly_wait(400)
                self.driver.close()
                self.driver.switch_to.window(parent_handle)
                time.sleep(4)
                BaseDriver.submit_button(self,By.XPATH, "//img[@title='Click On The Button To Confirm Interaction!']")
                break



        list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        count = 0
        for li in list:
            BaseDriver.submit_button(self,By.CSS_SELECTOR, "div[id^='likebutton']")
            self.driver.implicitly_wait(100)
            a_handle = self.driver.window_handles
            try:
                for handle in a_handle:
                    if handle != parent_handle:
                        self.driver.switch_to.window(handle)
                        self.driver.implicitly_wait(100)
                        time.sleep(5)
                        BaseDriver.login(self,By.XPATH, "//span[text()='Log in']")
                        self.driver.implicitly_wait(100)
                        BaseDriver.username(self,By.XPATH, "//input[@name='text']", TwitterUsername)

                        BaseDriver.submit_button(self,By.CSS_SELECTOR,
                                                 "div[role='button'] div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")

                        self.driver.implicitly_wait(100)
                        BaseDriver.password(self,By.XPATH, "//input[@name='password']", TwitterPassword)

                        BaseDriver.submit_button(self,By.CSS_SELECTOR,
                                                 "div[role='button'] div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")

                        self.driver.implicitly_wait(300)
                        time.sleep(5)
                        BaseDriver.submit_button(self,By.XPATH, "//div//div[@data-testid='like']")
                        self.driver.implicitly_wait(10)

                        time.sleep(5)
                        print("one tweet liked!")
                        self.driver.implicitly_wait(40)
                        self.driver.close()
                        self.driver.switch_to.window(parent_handle)
                        time.sleep(5)
                        BaseDriver.submit_button(self,By.XPATH,
                                                 "//img[@title='Click On The Button To Confirm Interaction!']")

            except:
                for handle in a_handle:
                    count += 1
                    if handle != parent_handle:
                        self.driver.switch_to.window(handle)

                        self.driver.implicitly_wait(90)
                        time.sleep(2)
                        BaseDriver.submit_button(self,By.XPATH, "//div[@aria-label='Like'][@role='button'][@tabindex='0']")
                        self.driver.implicitly_wait(100)

                        print("You liked ", count, " tweets")
                        time.sleep(2)
                        self.driver.implicitly_wait(400)
                        self.driver.close()
                        self.driver.switch_to.window(parent_handle)
                        time.sleep(1)
                        time.sleep(5)
                        BaseDriver.submit_button(self,By.XPATH,
                                                 "//img[@title='Click On The Button To Confirm Interaction!']")

                        time.sleep(5)