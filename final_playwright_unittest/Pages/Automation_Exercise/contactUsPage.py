# yiberet211@hopesx.com
# kalolkaspiderman

from Shared.commonfunctions import commonfunctions
# from selenium.webpage.common.by import By
# from selenium.common.exceptions import NoSuchElementException, WebpageException, TimeoutException, StaleElementReferenceException
from playwright.sync_api import TimeoutError
from Shared.locator import By

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
    # file_path = r"C:\Users\TNET17\Downloads\POM notes.pdf"
    # file_path = r"C:\Users\TNET17\Downloads\Playwright for Python_ Step-by-Step Guide (with unittest).pdf"
    file_path = r"docs\Playwright for Python_ Step-by-Step Guide (with unittest).pdf"
    # file_path = r"C:\Users\arthv\Downloads\DSA Learning Roadmap for 10 LPA Company Placement.pdf"
    

class contactUsPage:

    def __init__(self,page):
        self.page = page
        self.cf = commonfunctions(self.page)  
               
   
    # it checks the user input is properly given or not
    def contact_us_input(self,name, email_address, subject, message):
        '''take input of name, email address, subject and message'''
        try:
            self.cf.send_text(name, By.XPATH, contactUsPageLocator.contact_us_name)
            self.cf.send_text(email_address, By.XPATH, contactUsPageLocator.contact_us_email)
            self.cf.send_text(subject, By.XPATH, contactUsPageLocator.contact_us_subject)
            self.cf.send_text(message, By.XPATH, contactUsPageLocator.contact_us_message)

        except TimeoutError as e:
            print(e)        

    # def click_button(self,value):
    #     '''click on particular button'''
    #     self.cf.click_element(By.XPATH, value)   

    # def presence_of_element(self,value):
    #     '''checks that element is present or not'''
    #     return self.cf.is_element_visible(By.XPATH, value) 

    def file_send(self,value,file_path):
        '''upload the file based on file path'''
        self.cf.file_upload(file_path,By.XPATH,value) 


    # def submit_contact_form(self):
    #         self._submit_contact_form_with_retry()

    def submit_contact_form(self, timeout_ms=10000):

        self.page.on("dialog", lambda dialog: dialog.accept())
        self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_submit)

        try:
            self.page.wait_for_selector(
                contactUsPageLocator.success_message,
                state="visible",
                timeout=timeout_ms
            )
            return
        except TimeoutError as e:
            print(e)

        if self.page.url != "https://automationexercise.com/contact_us":
            self.page.go_back()

        # self.page.on("dialog", lambda dialog: dialog.accept())
        self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_submit)
        self.page.wait_for_selector(
            contactUsPageLocator.success_message,
            state="visible",
            timeout=timeout_ms
        )  
     
    # def submit_contact_form(self):
      
    #     url = self.page.url
    #     self.page.once('dialog', lambda dialog:dialog.accept())
    #     self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_submit)
    #     self.page.wait_for_timeout(3000)

    #     while url != self.page.url:
    #         self.page.go_back()
    #         self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_submit)
    #         self.page.wait_for_timeout(3000)

    # def submit_contact_form(self, retries=3):

    #     for attempt in range(1, retries + 1):
    #         try:
    #             print(f"Attempt {attempt}")

    #             with self.page.expect_event("dialog", timeout=5000) as dialog_info:
    #                 self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_submit)

    #             dialog = dialog_info.value
    #             dialog.accept()

    #             self.page.wait_for_selector(
    #                 contactUsPageLocator.success_message,
    #                 state="visible",
    #                 timeout=8000
    #             )

    #             return True

    #         except TimeoutError:
    #             print("Submission failed, retrying...")

    #             if attempt == retries:
    #                 raise Exception("Contact form submission failed after retries.")


                





