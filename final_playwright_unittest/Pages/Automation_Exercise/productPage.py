from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
from Shared.locator import By

class productPageLocator:
   
    product_button = "//div[@class='shop-menu pull-right']//a[@href='/products' or normalize-space(text())='Products']"
    product_cards_by_index = "(//div[@class='productinfo text-center'])[{index_no}]"
    product_cards_by_name = "//p[contains(text(),'{product_name}')]//ancestor::div[@class='productinfo text-center']"
    add_to_cart_button_by_index = "(//div[@class='overlay-content'])[{index_no}]//a[contains(text(),'Add to cart')]"
    add_to_cart_button_by_name = "//div[@class='overlay-content']//p[contains(text(),'{product_name}')]//following-sibling::a[contains(text(),'Add to cart')]"
    continue_shopping_button = "//button[@class='btn btn-success close-modal btn-block' and contains(text(),'Continue Shopping')]"
    view_cart_button = "//button[@class='btn btn-success close-modal btn-block' and contains(text(),'Continue Shopping')]//ancestor::div[@class='modal-footer']//preceding-sibling::div[@class='modal-body']//a[@href='/view_cart']"
    category_section_header = "//div[@class='left-sidebar']//h2[text()='Category']"
    main_category_toggle = "//div[@id='accordian']//a[@href='#{category_name}' and contains(normalize-space(.), '{category_name}')]"
    sub_category_link = "//div[@id='{category_name}']//a[contains(normalize-space(.),'{sub_category_name}')]"
    category_page_header = "//h2[@class='title text-center' and contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '{header_text}')]"
    product_page_text = "//section//h2[text()='All Products']"
    all_product = "//section//div[@class='col-sm-4']"
    view_product_button = "//section//div[@class='col-sm-4']//a[@href='/product_details/{product_no}']"
    product_detail_page_check = "//div[@class='product-details']//div[@class='product-information']//button"
    product_name = "//div[@class='product-information']//h2[contains(text(),.)]"
    product_category = "//div[@class='product-information']//p[contains(text(),.)]"
    product_price = "//div[@class='product-information']//span//span[contains(text(),'Rs.')]"
    product_availability = "//div[@class='product-information']//p//b[text()='Availability:']"
    product_condition = "//div[@class='product-information']//p//b[text()='Condition:']"
    product_brand = "//div[@class='product-information']//p//b[text()='Brand:']"
    search_box = "//input[@id='search_product']"
    search_button = "//button[@id='submit_search']"
    searched_products_text = "//h2[text()='Searched Products']"
    searched_product_cards = "//div[@class='product-image-wrapper']"
    searched_product_name = "//div[@class='product-information']//h2"
    searched_product_category = "//div[@class='product-information']//p[contains(text(),'Category')]"
    all_product_view_page_button = "//div[@class='features_items']//div[@class='choose']//a[text()='View Product']"
    quantity_input = "//input[@id='quantity']"
    add_to_cart_btn = "//button[contains(@class,'cart')]" 
    brand_section_header = "//div[@class='left-sidebar']//h2[normalize-space()='Brands']"
    brand_link_by_name = "//div[@class='brands-name']//a[contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '{brand_name}')]"
    # brand_page_header = "//h2[@class='title text-center' and contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '{brand_name} PRODUCTS')]"
    brand_page_header = "//h2[@class='title text-center' and contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'BRAND - {brand_name} PRODUCTS')]"
    brand_products = "//div[@class='features_items']//div[@class='product-image-wrapper']"
    # brand_product = "(//div[@class='features_items']//div[@class='product-image-wrapper'])[1]"
    write_your_review_text = "//a[@href='#reviews' and text()='Write Your Review']"
    review_name_input = "//input[@id='name']"
    review_email_input = "//input[@id='email']"
    review_textarea = "//textarea[@id='review']"
    review_submit_button = "//button[@id='button-review' or text()='Submit']"
    review_success_message = "//span[contains(text(),'Thank you for your review.')]"
    # product_cards = "//div[@class='product-image-wrapper']"
    # product_name_in_card = ".//div[@class='productinfo text-center']//h2"
    # product_link_in_card = ".//div[@class='choose']//a"
    # searched_product_category = "//div[@class='product-information']//p"




class productPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
                  

    # def click_button(self,value):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, value)      

    
    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)   

    def all_product_is_visible(self):
        '''checks that all product from product page is visible or not'''
        product_element = self.cf.locate_elements(By.XPATH, productPageLocator.all_product)
        if len(product_element) >= 1:
            return True
        return False
    
    def click_on_product(self,product_no):
        '''click on particular product'''
        self.cf.click_element(By.XPATH,productPageLocator.view_product_button.format(product_no=str(product_no)) )

    def search_product(self, keyword):
        '''take input of keyword for searching product'''
        self.cf.send_text(keyword, By.XPATH, productPageLocator.search_box)
        self.cf.click_element(By.XPATH, productPageLocator.search_button)

    def validate_searched_products(self, data):
        '''validate product that given data is matches to the given result of regarding that data'''
        products = self.cf.locate_elements(By.XPATH, productPageLocator.all_product_view_page_button)
        for index in range(len(products)):
            current = self.cf.locate_elements(By.XPATH, productPageLocator.all_product_view_page_button)[index]
            # self.cf.scroll_to_element(current)
            current.click()
            name = self.cf.locate_element(By.XPATH, productPageLocator.searched_product_name).text_content()
            category = self.cf.locate_element(By.XPATH, productPageLocator.searched_product_category).text_content()
            if data.lower() not in name.lower() and data.lower() not in category.lower():
                return False
            self.page.go_back()
            
        return True


    def add_product_to_cart_by_index(self, index_no):
        '''add product to the cart using index'''
        hover_xpath = productPageLocator.product_cards_by_index.format(index_no=index_no)
        add_to_cart_xpath = productPageLocator.add_to_cart_button_by_index.format(index_no=index_no)

        self.cf.hover_and_click(By.XPATH, hover_xpath, By.XPATH, add_to_cart_xpath)

    def add_product_to_cart_by_name(self, product_name):
        '''add product to the cart using name of product'''
        hover_xpath = productPageLocator.product_cards_by_name.format(product_name=product_name)
        add_to_cart_xpath = productPageLocator.add_to_cart_button_by_name.format(product_name=product_name)

        self.cf.hover_and_click(By.XPATH, hover_xpath, By.XPATH, add_to_cart_xpath)

    def set_quantity(self, quantity):
        '''set quantity of particular product'''
        self.cf.send_text(str(quantity), By.XPATH, productPageLocator.quantity_input)        

    def select_category(self, main_category, sub_category):
        '''select sub category of product from main category'''
        self.cf.click_element(By.XPATH, productPageLocator.main_category_toggle.format(category_name=main_category))
        self.cf.click_element(By.XPATH, productPageLocator.sub_category_link.format(category_name=main_category, sub_category_name=sub_category))

    def is_category_page_displayed(self, header_text):
        '''checks that category page is visible or not'''
        return self.cf.is_element_visible(By.XPATH, productPageLocator.category_page_header.format(header_text=header_text.upper()))

    def submit_review(self, name, email, review_text):
        '''take input of name, email and review text then submit it'''
        self.cf.send_text(name, By.XPATH, productPageLocator.review_name_input)
        self.cf.send_text(email, By.XPATH, productPageLocator.review_email_input)
        self.cf.send_text(review_text, By.XPATH, productPageLocator.review_textarea)
        self.cf.click_element(By.XPATH, productPageLocator.review_submit_button)




    
