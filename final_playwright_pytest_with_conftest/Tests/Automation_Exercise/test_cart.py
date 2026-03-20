from data.Automation_Exercise.test_data_1 import TEST_DATA_1
from Pages.Automation_Exercise.registerPage import registerPage, registerPageLocator
from Pages.Automation_Exercise.loginPage import loginPage, loginPageLocator
from Pages.Automation_Exercise.productPage import productPage, productPageLocator
from Pages.Automation_Exercise.homePage import homePage, homePageLocator
from Pages.Automation_Exercise.cartPage import cartPage, cartPageLocator

from Shared.TestAssert import TestAssert
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
import pytest

@pytest.mark.Automation
@pytest.mark.usefixtures("auto_cart_object")
class TestCart(TestAssert):
    site = "https://automationexercise.com/"

    # @pytest.fixture(autouse=True)
    # def init_pages(self,setup):

    #     self.page = setup

    #     self.obj_registerPage = registerPage(self.page)
    #     self.obj_loginPage = loginPage(self.page)
    #     self.obj_productPage = productPage(self.page)
    #     self.obj_homePage = homePage(self.page)
    #     self.obj_cartPage = cartPage(self.page)
    #     self.cf = commonfunctions(self.page)
    #     yield
 

    def test_12_verify_add_products_in_cart(self):
        '''Test Case 12: Add Products in Cart'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_button)
            self.assertTrue(homepage_element,'page is not visible')

            # click products button
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # Hover over first product and click 'Add to cart'
            # indices = TEST_DATA_1["products"]["cart_add_indices"]
            # self.obj_productPage.add_product_to_cart_by_index(indices[0])
            product_names = TEST_DATA_1["products"]["cart_add_name"]
            self.obj_productPage.add_product_to_cart_by_name(product_names[0])

            # click on continue shopping button
            self.cf.click_element(By.XPATH, productPageLocator.continue_shopping_button)

            # Hover over second product and click 'Add to cart'
            # self.obj_productPage.add_product_to_cart_by_index(indices[1])
            self.obj_productPage.add_product_to_cart_by_name(product_names[1])

            # Click on 'View Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            #  Verify both products are added to Cart
            product_element = self.obj_cartPage.validate_product_in_cart(product_names)
            self.assertTrue(product_element,"product is not added into cart")

            # Verify their prices, quantity and total price
            total_element = self.obj_cartPage.verify_price_quantity_total()
            self.assertTrue(total_element,"price, quantity, total price is not verified")

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise
        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_13_verify_product_quantity_in_cart(self):
        '''Test Case 13: Verify Product quantity in Cart'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.home_button)
            self.assertTrue(homepage_element,'page is not visible')

            # click view product button
            self.obj_homePage.click_particular_product_by_name(TEST_DATA_1["products"]["quantity_product_name"])

            #  Verify product detail is opened
            product_detail_page_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_detail_page_check)
            self.assertTrue(product_detail_page_element,'user is not landed product detail page')

            # increase quantity to 4
            self.obj_productPage.set_quantity(TEST_DATA_1["products"]["quantity"])

            # Click 'Add to cart' button
            self.cf.click_element(By.XPATH, productPageLocator.add_to_cart_btn)

            # Click 'View Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Verify that product is displayed in cart page with exact quantity
            product_quantity_element = self.obj_cartPage.check_product_quantity(TEST_DATA_1["products"]["quantity"])
            self.assertTrue(product_quantity_element,'product is displayed in cart page with not exact quantity')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise
        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_17_verify_remove_products_from_cart(self):
        '''Test Case 17: Remove Products From Cart'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_element, "Homepage not visible")

            # click products button
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # Add product to cart
            names_add = TEST_DATA_1["products"]["cart_add_name"]
            self.obj_productPage.add_product_to_cart_by_name(names_add[0])

            self.cf.click_element(By.XPATH, productPageLocator.continue_shopping_button)

            self.obj_productPage.add_product_to_cart_by_name(names_add[1])

            # click 'Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Cart page verification
            cart_page = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_visible)
            self.assertTrue(cart_page, "Cart page not visible")

            # Click 'X' button corresponding to particular product
            names_remove = TEST_DATA_1["products"]["remove_cart_name"]
            self.obj_cartPage.remove_product_by_name(names_remove)

            # Verify that product is removed from the cart
            empty_element = self.cf.is_element_visible(By.XPATH, cartPageLocator.empty_cart_text)
            self.assertTrue(empty_element,'product is not removed from the cart')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise
        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_22_verify_add_to_cart_from_recommended_items(self):
        '''Test Case 22: Add to cart from Recommended items'''
        try:

            # Homepage visible
            homepage_visible = self.cf.is_element_visible(By.XPATH, homePageLocator.product_button)
            self.assertTrue(homepage_visible, "Homepage is not visible")

            # Scroll to bottom of page
            self.obj_homePage.scroll_to_footer()

            # Verify 'RECOMMENDED ITEMS' are visible
            recommended_visible = self.cf.is_element_visible(By.XPATH, homePageLocator.recommended_items_text)
            self.assertTrue(recommended_visible, "'RECOMMENDED ITEMS' is not visible")

            # Click on 'Add To Cart' on Recommended product
            self.obj_homePage.click_particular_product_by_index(1)

            # Click on 'View Cart' button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # Verify that product is displayed in cart page
            cart_has_product = self.cf.is_element_visible(By.XPATH, cartPageLocator.cart_rows)
            self.assertTrue(cart_has_product, "Product is not displayed in cart")

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise
        except Exception as e:
            print("Error Occured:",e)
            raise


    def test_20_verify_search_products_cart_after_login(self):
        '''Test Case 20: Search Products and Verify Cart After Login'''
        try:

            # click Products page
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            #  Verify user is navigated to ALL PRODUCTS page successfully
            all_products = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_text)
            self.assertTrue(all_products, "ALL PRODUCTS page is not visible")

            # search for product
            keyword = TEST_DATA_1["search"]["keyword"]
            max_attempts = 3
            search_ok = False

            for _ in range(max_attempts):
                self.obj_productPage.search_product(keyword)
                searched_text = self.cf.is_element_visible(By.XPATH, productPageLocator.searched_products_text)
                if searched_text:
                    try:
                        if self.obj_productPage.validate_searched_products(keyword):
                            search_ok = True
                            break
                    except RuntimeError:
                        pass

            self.assertTrue(search_ok, "Search results contain unrelated products or did not load")

            # add first searched products to cart
            names = TEST_DATA_1["products"]["cart_add_name"]
            self.obj_productPage.add_product_to_cart_by_name(names[0])

            # click on continue shopping button
            self.cf.click_element(By.XPATH, productPageLocator.continue_shopping_button)

            # add second searched products to cart
            self.obj_productPage.add_product_to_cart_by_name(names[1])

            # click on view cart button
            self.cf.click_element(By.XPATH, productPageLocator.view_cart_button)

            # verify that products are visible in cart before login
            items_before_login = self.obj_cartPage.validate_product_in_cart(names)
            self.assertTrue(items_before_login, "Products not visible in cart before login")

            # Click 'Signup / Login' button
            self.cf.click_element(By.XPATH, registerPageLocator.login_signup)

            # submit login credentials
            login = TEST_DATA_1["login"]["valid"]
            self.obj_loginPage.user_login_input(login["email"], login["password"])
            self.cf.click_element(By.XPATH, loginPageLocator.login_btn)

            # wait for login success before navigating to cart
            login_ok = self.cf.is_element_visible(By.XPATH, loginPageLocator.username_visible_btn)
            self.assertTrue(login_ok, "Login not successful")

            # click on cart button
            self.cf.click_element(By.XPATH, cartPageLocator.cart_button)

            # verify that products are visible in cart after login
            items_after_login = self.obj_cartPage.validate_product_in_cart(names)
            self.assertTrue(items_after_login, "Products not visible in cart after login")

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise
        except Exception as e:
            print("Error Occured:",e)
            raise