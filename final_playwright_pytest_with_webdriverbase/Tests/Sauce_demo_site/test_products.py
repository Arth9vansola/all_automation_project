from data.Sauce_demo_site.test_data_2 import TEST_DATA_2

from Pages.Sauce_demo_site.loginPage import loginPage, loginPageLocator
from Pages.Sauce_demo_site.productPage import productPage, productPageLocator
from Pages.Sauce_demo_site.cartPage import cartPage, cartPageLocator

from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
import pytest

class TestProducts(webdriverbase):

    site = 'https://www.saucedemo.com/'

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup
        self.obj_loginPage = loginPage(self.page)
        self.obj_productPage = productPage(self.page)
        self.obj_cartPage = cartPage(self.page)
        self.cf = commonfunctions(self.page)
        yield
    
    def test_5_verify_view_product_details(self):
        '''Test Case 5: view product details'''
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

            # view particular product
            prod = TEST_DATA_2["view_prodcut"]
            self.obj_productPage.view_product(prod["product_name"])

            # verify that view product is visible
            view_product_element = self.cf.is_element_visible(By.XPATH, productPageLocator.description_of_product)
            self.assertTrue(view_product_element,"product detail in description is not present")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_7_verify_view_product_then_add_to_cart(self):
        '''Test Case 7: view product details and then add to cart'''
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

            # view particular product
            prod = TEST_DATA_2["view_prodcut"]
            self.obj_productPage.view_product(prod["product_name"])

            # verify that view product is visible
            view_product_element = self.cf.is_element_visible(By.XPATH, productPageLocator.description_of_product)
            self.assertTrue(view_product_element,"product detail in description is not present")

            # click on add to cart
            self.cf.click_element(By.XPATH, productPageLocator.add_to_cart_in_product_detail)

            # click on cart button 
            self.cf.click_element(By.XPATH, productPageLocator.cart_button)

            # Verify same product name is added to cart
            product_validation_element = self.obj_cartPage.validate_product_in_cart(prod["product_name"])
            self.assertTrue(product_validation_element,'product is not added to cart')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise