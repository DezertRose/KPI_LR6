import time
from selenium import webdriver

if __name__ == '__main__':
   browser = webdriver.Chrome()
   browser.get("https://play.google.com/")
   assert  browser.title == "Google Play"
   time.sleep(3)
   browser.find_element_by_css_selector('[name = "q"]').send_keys("Duskwood - Crime & Investigation Detective Story")
   browser.find_element_by_class_name('gbqfb').click()
   assert ("No results found" not in browser.page_source) and ("Результатов не найдено" not in browser.page_source)

   browser.find_element_by_xpath( "/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a").click()
   time.sleep(3)
   assert browser.current_url == "https://play.google.com/store/apps/details?id=com.everbytestudio.interactive.text.chat.story.rpg.cyoa.duskwood"

browser.close()