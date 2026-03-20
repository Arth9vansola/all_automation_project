# yiberet211@hopesx.com
# kalolkaspiderman

from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException

class contactUsPageLocator:
   
    contact_us_button = "//div[contains(@class,'shop-menu pull-right')]//a[contains(text(),'Contact us')]"
    get_in_touch_text = "//div[contains(@id,'contact-page')]//h2[text()='Get In Touch']"
    contact_us_name = "//form[contains(@id,'contact-us-form')]//input[@placeholder='Name']"
    contact_us_email = "//form[contains(@id,'contact-us-form')]//input[@placeholder='Email']"
    contact_us_subject = "//form[contains(@id,'contact-us-form')]//input[@placeholder='Subject']"
    contact_us_message = "//form[contains(@id,'contact-us-form')]//textarea[@placeholder='Your Message Here']"
    contact_us_file_upload = "//form[contains(@id,'contact-us-form')]//input[contains(@type,'file')]"
    contact_us_submit = "//form[contains(@id,'contact-us-form')]//input[contains(@name,'submit')]"
    success_message = "//div[contains(@class,'status alert alert-success') and contains(text(),'Success! Your details have been submitted successfully.')]"
    home_page_button = "//div[contains(@id,'form-section')]//span[contains(text(),'Home')]"
    file_path = r"C:\Users\TNET17\Downloads\POM notes.pdf"
    # file_path = r"C:\Users\arthv\Downloads\DSA Learning Roadmap for 10 LPA Company Placement.pdf"
    

class contactUsPage:

    def __init__(self,driver):
        self.driver = driver
        self.cf = commonfunctions(self.driver)  
               
   
    # it checks the user input is properly given or not
    def contact_us_input(self,name, email_address, subject, message):
        '''take input of name, email address, subject and message'''
        try:
            self.cf.send_text(name, By.XPATH, contactUsPageLocator.contact_us_name)
            self.cf.send_text(email_address, By.XPATH, contactUsPageLocator.contact_us_email)
            self.cf.send_text(subject, By.XPATH, contactUsPageLocator.contact_us_subject)
            self.cf.send_text(message, By.XPATH, contactUsPageLocator.contact_us_message)

        except (NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException) as e:
            raise RuntimeError(f"Error while filling login form: {e}")        

    # def click_button(self,xpath):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, xpath)   

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value) 

    def file_send(self,value,file_path):
        '''upload the file based on file path'''
        self.cf.file_upload(By.XPATH,value,file_path)             





