from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By


class homePageLocator:
   
    home_button = "//div[@class='shop-menu pull-right']//a[@href='/' or normalize-space(text())='Home']"
    view_product_of_home = "//div[@class='productinfo text-center']//p[text()='{product_name}']//ancestor::div[@class='single-products']//following-sibling::div[@class='choose']//a[text()='View Product']"
    product_button = "//div[@class='shop-menu pull-right']//a[@href='/products' or normalize-space(text())='Products']"
    email_box = "//input[@id='susbscribe_email']"
    subscription_text = "//footer[@id='footer']//h2[text()='Subscription']"
    arrow_button = "//footer[@id='footer']//button[@id='subscribe']"
    success_message = "//div[@id='success-subscribe']//div[text()='You have been successfully subscribed!']"
    recommended_items_text = "//h2[@class='title text-center' and contains(translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'RECOMMENDED ITEMS')]"
    recommended_add_to_cart = "(//div[@id='recommended-item-carousel']//a[contains(normalize-space(.),'Add to cart')])[{index_no}]"
    bottom_to_top_arrow_button = "//a[@id='scrollUp']"
    top_banner_text = "//h2[text()='Full-Fledged practice website for Automation Engineers']"

class homePage:

    def __init__(self,driver):
        self.driver = driver
        self.cf = commonfunctions(self.driver)  
                  

    # def click_button(self,xpath):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, xpath)      

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)   

    def email_input(self,email_address):
        '''take input of email address'''
        self.cf.send_text(email_address,By.XPATH,homePageLocator.email_box)

    def scroll_to_footer(self):
        '''scroll from top to footer'''
        element = self.cf.locate_element(By.XPATH,homePageLocator.email_box)
        self.cf.scroll_to_element(element)   

    def click_particular_product_by_name(self,product_name):
        '''click on particular product by name'''
        self.cf.click_element(By.XPATH, homePageLocator.view_product_of_home.format(product_name=product_name)) 
          
    def click_particular_product_by_index(self,index_no):
        '''click on particular product by index'''
        self.cf.click_element(By.XPATH, homePageLocator.recommended_add_to_cart.format(index_no=index_no)) 

    def scroll_to_top(self):
        '''scroll from bottom to top'''
        top_element = self.cf.locate_element(By.XPATH, homePageLocator.home_button)
        self.cf.scroll_to_element(top_element)


         