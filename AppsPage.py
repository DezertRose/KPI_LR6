from MainApp import DefineBasicMethods as dbm
from selenium.webdriver.common.by import By

class GoogleAppLocators:
    LOCATOR_GOOGLE_APP_SEARCH_FIELD = (By.CSS_SELECTOR, '[name = "q"]')
    LOCATOR_GOOGLE_APP_SEARCH_BUTTON = (By. CLASS_NAME,  "gbqfb")
    LOCATOR_GOOGLE_APP_TO_PAGE_BUTTON = (By. XPATH,  "/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a")
    LOCATOR_GOOGLE_APP_HEADER = (By.XPATH, "/html/body/div[1]/div[4]/c-wiz[3]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span)")


class SearchHelper(dbm):

    def enter_words_input(self, word):
        search_field = self.find_element(GoogleAppLocators.LOCATOR_GOOGLE_APP_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on(self, temp_locator):
        temp =  GoogleAppLocators.LOCATOR_GOOGLE_APP_SEARCH_BUTTON
        if temp_locator == 1:
          temp = GoogleAppLocators.LOCATOR_GOOGLE_APP_SEARCH_BUTTON
        if temp_locator == 2:
            temp = GoogleAppLocators.LOCATOR_GOOGLE_APP_TO_PAGE_BUTTON
        return  self.find_element(temp, time = 3).click

    def check_header(self):
        return ( self.look_for_elements(GoogleAppLocators.LOCATOR_GOOGLE_APP_HEADER, time=10)).text