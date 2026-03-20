from Shared.commonfunctions import commonfunctions
from Shared.locator import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
from playwright.sync_api import TimeoutError

class loginPageLocator:
   
    username = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    error_message = "//h3[@data-test='error' and contains(text(),'')]"



class loginPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
               
    def user_login_input(self,user_name,user_password):
        '''take input of user name and password'''
        try:
            self.cf.send_text(user_name, By.XPATH, loginPageLocator.username)
            self.cf.send_text(user_password, By.XPATH, loginPageLocator.password)
        except TimeoutError as e:
            raise RuntimeError(f"Error while filling login form: {e}")        

    def click_button(self,value):
        '''click on particular button'''
        self.cf.click_element(By.XPATH, value) 

    def presence_of_element(self,value):
        '''checks that element is present or not'''
        return self.cf.is_element_visible(By.XPATH, value)             

        





