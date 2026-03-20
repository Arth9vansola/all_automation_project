from Shared.commonfunctions import commonfunctions
from Shared.locator import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
from playwright.sync_api import TimeoutError


class paymentPageLocator:
  checkout_info_page = "//div[@class='checkout_info']" 
  continue_button_payment = "//input[@id='continue']"  
  error_message = "//div[@class='error-message-container error']"
  first_name = "//input[@id='first-name']"
  last_name = "//input[@id='last-name']"
  postal_code = "//input[@id='postal-code']"
  finish_button = "//button[text()='Finish']"
  success_message = "//h2[text()='Thank you for your order!']"
  get_items_in_checked = "//div[@class='cart_item']"
  product_price = "(//div[@class='inventory_item_price'])[{index_no}]"
  product_qunt = "(//div[@class='cart_quantity'])[{index_no}]"
  tax_price = "//div[@class='summary_tax_label']"
  total_price = "//div[@class='summary_total_label']"

    
class paymentPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
                     
    def click_button(self,value):
        '''click on particular product'''
        self.cf.click_element(By.XPATH, value)      

    def presence_of_element(self,value):
        '''checks that element is present or not'''
        return self.cf.is_element_visible(By.XPATH, value)

    def user_checkout_input(self,first_name, last_name, postal_code):
      '''take user input firstName, lastName, postalCode'''
      try:
          self.cf.send_text(first_name, By.XPATH, paymentPageLocator.first_name)
          self.cf.send_text(last_name, By.XPATH, paymentPageLocator.last_name)
          self.cf.send_text(postal_code, By.XPATH, paymentPageLocator.postal_code)
      except TimeoutError as e:
          raise RuntimeError(f"Error while filling login form: {e}")   

    def get_checked_items(self):
        '''get all item of checkout page'''
        return self.cf.locate_elements(By.XPATH,paymentPageLocator.get_items_in_checked)       

    def verify_price_quantity_total(self):
        '''compare the (quantity*price) + tax = total value'''
        items = self.get_checked_items()
        total_price = []
 
        tax = self.cf.locate_element(By.XPATH, paymentPageLocator.tax_price).text_content()
        total = self.cf.locate_element(By.XPATH, paymentPageLocator.total_price).text_content()
        tax_value = float(tax.replace("Tax: $","").strip())
        total_value = float(total.replace("Total: $", "").strip())

        for index_no in range(1, len(items) + 1):

            price_xpath = paymentPageLocator.product_price.format(index_no = index_no)
            qty_xpath = paymentPageLocator.product_qunt.format(index_no = index_no)

            price = self.cf.locate_element(By.XPATH, price_xpath).text_content()
            qty = self.cf.locate_element(By.XPATH, qty_xpath).text_content()
            
            price_value = float(price.replace("$", "").strip())
            qty_value = int(qty.strip())

            total_price.append(price_value * qty_value)

        if sum(total_price) + tax_value != total_value:
            return False
        else:
            return True





