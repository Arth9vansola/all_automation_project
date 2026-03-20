import time
from data.Sauce_demo_site.test_data_2 import TEST_DATA_2

from Pages.Sauce_demo_site.loginPage import loginPage, loginPageLocator
from Pages.Sauce_demo_site.productPage import productPage, productPageLocator
from Pages.Sauce_demo_site.cartPage import cartPage, cartPageLocator
from Pages.Sauce_demo_site.paymentPage import paymentPage,paymentPageLocator

from Shared.TestAssert import TestAssert
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
import pytest

@pytest.mark.SauceDemo
@pytest.mark.usefixtures("sauce_order_object")
class TestOrder(TestAssert):

    site = 'https://www.saucedemo.com/'

    # @pytest.fixture(autouse=True)
    # def init_pages(self,setup):

    #     self.page = setup
    #     self.obj_loginPage = loginPage(self.page)
    #     self.obj_productPage = productPage(self.page)
    #     self.obj_cartPage = cartPage(self.page)
    #     self.obj_paymentPage = paymentPage(self.page)
    #     self.cf = commonfunctions(self.page)
    #     yield

    def test_9_verify_checkout_after_adding_product(self):
        '''Test Case 9: checkout after adding product '''
        try:

            # login page verification
            self.assertEqual(self.site, self.page.url ,'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'login is not successfull')

            # add product to cart 
            product_name = TEST_DATA_2["add_to_cart"]
            self.obj_productPage.add_to_cart(product_name["product_name"][0])

            # click on cart button 
            self.cf.click_element(By.XPATH, productPageLocator.cart_button)

            # now validate product in cart
            product_validation_element = self.obj_cartPage.validate_product_in_cart(product_name["product_name"][0])
            self.assertTrue(product_validation_element,'product is not added to cart')

            # click on checkout button
            self.cf.click_element(By.XPATH, cartPageLocator.checkout_button)

            # verify that checkout information page is visible
            payment_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.checkout_info_page)
            self.assertTrue(payment_element,"chekout information page is not visible")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_10_verify_checkout_with_empty_details(self):
        '''Test Case 10: checkout with empty details '''
        try:

            # login page verification
            self.assertEqual(self.site, self.page.url ,'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'login is not successfull')

            # add product to cart 
            product_name = TEST_DATA_2["add_to_cart"]
            self.obj_productPage.add_to_cart(product_name["product_name"][0])

            # click on cart button 
            self.cf.click_element(By.XPATH, productPageLocator.cart_button)

            # now validate product in cart
            product_validation_element = self.obj_cartPage.validate_product_in_cart(product_name["product_name"][0])
            self.assertTrue(product_validation_element,'product is not added to cart')

            # click on checkout button
            self.cf.click_element(By.XPATH, cartPageLocator.checkout_button)

            # verify that checkout information page is visible
            payment_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.checkout_info_page)
            self.assertTrue(payment_element,"chekout information page is not visible")

            # click on continue button
            self.cf.click_element(By.XPATH, paymentPageLocator.continue_button_payment)

            # Verify error message is shown
            error_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.error_message)
            self.assertTrue(error_element,"there is all fields are filled correctly")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_11_verify_checkout_with_correct_details(self):
        '''Test Case 11: checkout with correct details '''
        try:

            # login page verification
            self.assertEqual(self.site, self.page.url ,'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'login is not successfull')

            # add product to cart 
            product_name = TEST_DATA_2["add_to_cart"]
            self.obj_productPage.add_to_cart(product_name["product_name"][0:3])

            # click on cart button 
            self.cf.click_element(By.XPATH, productPageLocator.cart_button)

            # now validate product in cart
            product_validation_element = self.obj_cartPage.validate_product_in_cart(product_name["product_name"][0:3])
            self.assertTrue(product_validation_element,'product is not added to cart')

            # click on checkout button
            self.cf.click_element(By.XPATH, cartPageLocator.checkout_button)

            # verify that checkout information page is visible
            payment_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.checkout_info_page)
            self.assertTrue(payment_element,"chekout information page is not visible")

            # fill the checkout details
            info = TEST_DATA_2["checkout_details"]
            self.obj_paymentPage.user_checkout_input(info["first_name"],info["last_name"],info["postal_code"])

            # click on continue button
            self.cf.click_element(By.XPATH, paymentPageLocator.continue_button_payment)

            # verify total price in respect of product
            total_element = self.obj_paymentPage.verify_price_quantity_total()
            self.assertTrue(total_element,"there is total price not match with product")

            # click on finish button
            self.cf.click_element(By.XPATH, paymentPageLocator.finish_button)

            # Verify order success message
            success_element = self.cf.is_element_visible(By.XPATH, paymentPageLocator.success_message)
            self.assertTrue(success_element,"order is not placed successfully")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise