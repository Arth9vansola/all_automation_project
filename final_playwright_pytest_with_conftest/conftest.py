import pytest
import os
from playwright.sync_api import sync_playwright, Page

from Pages.Automation_Exercise.registerPage import registerPage as AutoRegisterPage
from Pages.Automation_Exercise.loginPage import loginPage as AutoLoginPage
from Pages.Automation_Exercise.cartPage import cartPage as AutoCartPage
from Pages.Automation_Exercise.contactUsPage import contactUsPage as AutoContactUsPage
from Pages.Automation_Exercise.homePage import homePage as AutoHomePage
from Pages.Automation_Exercise.paymentPage import paymentPage as AutoPaymentPage
from Pages.Automation_Exercise.testCasePage import testCasePage as AutoTestCasePage
from Pages.Automation_Exercise.productPage import productPage as AutoProductPage
from Pages.Sauce_demo_site.cartPage import cartPage as SauceCartPage
from Pages.Sauce_demo_site.loginPage import loginPage as SauceLoginPage
from Pages.Sauce_demo_site.paymentPage import paymentPage as SaucePaymentPage
from Pages.Sauce_demo_site.productPage import productPage as SauceProductPage

from Shared.commonfunctions import commonfunctions
from datetime import datetime

from xdist.scheduler.load import LoadScheduling


class CustomScheduler(LoadScheduling):

    def schedule(self):

        assert self.collection_is_completed

        if not self._check_nodes_have_same_collection():
            return

        # get test collection
        self.collection = next(iter(self.node2collection.values()))

        # split tests based on folder
        automation_tests = []
        saucedemo_tests = []

        for i, test in enumerate(self.collection):

            if "Automation_Exercise" in test:
                automation_tests.append(i)

            elif "Sauce_demo_site" in test:
                saucedemo_tests.append(i)

        nodes = self.nodes

        if len(nodes) >= 2:

            gw0 = nodes[0]
            gw1 = nodes[1]

            self.node2pending[gw0].extend(automation_tests)
            self.node2pending[gw1].extend(saucedemo_tests)

            gw0.send_runtest_some(automation_tests)
            gw1.send_runtest_some(saucedemo_tests)


def pytest_xdist_make_scheduler(config, log):
    return CustomScheduler(config, log)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if item.get_closest_marker("Automation"):
            report.site_label = "AUTOMATION SITE"
        elif item.get_closest_marker("SauceDemo"):
            report.site_label = "SAUCE DEMO SITE"
        else:
            report.site_label = "GENERAL"

def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Site Category</th>")

def pytest_html_results_table_row(report, cells):
    label = getattr(report, "site_label", "N/A")
    cells.insert(1, f"<td>{label}</td>")

def pytest_html_report_title(report):
    report.title = "Master Automation & SauceDemo Report"

def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"reports/report_{timestamp}.html"

    config.option.htmlpath = report_file


@pytest.fixture(scope="session")
def playwright_instance():

    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture(scope="function")
def page(request, playwright_instance):

    browser = playwright_instance.chromium.launch(
        headless=False,
        args=["--start-maximized"],
        executable_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        slow_mo=350
    )

    context = browser.new_context(
        no_viewport=True,
        accept_downloads=True
    )

    context.set_default_timeout(120000)

    page: Page = context.new_page()


    # if request.node.get_closest_marker("Automation"):
    #     site = "https://automationexercise.com/"
    # elif request.node.get_closest_marker("SauceDemo"):
    #     site = "https://www.saucedemo.com/"
    # else:
    #     raise Exception("Test must have Automation or SauceDemo marker")



    download_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_path, exist_ok=True)

    request.cls.download_path = download_path
    # request.cls.page = page

    site = getattr(request.cls, "site", None)

    page.goto(site)

    yield page

    page.close()
    context.close()
    browser.close()


@pytest.fixture
def auto_auth_object(request,page):
    
    request.cls.page = page
    request.cls.obj_registerPage = AutoRegisterPage(page)
    request.cls.obj_loginPage = AutoLoginPage(page)
    request.cls.cf = commonfunctions(page)

    yield

@pytest.fixture
def auto_cart_object(request,page):

    request.cls.page = page
    request.cls.obj_registerPage = AutoRegisterPage(page)
    request.cls.obj_loginPage = AutoLoginPage(page)
    request.cls.obj_productPage = AutoProductPage(page)
    request.cls.obj_homePage = AutoHomePage(page)
    request.cls.obj_cartPage = AutoCartPage(page)
    request.cls.cf = commonfunctions(page)

    yield

@pytest.fixture
def auto_contact_test_object(request,page):

    request.cls.page = page
    request.cls.obj_contactUsPage = AutoContactUsPage(page)
    request.cls.obj_testCasePage = AutoTestCasePage(page)
    request.cls.cf = commonfunctions(page)

    yield

@pytest.fixture
def auto_order_object(request,page):

    request.cls.page = page
    request.cls.obj_registerPage = AutoRegisterPage(page)
    request.cls.obj_loginPage = AutoLoginPage(page)
    request.cls.obj_productPage = AutoProductPage(page)
    request.cls.obj_homePage = AutoHomePage(page)
    request.cls.obj_cartPage = AutoCartPage(page)
    request.cls.obj_paymentPage = AutoPaymentPage(page)
    request.cls.cf = commonfunctions(page)

    yield

@pytest.fixture
def auto_product_object(request,page):

    request.cls.page = page
    request.cls.obj_productPage = AutoProductPage(page)
    request.cls.cf = commonfunctions(page)

    yield

@pytest.fixture
def auto_subscription_object(request,page):

    request.cls.page = page
    request.cls.obj_homePage = AutoHomePage(page)
    request.cls.obj_cartPage = AutoCartPage(page)
    request.cls.cf = commonfunctions(page)

    yield    

@pytest.fixture
def auto_ui_scroll_object(request,page):

    request.cls.page = page
    request.cls.obj_homePage = AutoHomePage(page)
    request.cls.cf = commonfunctions(page)

    yield        

@pytest.fixture
def sauce_auth_object(request,page):

    request.cls.page = page
    request.cls.obj_loginPage = SauceLoginPage(page)
    request.cls.obj_productPage = SauceProductPage(page)
    request.cls.cf = commonfunctions(page)

    yield    

@pytest.fixture
def sauce_cart_object(request,page):

    request.cls.page = page
    request.cls.obj_loginPage = SauceLoginPage(page)
    request.cls.obj_productPage = SauceProductPage(page)
    request.cls.obj_cartPage = SauceCartPage(page)
    request.cls.cf = commonfunctions(page)

    yield    

@pytest.fixture
def sauce_order_object(request,page):

    request.cls.page = page
    request.cls.obj_loginPage = SauceLoginPage(page)
    request.cls.obj_productPage = SauceProductPage(page)
    request.cls.obj_cartPage = SauceCartPage(page)
    request.cls.obj_paymentPage = SaucePaymentPage(page)
    request.cls.cf = commonfunctions(page)

    yield    

@pytest.fixture
def sauce_products_object(request,page):

    request.cls.page = page                     
    request.cls.obj_loginPage = SauceLoginPage(page)
    request.cls.obj_productPage = SauceProductPage(page)
    request.cls.obj_cartPage = SauceCartPage(page)
    request.cls.cf = commonfunctions(page)

    yield    

@pytest.fixture
def tab_switch(request,page):
    request.cls.page = page      
    request.cls.cf = commonfunctions(page)     