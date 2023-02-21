import logging
import time
import softest
import pytest
from selenium.webdriver.common.by import By
from pages.earn_credits_page import Earn_Credits
from pages.like4like_launch_page import LaunchPage
from pages.twitter_like_util import Twitter_Like_Util
from utilities.custom_logger import custLogger
from utilities.read_data import Read_Data
from ddt import ddt, unpack, data,file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestLike4LikeAutomation(softest.TestCase):
    log = custLogger.cuslogger(loglevel=logging.WARNING)
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.earn = Earn_Credits(self.driver)
        self.TL = Twitter_Like_Util(self.driver)
    # @data(("username","password","//option[@value='twitterfav']"),("username","password","//option[@value='twitter']"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testdata.yaml")
    # @data(*Read_Data.read_data_from_ex("D:\\udemy\\my records for udemy\\Mastering python automation for every day life\\Test Automation Framework\\TestAutomationFramework\\testdata\\testdata.xlsx","Sheet1"))
    @data(*Read_Data.read_data_from_csv("D:\\udemy\\my records for udemy\\Mastering python automation for every day life\\Test Automation Framework\\TestAutomationFramework\\testdata\\testdata.csv"))
    @unpack

    def test_like4like(self,User,Passw,locator):
        # launch the browser and like4like website

        # hit the login

        self.lp.clicklogin()

        # handle login
        self.lp.like4like_login(User,Passw)

        # free credits
        self.lp.element_to_be_clickable(By.XPATH,"//ul[@class='font-book']//li//a[text()='Free']")
        self.log.warning("free button clicked")
        # //option[@value='twitter']
        self.earn.select_feature(By.XPATH, locator)
        self.log.warning("select_feature selected")
        parent_handler = self.driver.current_window_handle
        # self.earn.like_button(By.CSS_SELECTOR, "div[id^='likebutton']")
        # self.log.warning("like button clicked")



        # self.TL.like_tweet(parent_handler,"username","password")
        # self.log.warning("all tweet liked!")
        self.lp.like4like_logout()
        self.lp.clicklogin()





