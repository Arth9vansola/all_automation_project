# import time
from Pages.Automation_Exercise.homePage import homePage, homePageLocator


from Shared.webdriverbase import webdriverbase 
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
from Shared.TestAssert import TestAssert
import pytest


class TestUiScroll(webdriverbase):
    site = "https://automationexercise.com/"

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup

        self.obj_homePage = homePage(self.page)
        self.cf = commonfunctions(self.page)
        yield

    def test_25_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(self):
        '''Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element,'page is not visible')

            # scroll to footer 
            self.obj_homePage.scroll_to_footer()

            #  Verify text 'SUBSCRIPTION'
            subscription_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.subscription_text) 
            self.assertTrue(subscription_text_element,'subscription is not visible')

            #  Click on arrow at bottom right side to move upward
            self.cf.click_element(By.XPATH, homePageLocator.bottom_to_top_arrow_button)

            # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
            top_banner_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.top_banner_text) 
            self.assertTrue(top_banner_text_element,"Top banner text is not visible after scrolling up")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise



    def test_26_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(self):
        '''Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element, 'page is not visible')

            # scroll to footer 
            self.obj_homePage.scroll_to_footer()

            #  Verify text 'SUBSCRIPTION'
            subscription_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.subscription_text) 
            self.assertTrue(subscription_text_element, 'subscription is not visible')

            #  scroll up page to top
            self.obj_homePage.scroll_to_top()

            # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
            top_banner_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.subscription_text) 
            self.assertTrue(top_banner_text_element, 'Top banner text is not visible after scrolling up')


        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise