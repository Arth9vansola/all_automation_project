import time
from data.Automation_Exercise.test_data_1 import TEST_DATA_1
from Pages.Automation_Exercise.registerPage import registerPage, registerPageLocator
from Pages.Automation_Exercise.loginPage import loginPage, loginPageLocator
from Pages.Automation_Exercise.productPage import productPage, productPageLocator
from Pages.Automation_Exercise.homePage import homePage, homePageLocator
from Pages.Automation_Exercise.cartPage import cartPage, cartPageLocator
from Pages.Automation_Exercise.paymentPage import paymentPage, paymentPageLocator

from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
from Shared.TestAssert import TestAssert
import pytest


class TestOrder(webdriverbase):
    site = "https://automationexercise.com/"

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup
        self.obj_registerPage = registerPage(self.page)
        self.obj_loginPage = loginPage(self.page)
        self.obj_productPage = productPage(self.page)
        self.obj_homePage = homePage(self.page)
        self.obj_cartPage = cartPage(self.page)
        self.obj_paymentPage = paymentPage(self.page)
        self.cf = commonfunctions(self.page)
        yield

    def test_16_verify_place_order_login_before_checkout(self):
        '''Test Case 16: Place Order: Login before Checkout'''
        try:
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element, "Homepage not visible")

            # click on signup/login 
            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)
            self.assertTrue(login_element, "login page is not visible")

            # Create a fresh account with address details, then login with it (rerunnable)
            email, password = self.obj_registerPage.create_account(
                TEST_DATA_1["checkout_signup"],
                TEST_DATA_1["signup"]["email_strategy"],
            )
            self.cf.click_element(By.XPATH, loginPageLocator.logout_button)

            login_element = self.cf.is_element_visible(By.XPATH, loginPageLocator.login_page_text)
            self.assertTrue(login_element, "login page is not visible after logout")

            # enter the the login details and click on the login button   
            self.obj_loginPage.user_login_input(email, password)
            self.cf.click_element(By.XPATH, loginPageLocator.login_btn)

            # Logged in verification
            logged_in = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)
            self.assertTrue(logged_in, "User not logged in")

            # Add product to cart
            self.obj_productPage.add_product_to_cart_by_index(TEST_DATA_1["products"]["single_add_index"])

            # click 'Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Cart page verification
            cart_page = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_page, "Cart page not visible")

            # Proceed to checkout button click
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # address details verification
            address_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.address_details_text)
            self.assertTrue(address_element, "Address section missing")

            # Review Your Order details verification
            review_order_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.review_order_text)
            self.assertTrue(review_order_element, "Review order section missing")

            # Place the order
            self.obj_cartPage.enter_comment_and_place_order(TEST_DATA_1["order"]["comment"])

            # Enter payment details
            pay = TEST_DATA_1["payment"]
            self.obj_paymentPage.enter_payment_details(
                pay["name_on_card"],
                pay["card_number"],
                pay["cvc"],
                pay["expiry_month"],
                pay["expiry_year"],
            )

            # Verify success message
            success_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.success_message)
            self.assertTrue(success_element, "Order not placed successfully")

            # Delete account button 
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)

            # Verify 'ACCOUNT DELETED!'
            deleted_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(deleted_element, "Account not deleted")

            # click on continue button
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn)

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise
    

    def test_23_verify_address_details_in_checkout_page(self):
        '''Test Case 23: Verify address details in checkout page'''
        try:
            homepage_visible = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_visible, "Home page is not visible")

            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            email_cfg = TEST_DATA_1["signup"]["email_strategy"]
            email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
            self.obj_registerPage.user_signup_input(TEST_DATA_1["checkout_signup"]["name"], email)
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            self.obj_registerPage.fill_acc_form_details(
                TEST_DATA_1["checkout_signup"]["title"],
                TEST_DATA_1["checkout_signup"]["password"],
                TEST_DATA_1["checkout_signup"]["dob"],
            )

            cb = TEST_DATA_1["checkout_signup"]["checkboxes"]
            self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])

            addr = TEST_DATA_1["checkout_signup"]["address"]
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
                addr["mobile"],
            )

            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            created = self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text)
            self.assertTrue(created, "ACCOUNT CREATED! is not visible")

            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            logged_in = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)
            self.assertTrue(logged_in, "Logged in as username is not visible")

            self.cf.click_element(By.XPATH, productPageLocator.product_button)
            self.obj_productPage.add_product_to_cart_by_index(TEST_DATA_1["products"]["single_add_index"])
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            cart_visible = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_visible, "Cart page is not visible")

            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            address_section = self.cf.is_element_visible(By.XPATH, cartPageLocator.address_details_text)
            self.assertTrue(address_section, "Address Details section is not visible")

            delivery_text = self.obj_cartPage.get_delivery_address_text()
            self.assertTrue(addr["address1"] in delivery_text)
            self.assertTrue(addr["address2"] in delivery_text)

            billing_text = self.obj_cartPage.get_billing_address_text()
            self.assertTrue(addr["address1"] in billing_text)
            self.assertTrue(addr["address2"] in billing_text)

            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)

            deleted = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(deleted, "ACCOUNT DELETED! is not visible")

            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn)

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise
            
    def test_14_verify_place_order_register_while_checkout(self):
        '''Test Case 14: Place Order: Register while Checkout'''
        try:
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element, "Homepage not visible")

            # click on product 
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # Add product to cart
            self.obj_productPage.add_product_to_cart_by_index(TEST_DATA_1["products"]["single_add_index"])

            # click 'Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Cart page verification
            cart_page = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_page, "Cart page not visible")


            # Proceed to checkout button click
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # Register / Login button click
            self.cf.click_element(By.XPATH, cartPageLocator.register_login_button)

            # Signup user
            email_cfg = TEST_DATA_1["signup"]["email_strategy"]
            email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
            self.obj_registerPage.user_signup_input(TEST_DATA_1["checkout_signup"]["name"], email)
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            self.obj_registerPage.fill_acc_form_details(
                TEST_DATA_1["checkout_signup"]["title"],
                TEST_DATA_1["checkout_signup"]["password"],
                TEST_DATA_1["checkout_signup"]["dob"],
            )
            cb = TEST_DATA_1["checkout_signup"]["checkboxes"]
            self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])
            addr = TEST_DATA_1["checkout_signup"]["address"]
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
                addr["mobile"],
            )

            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            account_created = self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text)
            self.assertTrue(account_created, "Account not created")

            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            # Logged in verification
            logged_in = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)
            self.assertTrue(logged_in, "User not logged in")


            # Cart in  Checkout again
            # click on cart button
            self.cf.click_element(By.XPATH, cartPageLocator.cart_button)

            # click on proceed to checkout
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # address details verification
            address_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.address_details_text)
            self.assertTrue(address_element, "Address section missing")


            # Review Your Order details verification
            review_order_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.review_order_text)
            self.assertTrue(review_order_element, "Review order section missing")


            # Place the order
            self.obj_cartPage.enter_comment_and_place_order(TEST_DATA_1["order"]["comment"])

            # Enter payment details
            pay = TEST_DATA_1["payment"]
            self.obj_paymentPage.enter_payment_details(
                pay["name_on_card"],
                pay["card_number"],
                pay["cvc"],
                pay["expiry_month"],
                pay["expiry_year"],
            )

            # Verify success message 'Your order has been placed successfully!'
            success_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.success_message)
            self.assertTrue(success_element, "Order not placed successfully")


            # Delete account button 
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)

            #  Verify 'ACCOUNT DELETED!' 
            deleted_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(deleted_element, "Account not deleted")


            # click on continue button
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn)

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_15_verify_place_order_register_before_checkout(self):
        '''Test Case 15: Place Order: Register before Checkout'''
        try:
            # homepage visiblity
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element, 'Homepage not visible')


            # click on signup/login 
            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            # Signup user
            email_cfg = TEST_DATA_1["signup"]["email_strategy"]
            email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
            self.obj_registerPage.user_signup_input(TEST_DATA_1["checkout_signup"]["name"], email)
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            self.obj_registerPage.fill_acc_form_details(
                TEST_DATA_1["checkout_signup"]["title"],
                TEST_DATA_1["checkout_signup"]["password"],
                TEST_DATA_1["checkout_signup"]["dob"],
            )
            cb = TEST_DATA_1["checkout_signup"]["checkboxes"]
            self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])
            addr = TEST_DATA_1["checkout_signup"]["address"]
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
                addr["mobile"],
            )

            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            account_created = self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text)
            self.assertTrue(account_created, 'Account not created')


            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            # Logged in verification
            logged_in = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)
            self.assertTrue(logged_in, 'User not logged in')

            # Add product to cart
            self.obj_productPage.add_product_to_cart_by_index(TEST_DATA_1["products"]["single_add_index"])

            # click 'Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Cart page verification
            cart_page = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_page, 'Cart page not visible')


            # Proceed to checkout button click
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # address details verification
            address_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.address_details_text)
            self.assertTrue(address_element, 'Address section missing')


            # Review Your Order details verification
            review_order_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.review_order_text)
            self.assertTrue(review_order_element, 'Review order section missing')


            # Place the order
            self.obj_cartPage.enter_comment_and_place_order(TEST_DATA_1["order"]["comment"])

            # Enter payment details
            pay = TEST_DATA_1["payment"]
            self.obj_paymentPage.enter_payment_details(
                pay["name_on_card"],
                pay["card_number"],
                pay["cvc"],
                pay["expiry_month"],
                pay["expiry_year"],
            )

            # Verify success message 'Your order has been placed successfully!'
            success_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.success_message)
            self.assertTrue(success_element, 'Order not placed successfully')


            # Delete account button 
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)

            #  Verify 'ACCOUNT DELETED!' 
            deleted_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(deleted_element, 'Account not deleted')


            # click on continue button
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn)
            
        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise

    def test_24_verify_Download_Invoice_after_purchase_order(self):
        '''Test Case 24: Download Invoice after purchase order'''
        try:
            # Verify home page is visible
            homepage_visible = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_visible, 'Home page is not visible')


            # Add product to cart
            self.cf.click_element(By.XPATH, productPageLocator.product_button)
            self.obj_productPage.add_product_to_cart_by_index(TEST_DATA_1["products"]["single_add_index"])
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Verify cart page displayed
            cart_visible = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_visible, 'Cart page is not visible')


            # Proceed to checkout
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # Register / Login button click
            self.cf.click_element(By.XPATH, cartPageLocator.register_login_button)

            # Signup user
            email_cfg = TEST_DATA_1["signup"]["email_strategy"]
            email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
            self.obj_registerPage.user_signup_input(TEST_DATA_1["checkout_signup"]["name"], email)
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            self.obj_registerPage.fill_acc_form_details(
                TEST_DATA_1["checkout_signup"]["title"],
                TEST_DATA_1["checkout_signup"]["password"],
                TEST_DATA_1["checkout_signup"]["dob"],
            )
            cb = TEST_DATA_1["checkout_signup"]["checkboxes"]
            self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])

            addr = TEST_DATA_1["checkout_signup"]["address"]
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
                addr["mobile"],
            )

            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            account_created = self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text)
            self.assertTrue(account_created, 'Account not created')


            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            # Verify Logged in as username
            logged_in = self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn)
            self.assertTrue(logged_in, 'Logged in as username is not visible')


            # click on cart button
            self.cf.click_element(By.XPATH, cartPageLocator.cart_button)

            # click on proceed to checkout
            self.cf.click_element(By.XPATH, cartPageLocator.proceed_to_checkout)

            # address details verification
            address_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.address_details_text)
            self.assertTrue(address_element, 'Address section missing')


            # Review Your Order details verification
            review_order_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.review_order_text)
            self.assertTrue(review_order_element, 'Review order section missing')


            # Place the order
            self.obj_cartPage.enter_comment_and_place_order(TEST_DATA_1["order"]["comment"])

            # Enter payment details
            pay = TEST_DATA_1["payment"]
            self.obj_paymentPage.enter_payment_details(
                pay["name_on_card"],
                pay["card_number"],
                pay["cvc"],
                pay["expiry_month"],
                pay["expiry_year"]
            )

            # Verify success message 'Your order has been placed successfully!'
            success_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.success_message)
            self.assertTrue(success_element, 'Order not placed successfully')

        
            # Click 'Download Invoice' button and verify invoice is downloaded successfully.
            invoice_downloaded = self.obj_paymentPage.download_invoice(self.download_path)
            self.assertTrue(invoice_downloaded, 'Invoice not downloaded')


            # click on continue button
            self.cf.click_element(By.XPATH, paymentPageLocator.payment_page_continue_button)

            # delete account click    
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_btn)   

            # account deletion verification 
            del_continue_element = self.cf.is_element_visible(By.XPATH, registerPageLocator.deleted_account_text)
            self.assertTrue(del_continue_element, 'error while deleting account')


            # continue button click on deleted account page 
            self.cf.click_element(By.XPATH, registerPageLocator.del_acc_continue_btn) 

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise