import time
from data.Sauce_demo_site.test_data_2 import TEST_DATA_2

from Pages.Sauce_demo_site.loginPage import loginPage, loginPageLocator
from Pages.Sauce_demo_site.productPage import productPage, productPageLocator
from Pages.Sauce_demo_site.cartPage import cartPage, cartPageLocator

from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
import pytest

class TestCart(webdriverbase):

    site = 'https://www.saucedemo.com/'

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup
        self.obj_loginPage = loginPage(self.page)
        self.obj_productPage = productPage(self.page)
        self.obj_cartPage = cartPage(self.page)
        self.cf = commonfunctions(self.page)
        yield
    
    def test_4_verify_add_to_cart(self):
        '''Test Case 4: add product into the cart '''
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

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_6_verify_remove_from_cart(self):
        '''Test Case 6: remove product from the cart '''
        try:

            # login page verification
            self.assertTrue(self.site == self.page.url, 'Homepage is not visible')

            # enter the username and password
            cred = TEST_DATA_2["login_user"]
            self.obj_loginPage.user_login_input(cred["user_name"], cred["password"])

            # click on login
            self.cf.click_element(By.XPATH, loginPageLocator.login_button)

            # verify that login is successfull
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page, 'login is not successfull')

            # add product to cart 
            product_name = TEST_DATA_2["add_to_cart"]
            self.obj_productPage.add_to_cart(product_name["product_name"][0:2])

            # click on cart button 
            self.cf.click_element(By.XPATH, productPageLocator.cart_button)

            # now validate product in cart
            product_validation_element = self.obj_cartPage.validate_product_in_cart(product_name["product_name"][0])
            self.assertTrue(product_validation_element, 'product is not added to cart')

            # remove product from cart
            self.obj_cartPage.remove_product(product_name["product_name"][0:2])

            # verify that product is removed from cart
            removed_element = self.obj_cartPage.get_cart_items()
            self.assertEqual(removed_element, [], 'still there is product in cart')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_8_verify_navigate_back_to_product_page_by_continue_shopping(self):
        '''Test Case 8: navigate back to product page by continue shopping '''
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

            # click on continue shopping button
            self.cf.click_element(By.XPATH, cartPageLocator.continue_shopping_button)

            # Verify user is navigated back to Products page
            product_page = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_visible)
            self.assertTrue(product_page,'product page is not visible')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise