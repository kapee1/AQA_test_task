import pytest
from selenium import webdriver
import urls

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(urls.main_url)
    yield driver
    driver.quit()