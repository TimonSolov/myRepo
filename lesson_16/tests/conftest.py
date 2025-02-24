import pytest
from playwright.sync_api import sync_playwright

from saucedemo_test.locators.main_page_locators import ERROR_MESSAGE
from saucedemo_test.pages.login_page import LoginPage


def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    page.goto(url="https://saucedemo.com")
    yield page
    page.close()


@pytest.fixture()
def login_page(page):
    return LoginPage(page)



