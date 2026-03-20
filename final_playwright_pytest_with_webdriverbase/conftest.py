# import pytest
# from playwright.sync_api import sync_playwright

# from Shared.commonfunctions import commonfunctions
# from Pages.Automation_Exercise.registerPage import registerPage
# from Pages.Automation_Exercise.loginPage import loginPage
# from Pages.Automation_Exercise.cartPage import cartPage
# from Pages.Automation_Exercise.contactUsPage import contactUsPage
# from Pages.Automation_Exercise.homePage import homePage
# from Pages.Automation_Exercise.paymentPage import paymentPage
# from Pages.Automation_Exercise.testCasePage import testCasePage
# from Pages.Automation_Exercise.productPage import productPage
# from Pages.Sauce_demo_site.cartPage import cartPage 


# @pytest.fixture(scope="session")
# def playwright_instance():
#     playwright = sync_playwright().start()
#     yield playwright
#     playwright.stop()



# @pytest.fixture(scope="session")
# def browser(playwright_instance):

#     browser = playwright_instance.chromium.launch(
#         headless=False,
#         slow_mo=350,
#         args=["--start-maximized"],
#         executable_path= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
#     )

#     yield browser
#     browser.close()



# @pytest.fixture(scope="function")
# def context(browser):

#     context = browser.new_context(no_viewport=True)
#     context.set_default_timeout(60000)
#     yield context

#     context.close()



# @pytest.fixture(scope="function")
# def page(context):

#     page = context.new_page()

#     yield page

#     page.close()



# @pytest.fixture(scope="function", autouse=True)
# def setup(request, page):

#     site = getattr(request.cls, "site", None)

    
#     page.goto(site)

#     request.cls.page = page
#     request.cls.cf = commonfunctions(page)

#     request.cls.obj_registerPage = registerPage(page)
#     request.cls.obj_loginPage = loginPage(page)
#     request.cls.obj_cartPage = cartPage(page)
#     request.cls.obj_contactUsPage = contactUsPage(page)
#     request.cls.obj_homePage = homePage(page)
#     request.cls.obj_paymentPage = paymentPage(page)
#     request.cls.obj_productPage = productPage(page)
#     request.cls.obj_testCasePage = testCasePage(page)

#     yield



