
from playwright.sync_api import sync_playwright, Page
import pytest
import os
from Shared.TestAssert import TestAssert


class webdriverbase(TestAssert):

    # site = None
    global site

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        self.playwright = sync_playwright().start()

        request.cls.playwright = self.playwright

        yield

        self.playwright.stop()


    @pytest.fixture(autouse=True)
    def setup(self, request):

        self.browser = self.playwright.chromium.launch(
            headless=False,
            args=["--start-maximized"],
            executable_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            slow_mo=350
        )

        self.context = self.browser.new_context(
            no_viewport=True,
            accept_downloads=True
        )

        self.context.set_default_timeout(120000)

        self.page: Page = self.context.new_page()

        download_path = os.path.join(os.getcwd(), "downloads")
        self.download_path = download_path
        os.makedirs(self.download_path, exist_ok=True)

        self.page.goto(request.cls.site)

        # request.cls.context = self.context
        # request.cls.browser = self.browser

        yield self.page

        self.page.close()
        self.context.close()
        self.browser.close()