from playwright.sync_api import Page, Locator, expect

class Checkout:
    def __init__(self, page: Page):
        self.page = page

    # checkout title (quantity of items)
    @property
    def checkout_title(self) -> Locator:
        return self.page.locator(".checkout-summary-title")

    # total price
    @property
    def total(self) -> Locator:
        return self.page.locator(".checkout-total-value")

    #continuar como invitado
    @property
    def continue_as_guest_button(self) -> Locator:
        return self.page.locator(".blue-border-bottom")

    #-----------------informacion del cliente-----------------
    @property
    def first_name(self) -> Locator:
        return self.page.locator("input[name='first_name']")
    
    @property
    def last_name(self) -> Locator:
        return self.page.locator("input[name='last_name']")
    
    @property
    def email(self) -> Locator:
        return self.page.locator("input[name='email']")
    
    @property
    def phone(self) -> Locator:
        return self.page.locator("input[name='phone']")
    #-----------------informacion del cliente-----------------
    #boton continuar
    @property
    def continue_button(self) -> Locator:
        return self.page.locator(".btn-warning")

    #elegir tienda de despacho
    @property
    def store(self) -> Locator:
        return self.page.locator(".pickup-delivery-form .radio-input")

    #medio de pago
    @property
    def payment_method(self) -> Locator:
        return self.page.locator(".method_options .payment_method_group")

    #check de terminos y condiciones
    @property
    def terms(self) -> Locator:
        return self.page.locator(".summary-terms input[type='checkbox']")
