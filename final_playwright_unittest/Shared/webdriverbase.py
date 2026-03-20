from playwright.sync_api import sync_playwright, Page
import unittest
import os
from Shared.TestAssert import TestAssert

class webdriverbase(TestAssert, unittest.TestCase):
    global site

    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        # cls.browser = cls.playwright.chromium.launch(
        #     headless=False, 
        #     args=["--start-maximized", "--disable-popup-blocking"], 
        #     # args=["--start-maximized"], 
        #     executable_path= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        #     slow_mo=500
        #     )
        # cls.context = cls.browser.new_context(
        #     no_viewport=True,
        #     accept_downloads=True
        #     # viewport={"width": 1080, "height": 1080} 
        #     ) 



    def setUp(self):
        # self.p = sync_playwright().start()
        # self.browser = self.p.chromium.launch(headless=False, args=["--start-maximized"], executable_path= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", slow_mo=500)
        self.browser = self.playwright.chromium.launch(
            headless=False, 
            args=["--start-maximized", 
                # "--disable-popup-blocking",
                ], 
            # args=["--start-maximized"], 
            executable_path= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            slow_mo=350
            )  
              
        self.context = self.browser.new_context(no_viewport=True,accept_downloads=True)  
        self.context.set_default_timeout(60000)

        self.page:Page = self.context.new_page()

              
        download_path = os.path.join(os.getcwd(), "downloads")
        self.download_path = download_path  
        os.makedirs(self.download_path, exist_ok=True)  

        self.page.goto(self.site)


    def tearDown(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    @classmethod
    def tearDownClass(cls):
        # cls.context.close()
        # cls.browser.close()
        cls.playwright.stop()
