import  pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser_func():
    browser = webdriver.Chrome(executable_path="./chromedriver")
    yield browser
    browser.quit()