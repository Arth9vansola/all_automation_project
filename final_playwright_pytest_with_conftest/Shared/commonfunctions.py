import typing
from playwright.sync_api import Page


class commonfunctions():

    def __init__(self, page: Page):
        self.page = page


    def locate_element(
        self,
        locator: typing.Literal[
            "get_by_placeholder",
            "get_by_alt_text",
            "get_by_label",
            "get_by_role",
            "get_by_test_id",
            "get_by_text",
            "get_by_title",
            "id",
            "class_name",
            "xpath",
            "link_text",
            "partial_link_text",
            "name",
            "tag_name",
            "css_selector"
        ],
        value,
        name=None
    ):
        try:
            match locator:

                case "get_by_role":
                    return self.page.get_by_role(value, name=name).first

                case "get_by_text":
                    return self.page.get_by_text(value, exact=False).first

                case "get_by_alt_text":
                    return self.page.get_by_alt_text(value).first

                case "get_by_title":
                    return self.page.get_by_title(value).first

                case "get_by_placeholder":
                    return self.page.get_by_placeholder(value).first

                case "get_by_label":
                    return self.page.get_by_label(value).first

                case "id":
                    return self.page.locator(f'#{value}').first

                case "class_name":
                    return self.page.locator(f'.{value}').first

                case "xpath":
                    return self.page.locator(value).first
                
                case "link_text":
                    return self.page.get_by_role("link", name=value, exact=True).first

                case "partial_link_text":
                    return self.page.get_by_role("link", name=value, exact=False).first

                case "name":
                    return self.page.locator(f'[name="{value}"]').first

                case "tag_name":
                    return self.page.locator(value).first

                case "css_selector":
                    return self.page.locator(value).first                

                case _:
                    return self.page.locator(value).first

        except Exception:
            raise


    def locate_elements(
        self,
        locator: typing.Literal[
            "get_by_placeholder",
            "get_by_alt_text",
            "get_by_label",
            "get_by_role",
            "get_by_test_id",
            "get_by_text",
            "get_by_title",
            "id",
            "class_name",
            "xpath",
            "link_text",
            "partial_link_text",
            "name",
            "tag_name",
            "css_selector"
        ],
        value,
        name=None
    ):
        try:
            match locator:

                case "get_by_role":
                    return self.page.get_by_role(value, name=name).all()

                case "get_by_text":
                    return self.page.get_by_text(value, exact=False).all()

                case "get_by_alt_text":
                    return self.page.get_by_alt_text(value).all()

                case "get_by_title":
                    return self.page.get_by_title(value).all()

                case "get_by_placeholder":
                    return self.page.get_by_placeholder(value).all()

                case "get_by_label":
                    return self.page.get_by_label(value).all()

                case "id":
                    return self.page.locator(f'#{value}').all()

                case "class_name":
                    return self.page.locator(f'.{value}').all()

                case "xpath":
                    return self.page.locator(value).all()

                case "link_text":
                    return self.page.get_by_role("link", name=value, exact=True).all()

                case "partial_link_text":
                    return self.page.get_by_role("link", name=value, exact=False).all()

                case "name":
                    return self.page.locator(f'[name="{value}"]').all()

                case "tag_name":
                    return self.page.locator(value).all()

                case "css_selector":
                    return self.page.locator(value).all()
                
                case _:
                    return self.page.locator(value).all()

        except Exception:
            raise


    def click_element(self, locator, value, name=None):
        try:
            self.locate_element(locator, value, name).click()
        except Exception:
            raise


    def send_text(self, data, locator, value, name=None):
        try:
            self.locate_element(locator, value, name).fill(data)
        except Exception:
            raise


    def check_btn(self, locator, value, name=None):
        try:
            element = self.locate_element(locator, value, name)

            if not element.is_checked():
                element.check()

        except Exception:
            raise


    def handle_dropdown(self, locator, value, data, name=None):
        try:
            self.locate_element(locator, value, name).select_option(data)
        except Exception:
            raise


    def is_element_visible(self, locator, value, name=None):
        try:
            element = self.locate_element(locator, value, name)
            return element.is_visible()

        except Exception:
            raise


    def click_accept_alert(self, role, name):
        try:
            self.page.on("dialog", lambda dialog: dialog.accept())
            self.page.get_by_role(role=role, name=name).click()
        except Exception:
            raise


    def file_upload(self, file_path, locator, value, name=None):
        try:
            self.locate_element(locator, value, name).set_input_files(file_path)
        except Exception:
            raise


    def scroll_to_element(self, locator, value, name=None):
        try:
            self.locate_element(locator, value, name).scroll_into_view_if_needed()
        except Exception:
            raise


    def hover_and_click(
        self,
        hover_locator,
        hover_value,
        click_locator,
        click_value,
        hover_name=None,
        click_name=None
    ):
        try:
            self.locate_element(hover_locator, hover_value, hover_name).hover()
            self.locate_element(click_locator, click_value, click_name).click()
        except Exception:
            raise


    def switch_tab(self, index_of_window):
        try:
            self.page.wait_for_timeout(2000)

            tabs = self.page.context.pages

            tabs[index_of_window].bring_to_front()

            self.page = tabs[index_of_window]

        except Exception:
            raise