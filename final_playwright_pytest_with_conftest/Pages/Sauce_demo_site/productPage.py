from Shared.commonfunctions import commonfunctions
from Shared.locator import By


class productPageLocator:
   
    product_page_visible = "//div[@class='inventory_item_description']//div[contains(text(),'Sauce Labs Backpack')]"
    # product_page_visible = "//div[@id='inventory_container']"
    # product_page_visible = "//span[text()='Products']"
    product_view_button = "//div[@class='inventory_item_description']//div[contains(text(),'{product_name}')]"
    description_of_product = "//div[@class='inventory_details']"
    menu_button = "//button[text()='Open Menu']"
    logout_button = "//a[@id='logout_sidebar_link']"
    add_to_cart_button = "//div[text()='{product_name}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button[text()='Add to cart']"
    cart_button = "//a[@class='shopping_cart_link']"
    add_to_cart_in_product_detail = "//button[text()='Add to cart']"
    



class productPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
                     
    def click_button(self,value):
        '''click on particular button'''
        self.cf.click_element(By.XPATH, value)      

    def presence_of_element(self,value):
        '''checks that element is present or not'''
        return self.cf.is_element_visible(By.XPATH, value)      

    def add_to_cart(self,product_name):
        '''add product into the cart'''
        if isinstance(product_name, str):
            self.cf.click_element(By.XPATH,productPageLocator.add_to_cart_button.format(product_name=product_name))
            return

        if isinstance(product_name, list):
            for name in product_name:
                self.cf.click_element(By.XPATH,productPageLocator.add_to_cart_button.format(product_name=name))
            return
        
    def view_product(self,product_name):
        '''view particular product by name'''
        self.cf.click_element(By.XPATH,productPageLocator.product_view_button.format(product_name=product_name))     





