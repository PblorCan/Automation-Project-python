from playwright.sync_api import Page, expect, Locator
from pages.results.results import Results

class Navbar:
    def __init__(self, page: Page):
        self.page = page

    @property
    def search_input(self) -> Locator:
        return self.page.locator("#algolia-search-bar > div > div > form > input[type=search]")

    @property
    def search_button(self) -> Locator:
        return self.page.locator("#algolia-search-bar > div > div > form > button")


    """ methods """

    def search(self, product: str):
        self.search_input.fill(product)
        self.search_button.press("Enter")
        return Results(self.page)
        
