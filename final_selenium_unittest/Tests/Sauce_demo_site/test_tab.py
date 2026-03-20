from Shared.webdriverbase import webdriverbase
from Shared.commonfunctions import commonfunctions
from selenium.webdriver.common.by import By


class TestTab(webdriverbase):

    def setUp(self):
        self.site = "https://vinothqaacademy.com/multiple-windows/"
        super().setUp()

        self.cf = commonfunctions(self.driver) 
    
    # def test_12_swtich_window(self):
    #     self.cf.click_element("get_by_role", "button", name="New Browser Tab")

    #     self.cf.switch_tab(1)
    #     result = self.cf.is_element_visible(By.XPATH,"//h2[text()='Project Details']")
    #     self.assertTrue(result,"page is not visible")
    #     self.cf.switch_tab(0)

    #     self.cf.click_element("get_by_role", "button", name="New Browser Window")
    #     # self.driver.wait_for_timeout(2000)
    #     self.driver.wait_for_load_state()

    # def test_12_swtich_window(self):
    #     self.cf.click_element("get_by_role", "button", name="New Browser Tab")
    #     # self.cf.switch_tab(0)
    #     self.driver = self.cf.switch_tab(self.driver,1)
    #     result = self.cf.is_element_visible(By.XPATH,"//h2[text()='Project Details']")
    #     self.assertTrue(result,"page is not visible")
    #     self.driver = self.cf.switch_tab(self.driver, 0)

    #     self.cf.click_element("get_by_role", "button", name="New Browser Window")
    #     # self.driver.wait_for_timeout(2000)
    #     self.driver.wait_for_load_state()

    