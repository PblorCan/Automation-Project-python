import pytest
from playwright.sync_api import sync_playwright 
from pages.home.home_page import HomePage

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def home_page(browser):
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.open()
    yield home_page
    page.close()
