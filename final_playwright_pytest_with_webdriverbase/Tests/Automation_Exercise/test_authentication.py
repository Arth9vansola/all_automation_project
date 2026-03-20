import time
from data.Automation_Exercise.test_data_1 import TEST_DATA_1

from Pages.Automation_Exercise.registerPage import registerPage, registerPageLocator
from Pages.Automation_Exercise.loginPage import loginPage, loginPageLocator

from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
from Shared.TestAssert import TestAssert
import pytest


class TestAuthentication(webdriverbase):

    site = "https://automationexercise.com/"

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup

        self.obj_registerPage = registerPage(self.page)
        self.obj_loginPage = loginPage(self.page)
        self.cf = commonfunctions(self.page)

        yield
    
    def test_1_verify_account_registered_deleted(self):
        '''Test Case 1: Register User'''
        try:
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.login_signup)
            self.assertTrue(homepage_element,'Homepage is not visible')

            # click on login/singup of homepage
            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            # signup page verification
            signup_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.signup_text)

            self.assertTrue( signup_element,'singup page is not visible')

            # enter the username and email
            email_cfg = TEST_DATA_1["signup"]["email_strategy"]
            email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'

            self.obj_registerPage.user_signup_input(TEST_DATA_1["signup"]["name"], email)

            # click on signup
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            # account information verification
            acc_info_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.acc_info_intro_text)
            self.assertTrue(acc_info_element,'account information page is not visible')

            # account information details filling

            self.obj_registerPage.fill_acc_form_details(
                TEST_DATA_1["signup"]["title"],
                TEST_DATA_1["signup"]["password"],
                TEST_DATA_1["signup"]["dob"]
            )

            cb = TEST_DATA_1["signup"]["checkboxes"]
            self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])

            addr = TEST_DATA_1["signup"]["address"]
            self.obj_registerPage.fill_address_form_details(
                addr["first_name"],
                addr["last_name"],
                addr["company"],
                addr["address1"],
                addr["address2"],
                addr["country"],
                addr["state"],
                addr["city"],
                addr["zipcode"],
                addr["mobile"]
            )

            # click on create account button
            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            # account creation verification
            account_created_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text)
            self.assertTrue(account_created_element,'account is not created')

            # click on continue button of account created
            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            # username visiblity verification
            username_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)

            self.assertTrue(username_element,'failed to show logged in')

            # delete account click
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)

            # account deletion verification
            del_continue_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(del_continue_element,'error while deleting account')

            # continue button click on deleted account page
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn)

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_2_verify_account_login_right_credentials(self):
        '''Test Case 2: Login User with correct email and password'''
        try:

            homepage_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_signup)
            self.assertTrue(homepage_element,'page is not visible')

            # click on login/signup button on homepage
            self.cf.click_element(By.XPATH, loginPageLocator.login_signup)

            # login page visiblity verification
            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)

            self.assertTrue( login_element,'login page is not visible')

            '''this will create account and return login credential for login'''
            # Create a fresh account first
            email, password = self.obj_registerPage.create_account(
                TEST_DATA_1["signup"],
                TEST_DATA_1["signup"]["email_strategy"],
            )

            # Logout to ensure we perform an actual login step
            self.cf.click_element(By.XPATH, loginPageLocator.logout_button)

            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)
            self.assertTrue(login_element, 'login page is not visible after logout')

            # enter the the login details and click on the login button
            self.obj_loginPage.user_login_input(email, password)
            self.cf.click_element(By.XPATH, loginPageLocator.login_btn)

            # username visiblity verificaiton
            username_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.username_visible_btn)

            self.assertTrue(username_element,'failed to show logged in user')

            # click on delete button
            self.cf.click_element(By.XPATH, loginPageLocator.del_acc_btn)

            # account deletion verification
            del_continue_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.del_acc_text)
            self.assertTrue(del_continue_element,'error while deleting account')

            # Continue after deletion
            self.cf.click_element(By.XPATH, loginPageLocator.del_acc_continue_btn)

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_3_verify_account_login_wrong_credentials(self):
        '''Test Case 3: Login User with incorrect email and password'''
        try:

            # homepage visiblity verification
            homepage_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_signup)
            self.assertTrue(homepage_element,'page is not visible')

            # click on login/signup button on homepage
            self.cf.click_element(By.XPATH, loginPageLocator.login_signup)

            # login page visiblity verification
            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)

            self.assertTrue( login_element,'login page is not visible')

            # enter the the login details and click on the login button
            bad = TEST_DATA_1["login"]["invalid"]
            self.obj_loginPage.user_login_input(bad["email"], bad["password"])
            self.cf.click_element(By.XPATH, loginPageLocator.login_btn)

            # wrong credentials error verification
            error_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.error_after_password)
            self.assertTrue(error_element,'credentials are right')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_4_verify_account_logout_user(self):
        '''Test Case 4: Logout User'''
        try:

            # homepage visiblity verification
            homepage_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_signup)
            self.assertTrue(homepage_element,'page is not visible')

            # click on login/signup button on homepage
            self.cf.click_element(By.XPATH, loginPageLocator.login_signup)

            # login page visiblity verification
            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)

            self.assertTrue( login_element,'login page is not visible')

            # enter the the login details and click on the login button
            logout_user = TEST_DATA_1["login"]["logout_user"]
            self.obj_loginPage.user_login_input(logout_user["email"], logout_user["password"])
            self.cf.click_element(By.XPATH, loginPageLocator.login_btn)

            # username visiblity verificaiton
            username_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.username_visible_btn)

            self.assertTrue(username_element,'failed to show logged in')

            # click on logout button
            self.cf.click_element(By.XPATH, loginPageLocator.logout_button)

            # back to login page visiblity verification
            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)

            self.assertTrue( login_element,'login page is not visible')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_5_verify_acccount_register_email_exist(self):
        '''Test Case 5: Register User with existing email'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.login_signup)
            self.assertTrue(homepage_element,'page is not visible')

            # click on login/singup of homepage
            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            # signup page verification
            signup_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.signup_text)

            self.assertTrue( signup_element,'singup page is not visible')

            # enter the username and password
            existing = TEST_DATA_1["existing_signup"]
            self.obj_registerPage.user_signup_input(existing["name"], existing["email"])

            # click on signup
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            # error while signup
            error_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.error_after_email)
            self.assertTrue(error_element,'error is not there')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise