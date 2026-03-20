# from Shared.TestAssert import TestAssert
# from Shared.commonfunctions import commonfunctions
# from Shared.locator import By
# import pytest

# # @pytest.mark.usefixtures("sauce_products_object")
# class TestTab(TestAssert,commonfunctions):
#     site = "https://vinothqaacademy.com/multiple-windows/"
#     # def setUp(self):
#     #     self.site = "https://vinothqaacademy.com/multiple-windows/"
#     #     super().setUp()

#     cf = commonfunctions(page) 
    
#     def test_12_swtich_window(self):
#         self.cf.click_element("get_by_role", "button", name="New Browser Tab")

#         self.cf.switch_tab(1)
#         result = self.cf.is_element_visible(By.XPATH,"//h2[text()='Project Details']")
#         self.assertTrue(result,"page is not visible")
#         self.cf.switch_tab(0)

#         self.cf.click_element("get_by_role", "button", name="New Browser Window")
#         # self.page.wait_for_timeout(2000)
#         self.page.wait_for_load_state()

#     # def test_12_swtich_window(self):
#     #     self.cf.click_element("get_by_role", "button", name="New Browser Tab")
#     #     # self.cf.switch_tab(0)
#     #     self.page = self.cf.switch_tab(self.page,1)
#     #     result = self.cf.is_element_visible(By.XPATH,"//h2[text()='Project Details']")
#     #     self.assertTrue(result,"page is not visible")
#     #     self.page = self.cf.switch_tab(self.page, 0)

#     #     self.cf.click_element("get_by_role", "button", name="New Browser Window")
#     #     # self.page.wait_for_timeout(2000)
#     #     self.page.wait_for_load_state()

# from Shared.TestAssert import TestAssert
# from Shared.commonfunctions import commonfunctions
# from Shared.locator import By
# import pytest


# @pytest.mark.usefixtures("tab_switch")
# class TestTab(TestAssert):

#     site = "https://vinothqaacademy.com/multiple-windows/"

#     # @pytest.fixture(autouse=True)
#     # def init_objects(self, page):
#     #     self.page = page
#     #     self.cf = commonfunctions(self.page)

#     def test_12_swtich_window(self):

#         self.cf.click_element("get_by_role", "button", name="New Browser Tab")

#         self.cf.switch_tab(1)

#         result = self.cf.is_element_visible(By.XPATH,"//h2[text()='Project Details']")
#         self.assertTrue(result,"page is not visible")

#         self.cf.switch_tab(0)

#         self.cf.click_element("get_by_role", "button", name="New Browser Window")

#         self.page.wait_for_load_state()