import time
from data.Sauce_demo_site.test_data_2 import TEST_DATA_2

from Pages.Sauce_demo_site.loginPage import loginPage, loginPageLocator
from Pages.Sauce_demo_site.productPage import productPage, productPageLocator

from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By
# from Shared.locator import By


class TestAuthentication(webdriverbase):

    def setUp(self):
        self.website_url = 'https://www.saucedemo.com/'
        super().setUp()

        self.obj_loginPage = loginPage(self.driver)
        self.obj_productPage = productPage(self.driver)
        self.cf = commonfunctions(self.driver)
    
    def test_1_verify_account_login_with_correct_credentials(self):
        '''Test Case 1: Login User with correct credentials'''
        try:

            # login page verification
            self.assertEqual(self.website_url, self.driver.current_url ,'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'login is not successfull')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_2_verify_account_login_with_incorrect_credentials(self):
        '''Test Case 2: Login User with incorrect credentials'''
        try:

            # login page verification
            self.assertEqual(self.website_url, self.driver.current_url ,'Homepage is not visible')

            # enter the username and password
            cred_wrong = TEST_DATA_2["login_user_wrong"]
            self.obj_loginPage.user_login_input(cred_wrong["user_name"], cred_wrong["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that error message is shown
            error_message_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.error_message)
            self.assertTrue(error_message_element,'there is no wrong credentials')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_3_verify_account_logout_user(self):
        '''Test Case 3: Logout User '''
        try:

            # login page verification
            self.assertEqual(self.website_url, self.driver.current_url ,'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'login is not successfull')

            # logout the user
            self.cf.click_element(By.XPATH, productPageLocator.menu_button)
            self.cf.click_element(By.XPATH, productPageLocator.logout_button)

            # login page verification
            self.assertEqual(self.website_url, self.driver.current_url ,'Homepage is not visible')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise