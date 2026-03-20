from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By
import time
import os

class paymentPageLocator:
    name_on_card = "//div[@class='payment-information']//input[@name='name_on_card']"
    card_number_path = "//div[@class='payment-information']//input[@name='card_number']"
    cvc_path = "//div[@class='payment-information']//input[@name='cvc']"
    expiry_month_path = "//div[@class='payment-information']//input[@name='expiry_month']"
    expiry_year_path = "//div[@class='payment-information']//input[@name='expiry_year']"
    pay_confirm_button = "//div[@class='payment-information']//button[text()='Pay and Confirm Order']"
    # success_message = "//form[@action='/payment']//div[@class='alert-success alert' or text()='Your order has been placed successfully!']"
    # success_message = "//p[text()='Your order has been placed successfully!']"
    success_message = "//p[text()='Congratulations! Your order has been confirmed!']"
    download_invoice_button = "//section[@id='form']//a[text()='Download Invoice']"
    payment_page_continue_button = "//section[@id='form']//a[text()='Continue']"

class paymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.cf = commonfunctions(self.driver)

    # def click_button(self,xpath):
    #     '''click on particular element'''
    #     self.cf.click_element(By.XPATH, xpath)       

    def enter_payment_details(self,user_name, card_number, cvc, expiry_month,expiry_year):
        '''take input of payment details like userName, cardNumber, cvc, expiry month, expiry year'''
        self.cf.send_text(user_name, By.XPATH, paymentPageLocator.name_on_card)
        self.cf.send_text(card_number, By.XPATH, paymentPageLocator.card_number_path)
        self.cf.send_text(cvc, By.XPATH, paymentPageLocator.cvc_path)
        self.cf.send_text(expiry_month, By.XPATH, paymentPageLocator.expiry_month_path)
        self.cf.send_text(expiry_year, By.XPATH, paymentPageLocator.expiry_year_path)

        self.cf.click_element(By.XPATH, paymentPageLocator.pay_confirm_button)

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)  
    
    def download_invoice(self, download_path):
        '''take download path of particular invoice '''
        for file in os.listdir(download_path):
            if file.endswith(".txt") or file.endswith(".pdf"):
                os.remove(os.path.join(download_path, file))
                
        self.cf.click_element(By.XPATH,paymentPageLocator.download_invoice_button)

        time.sleep(5) 

        files = os.listdir(download_path)

        for file in files:
            if file.endswith(".txt") or file.endswith(".pdf"):
                return True

        return False



