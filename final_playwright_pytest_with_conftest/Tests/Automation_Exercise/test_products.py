# import time
from data.Automation_Exercise.test_data_1 import TEST_DATA_1
from Pages.Automation_Exercise.productPage import productPage, productPageLocator

from Shared.TestAssert import TestAssert
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
import pytest

@pytest.mark.Automation
@pytest.mark.usefixtures("auto_product_object")
class TestProducts(TestAssert):
    site = "https://automationexercise.com/"

    # @pytest.fixture(autouse=True)
    # def init_pages(self,setup):

    #     self.page = setup
    #     self.obj_productPage = productPage(self.page)
    #     self.cf = commonfunctions(self.page)
    #     yield

    def test_8_verify_product_detail_page(self):
        '''Test Case 8: Verify All Products and product detail page'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_button)
            self.assertTrue(homepage_element, 'page is not visible')

            # click on products page 
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # ALL PRODUCTS page visiblity verification
            product_page_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_text) 
            self.assertTrue(product_page_element, 'all products page is not visible')

            # product list visible verification
            products_visible_element = self.obj_productPage.all_product_is_visible()
            self.assertTrue(products_visible_element, 'product list is not visible')

            # click on view product of first product
            self.obj_productPage.click_on_product(TEST_DATA_1["products"]["view_product_index"])  # converted to string then

            # verify that user landed on product detail page
            product_detail_page_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_detail_page_check)
            self.assertTrue(product_detail_page_element, 'user is not landed product detail page')

            # product name is visible or not checking
            product_name_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_name)
            self.assertTrue(product_name_element, 'product name is not visible')

            # product category is visible or not checking
            product_category_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_category)
            self.assertTrue(product_category_element, 'product category is not visible')

            # product price is visible or not checking
            product_price_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_price)
            self.assertTrue(product_price_element, 'product price is not visible')

            # product availability is visible or not checking
            product_availability_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_availability)
            self.assertTrue(product_availability_element, 'product availability is not visible')

            # product condition is visible or not checking
            product_condition_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_condition)
            self.assertTrue(product_condition_element, 'product condition is not visible')

            # product brand is visible or not checking
            product_brand_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_brand)
            self.assertTrue(product_brand_element, 'product brand is not visible')


        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_9_verify_search_product(self):
        '''Test Case 9: Search Product'''
        try:
            
            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_button)
            self.assertTrue(homepage_element, 'page is not visible')

            # click on products page 
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # ALL PRODUCTS page visiblity verification
            product_page_element = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_text) 
            self.assertTrue(product_page_element, 'all products page is not visible')

            # serch for product
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
                        raise


            self.assertTrue(search_ok, 'Search result contains invalid products or did not load')

            # self.obj_productPage.search_product(keyword)

            # # verify SEARCHED PRODUCTS text
            # searched_text = self.obj_productPage.presence_of_element(productPageLocator.searched_products_text)
            # self.assertTrue(searched_text, "'SEARCHED PRODUCTS' not visible")

            # # get searched products
            # products_element = self.obj_productPage.validate_searched_products(keyword)
            # self.assertTrue(products_element,"Search result contains invalid products")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_18_verify_view_category_products(self):
        '''Test Case 18: View Category Products'''
        try:
            
            #  Verify that categories are visible on left side bar
            categories_visible = self.cf.is_element_visible(By.XPATH, productPageLocator.category_section_header)
            self.assertTrue(categories_visible, "categories sidebar is not visible")

            #  Click on any category link under 'Women' category, for example: Dress
            cat1 = TEST_DATA_1["categories"]["first"]
            self.obj_productPage.select_category(cat1["main"], cat1["sub"])

            # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
            women_category_visible = self.obj_productPage.is_category_page_displayed(cat1["header"])
            self.assertTrue(women_category_visible, "Women Tops category page is not visible")

            # Click on any category link under 'Men' category, for example: Tshirts
            cat2 = TEST_DATA_1["categories"]["second"]
            self.obj_productPage.select_category(cat2["main"], cat2["sub"])

            # Verify that category page is displayed and confirm text 'MEN - TOPS PRODUCTS'
            men_category_visible = self.obj_productPage.is_category_page_displayed(cat2["header"])
            self.assertTrue(men_category_visible, "Men Tshirts category page is not visible")

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_19_verify_view_brand_products(self):
        '''Test Case 19: View & Cart Brand Products'''
        try:
            
            # click on  Products page
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # brand sidebar section verification
            brands_visible = self.cf.is_element_visible(By.XPATH, productPageLocator.brand_section_header)
            self.assertTrue(brands_visible, 'Brands sidebar is not visible')

            # click first brand
            brand1 = TEST_DATA_1["brands"]["first"]
            self.cf.click_element(By.XPATH, productPageLocator.brand_link_by_name.format(brand_name=brand1))

            #  Verify that user is navigated to POLO page 
            brand_one_header = self.cf.is_element_visible(By.XPATH, productPageLocator.brand_page_header.format(brand_name=brand1))
            self.assertTrue(brand_one_header, 'Polo brand page not visible')

            # Verify POLO brand products are displayed
            brand_one_products = self.cf.is_element_visible(By.XPATH, productPageLocator.brand_products)
            self.assertTrue(brand_one_products, 'Polo brand products not visible')

            # click another brand
            brand2 = TEST_DATA_1["brands"]["second"]
            self.cf.click_element(By.XPATH, productPageLocator.brand_link_by_name.format(brand_name=brand2))

            #  Verify that user is navigated to H&M page 
            brand_two_header = self.cf.is_element_visible(By.XPATH, productPageLocator.brand_page_header.format(brand_name=brand2))
            self.assertTrue(brand_two_header, 'H&M brand page not visible')

            # Verify H&M brand products are displayed
            brand_two_products = self.cf.is_element_visible(By.XPATH, productPageLocator.brand_products)
            self.assertTrue(brand_two_products, 'H&M brand products not visible')

        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise


    def test_21_verify_add_review_on_product(self):
        '''Test Case 21: Add review on product'''
        try:
            
            # Click on 'Products' button
            self.cf.click_element(By.XPATH, productPageLocator.product_button)

            # Verify user is navigated to ALL PRODUCTS page successfully
            all_products = self.cf.is_element_visible(By.XPATH, productPageLocator.product_page_text)
            self.assertTrue(all_products, 'ALL PRODUCTS page is not visible')

            # Click on first 'View Product' button 
            first_view_product = f"({productPageLocator.all_product_view_page_button})[1]"
            self.cf.click_element(By.XPATH, first_view_product)

            # Verify 'Write Your Review' is visible
            review_title = self.cf.is_element_visible(By.XPATH, productPageLocator.write_your_review_text)
            self.assertTrue(review_title, "'Write Your Review' is not visible")

            # Enter name, email and review and submit
            review = TEST_DATA_1["review"]
            self.obj_productPage.submit_review(review["name"], review["email"], review["text"])

            # Verify success message 'Thank you for your review.'
            success = self.cf.is_element_visible(By.XPATH, productPageLocator.review_success_message)
            self.assertTrue(success, 'Review success message not visible')


        except AssertionError as ae:
            print("Assertion Error:", ae)
            raise
        except Exception as e:
            print("Error Occured:", e)
            raise