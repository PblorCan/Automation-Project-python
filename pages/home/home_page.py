from playwright.sync_api import Page
from pages.home.components.navbar import Navbar 
from pages.home.components.header import Header
from pages.results.results import Results
from pages.checkout.checkout import Checkout
from pages.item.item import Item
from pages.car.car import Car

class HomePage:
    URL = "https://www.salcobrand.cl"

    def __init__(self, page: Page):
        self.page = page
        self.navbar = Navbar(self.page)
        self.header = Header(self.page)
        self.results = Results(self.page)
        self.checkout = Checkout(self.page)
        self.item = Item(self.page)
        self.car = Car(self.page)

    def open(self):
        self.page.goto(self.URL)
