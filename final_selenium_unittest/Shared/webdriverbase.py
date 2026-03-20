from selenium import webdriver 
import unittest
from selenium.webdriver.chrome.options import Options 
import os
from Shared.TestAssert import TestAssert

class webdriverbase(TestAssert, unittest.TestCase):
    def setUp(self):
        
        # download_path = os.path.join(os.getcwd(), "downloads")
        # options = Options()
        # options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        # self.driver = webdriver.Chrome(options=options)
        # # self.wait = WebDriverWait(self.driver, 20)
        # # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # website_url = "https://automationexercise.com/"
        # self.driver.get(website_url)

        if "Sauce_demo" in self.id():
            self.website_url = 'https://www.saucedemo.com/'
        elif "Automation" in self.id():
            self.website_url = 'https://automationexercise.com/'
 
        brave_options = Options()

        brave_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

        download_path = os.path.join(os.getcwd(), "downloads")

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        prefs = {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "plugins.always_open_pdf_externally": True,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.credit_card_enabled": False,
            "autofill.profile_enabled": False
        }

        brave_options.add_experimental_option("prefs", prefs)

        brave_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )

        # brave_options.add_argument("--incognito")
        brave_options.add_argument("--disable-popup-blocking")
        brave_options.add_argument("--disable-notifications")
        brave_options.add_argument("--disable-save-password-bubble")
        brave_options.add_argument("--disable-features=AutofillServerCommunication")
        brave_options.add_argument("--disable-autofill-keyboard-accessory-view[8]")

        self.driver = webdriver.Chrome(options=brave_options)

        self.driver.get(self.website_url)
        self.driver.maximize_window()

        self.download_path = download_path

    def tearDown(self):
        self.driver.quit()    

