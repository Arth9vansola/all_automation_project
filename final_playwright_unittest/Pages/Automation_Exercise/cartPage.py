import time
from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
from Shared.locator import By


class cartPageLocator:
   
    # cart_button = "//div[@class='shop-menu pull-right']//a[@href='/view_cart']"
    # cart_button = "//a[contains(text(),'Cart')]"
    # cart_button = "//a[text()=' Cart']"
    cart_visible = "//a[text()='Proceed To Checkout']"
    cart_button = "//ul[@class='nav navbar-nav']//a[@href='/view_cart' and text()=' Cart']"
    cart_rows = "//tr[contains(@id,'product')]"
    cart_rows_name = "//tr[contains(@id,'product')]//td[@class='cart_description']//h4"
    remove_product_button_name = "//tr[contains(@id,'product')]//td[contains(@class,'cart_description')]//a[contains(text(),'{product_name}')]//ancestor::td[@class='cart_description']//following-sibling::td[@class='cart_delete']//a"
    # remove_product_button = "(//tr[contains(@id,'product')]//a[@class='cart_quantity_delete'])[{index_no}]"
    remove_product_button = "//a[contains(text(),'{product_name}')]//ancestor::td[@class='cart_description']//following-sibling::td[@class='cart_delete']//a"
    empty_cart_text = "//b[text()='Cart is empty!']"
    product_price = "(//tr[contains(@id,'product')]//td[@class='cart_price']/p)[{index_no}]"
    product_quantity = "(//tr[contains(@id,'product')]//td[@class='cart_quantity']/button)[{index_no}]"
    product_total = "(//tr[contains(@id,'product')]//td[@class='cart_total']/p)[{index_no}]"
    email_box = "//input[@id='susbscribe_email']"
    subscription_text = "//footer[@id='footer']//h2[text()='Subscription']"
    arrow_button = "//footer[@id='footer']//button[@id='subscribe']"
    success_message = "//div[@id='success-subscribe']//div[text()='You have been successfully subscribed!']"
    proceed_to_checkout = "//a[contains(text(),'Proceed To Checkout')]"
    register_login_button = "//div[@class='modal-content']//a[@href='/login' or text()='Register/Login']"
    address_details_text = "//section[@id='cart_items']//h2[text()='Address Details']"
    review_order_text = "//section[@id='cart_items']//h2[text()='Review Your Order']"
    comment_textarea = "//section[@id='cart_items']//textarea[@name='message']"
    place_order_button = "//section[@id='cart_items']//a[text()='Place Order']"        
    delivery_address_block = "//ul[@id='address_delivery']"
    billing_address_block = "//ul[@id='address_invoice']"

class cartPage:

  def __init__(self,page):
      self.page = page
      self.cf = commonfunctions(self.page)  
                
#   def click_button(self,value):
#       '''click on particular button'''
#       self.cf.click_element(By.XPATH,value)      
  
#   def presence_of_element(self,value):
#       '''checks that element is present or not'''
#       return self.cf.is_element_visible(By.XPATH, value)   

  def email_input(self,email_address):
      '''takes email input'''
      self.cf.send_text(email_address,By.XPATH,cartPageLocator.email_box)

  def scroll_to_footer(self):
      '''scroll from top to the footer'''
      # element = self.cf.locate_element(By.XPATH,cartPageLocator.email_box)
      # self.cf.scroll_to_element(element)    
      self.cf.scroll_to_element(By.XPATH,cartPageLocator.email_box)      

  def get_cart_items(self):
      '''get that how many items in cart'''
      return self.cf.locate_elements(By.XPATH, cartPageLocator.cart_rows)

  # def verify_products_added(self, expected_count):
  #     '''checks that added product count and actual product count in cart is same or not'''
  #     for _ in range(2):
  #         items = self.cf.locate_elements(By.XPATH, cartPageLocator.cart_rows)

  #         if len(items) == expected_count:
  #             return True

  #         if expected_count == 0 and self.cf.is_element_visible(By.XPATH, cartPageLocator.empty_cart_text):
  #             return True

  #     return False
  

  def validate_product_in_cart(self, product_name):
    '''check that given input product is same as given output product by cart'''
    product_elements = self.cf.locate_elements(By.XPATH, cartPageLocator.cart_rows_name)

    product_names = [element.text_content().strip() for element in product_elements]

    if isinstance(product_name, str):
        return product_name in product_names

    if isinstance(product_name, list):
        return all(name in product_names for name in product_name)

    return False

  def verify_price_quantity_total(self):
      '''chekcks that price and quantity of product is actually equal to the original price or not'''
      items = self.get_cart_items()

      for index_no in range(1, len(items) + 1):

          price_xpath = cartPageLocator.product_price.format(index_no = index_no)
          qty_xpath = cartPageLocator.product_quantity.format(index_no = index_no)
          total_xpath = cartPageLocator.product_total.format(index_no = index_no)

          price = self.cf.locate_element(By.XPATH, price_xpath).text_content()
          qty = self.cf.locate_element(By.XPATH, qty_xpath).text_content()
          total = self.cf.locate_element(By.XPATH, total_xpath).text_content()

          price_value = int(price.replace("Rs.", "").strip())
          qty_value = int(qty.strip())
          total_value = int(total.replace("Rs.", "").strip())

          if price_value * qty_value != total_value:
              return False

      return True
  

  def check_product_quantity(self, expected_quantity):
      '''checks that actual product quantity is same as expected quantity of product'''
      items = self.get_cart_items()

      if not items:
          return False

      qty = self.cf.locate_element(
          By.XPATH,
          cartPageLocator.product_quantity.replace("{index_no}", "1")
          if "{index_no}" in cartPageLocator.product_quantity
          else cartPageLocator.product_quantity
          ).text_content()

      return int(qty.strip()) == expected_quantity
  
  def enter_comment_and_place_order(self, comment):
      '''Enter the comment and click on place order button'''
      self.cf.send_text(comment, By.XPATH, cartPageLocator.comment_textarea)
      self.cf.click_element(By.XPATH, cartPageLocator.place_order_button)


  def remove_product_by_name(self,product_name):
      '''remove the product by name based on there is one product or more than one product'''
      for name in product_name:
          delete_xpath = cartPageLocator.remove_product_button_name.format(product_name=name)
          
          if self.cf.is_element_visible(By.XPATH, cartPageLocator.empty_cart_text):
              break
          
          if not self.cf.is_element_visible(By.XPATH, delete_xpath):
              continue
          
          self.cf.click_element(By.XPATH, delete_xpath)
          self.page.wait_for_timeout(2000)

          
  def get_delivery_address_text(self):
      '''give the get delivery text'''
      return self.cf.locate_element(By.XPATH, cartPageLocator.delivery_address_block).text_content()

  def get_billing_address_text(self):
      '''give the get billing address text'''
      return self.cf.locate_element(By.XPATH, cartPageLocator.billing_address_block).text_content()    

