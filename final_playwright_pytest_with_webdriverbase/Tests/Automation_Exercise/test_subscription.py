from data.Automation_Exercise.test_data_1 import TEST_DATA_1
from Pages.Automation_Exercise.homePage import homePage, homePageLocator
from Pages.Automation_Exercise.cartPage import cartPage, cartPageLocator


from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
from Shared.TestAssert import TestAssert
import pytest

class TestSubscription(webdriverbase):
    site = "https://automationexercise.com/"

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup

        self.obj_homePage = homePage(self.page)
        self.obj_cartPage = cartPage(self.page)
        self.cf = commonfunctions(self.page)
        yield

    def test_10_verify_subscription_in_home_page(self):
        '''Test Case 10: Verify Subscription in home page'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element,'page is not visible')

            # scroll to footer 
            self.obj_homePage.scroll_to_footer()

            #  Verify text 'SUBSCRIPTION'
            subscription_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.subscription_text) 
            self.assertTrue(subscription_text_element,'subscription is not visible')

            # enter email address
            self.obj_homePage.email_input(TEST_DATA_1["subscription"]["email"])

            # click on submit arrow button
            self.cf.click_element(By.XPATH, homePageLocator.arrow_button)

            # verify 'You have been successfully subscribed!' 
            success_text_element = self.cf.is_element_visible(By.XPATH, homePageLocator.success_message) 
            self.assertTrue(success_text_element,'subscription message is not visible')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise



    def test_11_verify_subscription_in_cart_page(self):
        '''Test Case 11: Verify Subscription in Cart page'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_button)
            self.assertTrue(homepage_element,'page is not visible')

            # click cart button
            self.cf.click_element(By.XPATH, cartPageLocator.cart_button)

            # scroll to footer 
            self.obj_cartPage.scroll_to_footer()

            #  Verify text 'SUBSCRIPTION'
            subscription_text_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.subscription_text) 
            self.assertTrue(subscription_text_element,'subscription is not visible')

            # enter email address
            self.obj_cartPage.email_input(TEST_DATA_1["subscription"]["email"])

            # click on submit arrow button
            self.cf.click_element(By.XPATH, homePageLocator.arrow_button)

            # verify 'You have been successfully subscribed!' 
            success_text_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.success_message) 
            self.assertTrue(success_text_element,'subscription message is not visible')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise