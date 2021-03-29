import pytest
from selenium import webdriver

from ui.pages.AutorizationPage import *
from creds.creds import EMAIL, PASSWORD
from ui.pages.AuthorizedPage import AuthorizedPage


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path='C:\\Users\\Андрей\\chromedriver.exe')
    browser.get(url)
    browser.set_window_size(1400, 1000)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def authorization_page(driver):
    return AuthorizationPage(driver)


@pytest.fixture(scope="function")
def authorized_page(driver):
    page = AuthorizationPage(driver)
    page.authorize(EMAIL, PASSWORD)
    return AuthorizedPage(page.driver)
