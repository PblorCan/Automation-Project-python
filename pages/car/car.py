from playwright.sync_api import Page, Locator

class Car:
    def __init__(self, page: Page):
        self.page = page

    @property
    def go_to_pay_button(self) -> Locator:
        # The big orange button in the cart
        return self.page.get_by_role("link", name="IR A PAGAR")