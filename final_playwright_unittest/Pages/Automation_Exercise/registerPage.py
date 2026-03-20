import time
from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
from playwright.sync_api import TimeoutError
from Shared.locator import By

class registerPageLocator:
   
    login_signup = "//*[contains(@href,'/login') and contains(text(),' Signup / Login')]"
    signup_text = "//section[@id='form']//h2[contains(text(),'New User Signup!')]"
    Name = "//form[contains(@action, '/signup')]//following::input[contains(@placeholder,'Name')]"
    email_address = "//form[contains(@action, '/signup')]//following::input[contains(@placeholder,'Email Address')]"
    singUp_btn = "//form[contains(@action, '/signup')]//following::button[contains(@type,'submit') and contains(text(),'Signup')]"
    # error_after_email = "//form[@action='/signup']//input[@type='email']//following-sibling::p[contains(text(),.)]"
    error_after_email = "//form[@action='/signup']//input[@type='email']//following-sibling::p[contains(text(),'Email Address already exist!')]"
    acc_info_intro_text = "//div[@class='login-form']//h2//b[contains(text(),'Enter Account Information')]"
    acc_salutation_mr_title = "//form[contains(@action,'/signup')]//div[contains(@class,'radio-inline')]//input[@value='Mr']"
    acc_salutation_mrs_title = "//form[contains(@action,'/signup')]//div[contains(@class,'radio-inline')]//input[@value='Mrs']"
    acc_name = "//form[contains(@action,'/signup')]//descendant::input[@id='name']"
    acc_email = "//form[contains(@action,'/signup')]//descendant::input[@id='email']"
    acc_password = "//form[contains(@action,'/signup')]//descendant::input[@id='password']"
    # acc_dob_days = "//select[contains(@id,'days')]//option[@value="
    # acc_dob_months = "//select[contains(@id,'months')]//option[@value="
    # acc_dob_years = "//select[contains(@id,'years')]//option[@value="
    acc_dob_days = "//div[@class='login-form']//select[@id='days']"
    acc_dob_months = "//div[@class='login-form']//select[@id='months']"
    acc_dob_years = "//div[@class='login-form']//select[@id='years']"
    acc_checkbox_newsletter = "//input[@id='newsletter']//ancestor::div[@id='uniform-newsletter']//following-sibling::label[text()='Sign up for our newsletter!']"
    acc_checkbox_special_offer = "//input[@id='optin']//ancestor::div[@id='uniform-optin']//following-sibling::label[text()='Receive special offers from our partners!']"
    address_info_first_name = "//form[@action='/signup']//following::p//input[@id='first_name']"
    address_info_last_name = "//form[@action='/signup']//following::p//input[@id='last_name']"
    address_info_company = "//form[@action='/signup']//following::p//input[@id='company']"
    country_name = "//select[@id='country']"
    address_info_address = "//form[@action='/signup']//following::p//input[@id='address1']" 
    address_info_address2 = "//form[@action='/signup']//following::p//input[@id='address2']"
    address_info_country = "//form[@action='/signup']//following::p//select//option[@value='{country_name}']"
    address_info_state = "//form[@action='/signup']//following::p//input[@id='state']"
    address_info_city = "//form[@action='/signup']//following::p//input[@id='city']"
    address_info_zipcode = "//form[@action='/signup']//following::p//input[@id='zipcode']"
    address_info_mobile_number = "//form[@action='/signup']//following::p//input[@id='mobile_number']"
    account_created_text = "//section[@id='form']//h2//b[contains(text(),'Account Created')]"
    address_info_create_account_btn = "//form[@action='/signup']//descendant::button[contains(text(),'Create Account')]"
    acc_created_continue_btn = "//a[@class='btn btn-primary' and contains(text(),'Continue')]"
    username_visible_btn = "//div[@class='shop-menu pull-right']//li//a//i[contains(@class,'fa fa-envelope')]//ancestor::li//following-sibling::li//a[normalize-space(text())='Logged in as']"
    del_acc_btn = "//div[@class='shop-menu pull-right']//li//a//i[contains(@class,'fa fa-envelope')]//ancestor::li//preceding-sibling::li//a[@href='/delete_account']"
    deleted_account_text = "//section[@id='form']//h2//b[contains(text(),'Account Deleted!')]"
    del_acc_continue_btn = "//div[contains(@class,'pull-right')]//a[@class='btn btn-primary' and contains(text(),'Continue')]"
    

class registerPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  

    def generate_unique_email(self, email_strategy):
        '''it genereates unique emial id'''
        try:
            prefix = email_strategy.get("prefix", "user_")
            domain = email_strategy.get("domain", "@example.com")
            return f"{prefix}{int(time.time())}{domain}"
        except Exception:
            raise 

    def create_account(self, profile, email_strategy):
        '''it creates new account every time when we call and return emali id and password'''
        try:
            email = self.generate_unique_email(email_strategy)

            self.user_signup_input(profile["name"], email)
            self.cf.click_element(By.XPATH, registerPageLocator.singUp_btn)

            self.fill_acc_form_details(profile["title"], profile["password"], profile["dob"])

            cb = profile["checkboxes"]
            self.check_the_box(cb["newsletter"],cb["special_offer"])

            addr = profile["address"]
            self.fill_address_form_details(
                addr["first_name"],
                addr["last_name"],
                addr["company"],
                addr["address1"],
                addr["address2"],
                addr["country"],
                addr["state"],
                addr["city"],
                addr["zipcode"],
                addr["mobile"],
            )

            self.cf.click_element(By.XPATH, registerPageLocator.address_info_create_account_btn)

            if not self.cf.is_element_visible(By.XPATH, registerPageLocator.account_created_text):
                raise RuntimeError("Account not created")

            self.cf.click_element(By.XPATH, registerPageLocator.acc_created_continue_btn)

            if not self.cf.is_element_visible(By.XPATH, registerPageLocator.username_visible_btn):
                raise RuntimeError("User not logged in")

            return email, profile["password"]
        except Exception:
            raise
         
    def user_signup_input(self,user_name,user_email_address):
        '''user insert user name and email addresss'''
        try:
            self.cf.send_text(user_name, By.XPATH, registerPageLocator.Name)
            self.cf.send_text(user_email_address, By.XPATH, registerPageLocator.email_address)
        except Exception:
            raise      
     
        
    def fill_acc_form_details(self,title,password,dob):
        '''user inserts title: Mr or Mrs. , password and date of birth'''
        try:
            self.cf.click_element(By.XPATH, registerPageLocator.acc_salutation_mr_title) if title == 'Mr' else self.cf.click_element(By.XPATH, registerPageLocator.acc_salutation_mrs_title)
            self.cf.send_text(password, By.XPATH, registerPageLocator.acc_password)
            self.cf.handle_dropdown(By.XPATH, registerPageLocator.acc_dob_days, dob[0:1])
            self.cf.handle_dropdown(By.XPATH, registerPageLocator.acc_dob_months, dob[1:2])
            self.cf.handle_dropdown(By.XPATH, registerPageLocator.acc_dob_years, dob[2:])
        except Exception:
            raise

    def check_the_box(self, newsletter = True, special_offer = True):
        '''check the all checkbox of newsletter and special offer'''
        try:
            if newsletter:
                self.cf.click_element(By.XPATH, registerPageLocator.acc_checkbox_newsletter)
            if special_offer:
                self.cf.click_element(By.XPATH, registerPageLocator.acc_checkbox_special_offer)
        except Exception:
            raise


    def fill_address_form_details(self,first_name,last_name,company,address_one,address_two,country_name,state_name,city_name,zipcode,mobile_number):
        '''take input for firstName, lastName, companyName, first address, second address, countryName, stateName, cityName, zipcode, mobile number'''
        try:
            if not first_name or not last_name:
                raise RuntimeError("First name and Last name are required fields. Please fill them in.")
            self.cf.send_text(first_name, By.XPATH, registerPageLocator.address_info_first_name)
            self.cf.send_text(last_name, By.XPATH, registerPageLocator.address_info_last_name)
            self.cf.send_text(company, By.XPATH, registerPageLocator.address_info_company)
            self.cf.send_text(address_one, By.XPATH, registerPageLocator.address_info_address)
            self.cf.send_text(address_two, By.XPATH, registerPageLocator.address_info_address2)
            self.cf.handle_dropdown(By.XPATH, registerPageLocator.country_name, country_name)
            self.cf.send_text(state_name, By.XPATH, registerPageLocator.address_info_state)
            self.cf.send_text(city_name, By.XPATH, registerPageLocator.address_info_city)
            self.cf.send_text(zipcode, By.XPATH, registerPageLocator.address_info_zipcode)
            self.cf.send_text(mobile_number, By.XPATH, registerPageLocator.address_info_mobile_number)
        except Exception:
            raise

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)
    
    # def click_button(self,value):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, value)    
            
