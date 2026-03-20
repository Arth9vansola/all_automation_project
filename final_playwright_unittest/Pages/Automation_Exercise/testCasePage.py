from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
from Shared.locator import By

class testCasePageLocator:
   
    test_case_button = "//div[@class='shop-menu pull-right']//a[@href='/test_cases' or text()='Test Cases']"
    test_case_text = "//section[@id='form']//h2//b[text()='Test Cases']"

class testCasePage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
                     

    # def click_button(self,value):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, value)      

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)          





