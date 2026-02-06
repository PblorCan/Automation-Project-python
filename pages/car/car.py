from playwright.sync_api import Page

class Car:
    def __init__(self, page: Page):
        self.page = page