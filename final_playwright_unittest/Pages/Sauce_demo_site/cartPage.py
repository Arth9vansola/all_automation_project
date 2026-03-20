from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
from playwright.sync_api import TimeoutError
from Shared.locator import By

class cartPageLocator:
    product_names = "//div[@class='inventory_item_name']"
    remove_button = "//div[text()='{product_name}']//ancestor::div[@class='cart_item_label']//div[@class='item_pricebar']//button"
    cart_item = "//div[@class='cart_item']"
    continue_shopping_button = "//button[text()='Continue Shopping']"
    checkout_button = "//button[text()='Checkout']"


class cartPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
                  

    # def click_button(self,value):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, value) 

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)   

    def get_cart_items(self):
        '''give that how many product is in cart'''
        return self.cf.locate_elements(By.XPATH,cartPageLocator.product_names)
    
    def validate_product_in_cart(self, product_name):
        '''check that given input product is same as given output product by cart'''
        product_elements = self.cf.locate_elements(By.XPATH, cartPageLocator.product_names)

        product_names = [element.text_content().strip() for element in product_elements]

        if isinstance(product_name, str):
            return product_name in product_names

        if isinstance(product_name, list):
            return all(name in product_names for name in product_name)

        return False
    
    def remove_product(self,product_name):
        '''remove product from the cart'''
        if isinstance(product_name, str):
            self.cf.click_element(By.XPATH,cartPageLocator.remove_button.format(product_name=product_name))
            return

        if isinstance(product_name, list):
            for name in product_name:
                self.cf.click_element(By.XPATH,cartPageLocator.remove_button.format(product_name=name))
            return



        





