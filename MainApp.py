from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class DefineBasicMethods:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://play.google.com/"

    def find_element(self, locator, time = 5 ):
        return WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator), message=f"Can't find element by {locator}")

    def find_more_elements(self, locator, time = 5):
        return WebDriverWait(self.browser, time).until(ec.presence_of_all_elements_located(locator), message=f"Can't find elements by {locator}")

    def way_to_website(self):
        return self.browser.get(self.base_url)