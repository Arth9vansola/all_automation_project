from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
# from playwright.sync_api import TimeoutError
from Shared.locator import By

class loginPageLocator:
   
    login_signup = "//*[contains(@href,'/login') and contains(text(),' Signup / Login')]"
    logout_button = "//div[contains(@class,'shop-menu pull-right')]//a[@href='/logout' and contains(text(),'Logout')]"
    login_page_text = "//section[@id='form']//h2[text()='Login to your account']"
    email_address = "//form[contains(@action, '/login')]//input[contains(@name,'email')]"
    password = "//form[contains(@action, '/login')]//input[contains(@name,'password')]"
    login_btn = "//form[contains(@action, '/login')]//button[contains(@type,'submit')]"
    username_visible_btn = "//div[@class='shop-menu pull-right']//li//a//i[contains(@class,'fa fa-envelope')]//ancestor::li//following-sibling::li//a[normalize-space(text())='Logged in as']"
    del_acc_btn = "//div[@class='shop-menu pull-right']//li//a//i[contains(@class,'fa fa-envelope')]//ancestor::li//preceding-sibling::li//a[@href='/delete_account']"
    del_acc_text = "//section[@id='form']//h2//b[text()='Account Deleted!']"
    del_acc_continue_btn = "//div[contains(@class,'pull-right')]//a[@class='btn btn-primary' and contains(text(),'Continue')]"
    error_after_password = "//form[@action='/login']//input[@type='password']//following-sibling::p[contains(text(),.)]"



class loginPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
               
   
    # it checks the user input is properly given or not
    def user_login_input(self,user_email_address,user_password):
        '''take input of email address and password'''
        try:
            self.cf.send_text(user_email_address, By.XPATH, loginPageLocator.email_address)
            self.cf.send_text(user_password, By.XPATH, loginPageLocator.password)
        except Exception:
            raise    

    # def click_button(self,value):
    #     '''click on particular element'''
    #     self.cf.click_element(By.XPATH, value)      

    
    # def presence_of_element(self,value):
    #     '''check that element is presen or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)          





