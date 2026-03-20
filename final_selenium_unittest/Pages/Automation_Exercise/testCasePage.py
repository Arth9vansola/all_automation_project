from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By

class testCasePageLocator:
   
    test_case_button = "//div[@class='shop-menu pull-right']//a[@href='/test_cases' or text()='Test Cases']"
    test_case_text = "//section[@id='form']//h2//b[text()='Test Cases']"

class testCasePage:

    def __init__(self,driver):
        self.driver = driver
        self.cf = commonfunctions(self.driver)  
                     

    # def click_button(self,xpath):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, xpath)      

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value)          





