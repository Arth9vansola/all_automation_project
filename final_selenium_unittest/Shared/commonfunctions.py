from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException,NoAlertPresentException

class commonfunctions:
    def __init__(self,driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

  
    def scroll_to_element(self, element):
        '''scroll to the particular element'''
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'nearest'});", element)
        except StaleElementReferenceException:
            # raise RuntimeError(f"Scroll Error: Element is stale or missing.") from e
            raise  
        except Exception:
            # raise RuntimeError("Failed to scroll to element") from e
            raise 

    def click_element(self, locator, value):
            '''click on element'''
            try:
                element = self.wait.until(EC.element_to_be_clickable((locator, value)))
                self.scroll_to_element(element)
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)
            except TimeoutException :
                # raise RuntimeError(f"Element not clickable: {value}") from e                
                raise                 
            except Exception :
                # raise RuntimeError(f"Unable to click element: locator={locator}, value={value}") from e  
                raise 

    def read_file(self, file_name):
        '''read content from particular file'''
        try:
            with open(file_name, "r") as file:
                for line in file:
                    print(line.strip())
        except Exception :
            # raise RuntimeError(f"Unable to read file: {file_name}") from e        
            raise 

    def write_file(self, file_name, file_content):
        '''write inside particular file'''
        try:
            with open(file_name, "a") as writing_file:
                writing_file.write(file_content)
        except Exception :
            # raise RuntimeError(f"Unable to write to file: {file_name}") from e
            raise 

    def locate_element(self, locator, value):
            '''locate one element'''
            try:
                return self.wait.until(EC.visibility_of_element_located((locator, value)))
            except Exception:
                # raise RuntimeError(f"Element not found with locator={locator}, value={value}") from e
                raise 


    def locate_elements(self, locator, value, min_count=1):
            '''locate more than one elements'''
            try:
                self.wait.until(lambda driver: len(driver.find_elements(locator, value)) >= min_count)
                elements = self.driver.find_elements(locator, value)
                if elements:
                    self.scroll_to_element(elements[0])
                return elements
            except TimeoutException:
                return []
            except Exception:
                # raise RuntimeError(f"Unable to locate elements with locator={locator}, value={value}") from e
                raise 

    def is_element_visible(self, locator, value):
        '''checks that particular is visible or not - Returns Boolean for Assertions'''
        try:
            return self.wait.until(EC.visibility_of_element_located((locator, value))).is_displayed()
        except (NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException):
            raise 
        except Exception:
            raise 
        
    def send_text(self, text, locator, value):
        '''send text in particular text field'''
        try:
            element = self.locate_element(locator, value)
            self.scroll_to_element(element)
            self.actions.move_to_element(element).click().perform()
            element.clear()
            element.send_keys(text)
        except Exception:
            # raise RuntimeError(f"Unable to send text to element with locator={locator}, value={value}") from e
            raise 

    def file_upload(self, locator, value, file_path):
        '''upload the file'''
        try:
            file_input = self.locate_element(locator, value)
            self.scroll_to_element(file_input)
            file_input.send_keys(file_path)
        except Exception:
            # raise RuntimeError(f"File upload failed for path: {file_path}") from e
            raise 
            
    def accept_alert(self):
        '''accept the alert'''
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            # raise RuntimeError("Unable to accept alert") from e
            raise 

    def dismiss_alert(self):
        '''dismiss the alert'''
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except Exception:
            # raise RuntimeError("Unable to dismiss alert") from e   
            raise 


    def hover_and_click(self, hover_locator, hover_value, click_locator, click_value):
        '''hover on particular card and then click on desired element'''
        try:
            # self.handle_ads()

            # hover
            hover_element = self.locate_element(hover_locator, hover_value)
            self.scroll_to_element(hover_element)
            self.actions.move_to_element(hover_element).perform()

            # click after hover
            self.wait.until(EC.element_to_be_clickable((click_locator, click_value)))
            click_element = self.locate_element(click_locator, click_value)
            click_element.click()

        except Exception:
            # raise RuntimeError(f"Unable to hover and click element") from e
            raise 
        
    def handle_dropdown(self, locator, value, data):
        '''Selects Dropdown elements'''
        try:
            dropdown = self.locate_element(locator,value)
            self.scroll_to_element(dropdown)
            self.actions.move_to_element(dropdown).click().perform()
            self.wait.until(EC.element_to_be_clickable((locator, value)))
            select = Select(dropdown)
            select.select_by_value(data)
        except Exception :
            # raise RuntimeError('Unable to select dropdown') from e    
            raise 

