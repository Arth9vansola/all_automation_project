
from data.Automation_Exercise.test_data_1 import TEST_DATA_1

from Pages.Automation_Exercise.contactUsPage import contactUsPage, contactUsPageLocator
from Pages.Automation_Exercise.testCasePage import testCasePage, testCasePageLocator


from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from Shared.locator import By
from Shared.TestAssert import TestAssert
import pytest

class TestContactTestCase(webdriverbase):
    site = "https://automationexercise.com/"

    @pytest.fixture(autouse=True)
    def init_pages(self,setup):

        self.page = setup

        self.obj_contactUsPage = contactUsPage(self.page)
        self.obj_testCasePage = testCasePage(self.page)
        self.cf = commonfunctions(self.page)
        yield

    def test_6_verify_acccount_contact_us(self):
        '''Test Case 6: Contact Us Form'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, contactUsPageLocator.contact_us_button) 
            self.assertTrue(homepage_element,'page is not visible')

            # click on contact us of homepage
            self.cf.click_element(By.XPATH, contactUsPageLocator.contact_us_button)

            # contactUs page visiblity verification
            contact_us_element = self.cf.is_element_visible(By.XPATH, contactUsPageLocator.get_in_touch_text) 
            self.assertTrue(contact_us_element,'contact us page is not visible')

            # enter the details 
            contact = TEST_DATA_1["contact_us"]
            self.obj_contactUsPage.contact_us_input(contact["name"], contact["email"], contact["subject"], contact["message"])

            # upload the file
            self.obj_contactUsPage.file_send(contactUsPageLocator.contact_us_file_upload,contactUsPageLocator.file_path)

            # click on submit button
            # accept = self.obj_contactUsPage.click_button(contactUsPageLocator.contact_us_submit)

            # click on okay button prompted by browser
            # self.cf.handle_accept_alerts(accept)
            self.obj_contactUsPage.submit_contact_form()

            # file is uploaded or not verification
            # success_message_element = self.obj_contactUsPage.presence_of_element(contactUsPageLocator.success_message)
            # self.assertTrue(success_message_element,'file is not uploaded')

            # success_message_element = self.obj_contactUsPage.wait_for_success_message()
            # self.assertTrue(success_message_element,'file is not uploaded')

            # click on home button
            self.cf.click_element(By.XPATH, contactUsPageLocator.home_page_button)

            # verify that landed on homepage
            homepage_element = self.cf.is_element_visible(By.XPATH, contactUsPageLocator.contact_us_button) 
            self.assertTrue(homepage_element,'page is not visible')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise



    def test_7_verify_test_cases_page(self):
        '''Test Case 7: Verify Test Cases Page'''
        try:

            # homepage verification
            homepage_element = self.cf.is_element_visible(By.XPATH, testCasePageLocator.test_case_button)
            self.assertTrue(homepage_element,'page is not visible')

            # click on test case page 
            self.cf.click_element(By.XPATH, testCasePageLocator.test_case_button)

            # test case page visiblity verification
            test_case_element = self.cf.is_element_visible(By.XPATH, testCasePageLocator.test_case_text) 
            self.assertTrue(test_case_element,'test case page is not visible')

        except AssertionError as ae:
            print("Assertion Error:",ae)
            raise

        except Exception as e:
            print("Error Occured:",e)
            raise