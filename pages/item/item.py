from playwright.sync_api import Page, Locator, expect

class Item:
    def __init__(self, page: Page):
        self.page = page
    #añadir al carrito
    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.locator(".btn-warning")
    #precio internet
    @property
    def internet_price(self) -> Locator:
        return self.page.locator(".price .offer-price .display-price")
    #titulo del producto
    @property
    def title(self) -> Locator:
        return self.page.locator(".product-content .product-info")
    
    #formato del producto
    @property
    def format(self) -> Locator:
        return self.page.locator(".input-group .last")
    
    #cantidad del producto
    @property
    def quantity(self) -> Locator:
        return self.page.locator(".input-group .show")
    
    #boton up contador producto
    @property
    def up_button(self) -> Locator:
        return self.page.locator(".quantity .fa-chevron-up")
    
    #boton down contador producto
    @property
    def down_button(self) -> Locator:
        return self.page.locator(".quantity .fa-chevron-down")
    
    #modal y boton ir a pagar
    @property
    def go_to_pay_button(self) -> Locator:
        return self.page.locator(".col-xs-12 .btn-flat[href='/cart']")

    #modal y boton seguir comprando
    @property
    def continue_shopping_button(self) -> Locator:
        return self.page.locator(".col-xs-12 .btn-flat[data-dismiss='modal']")
    
    #modal y  cantidad del producto
    @property
    def modal_quantity(self) -> Locator:
        return self.page.locator(".addedtocart__quantity")

    
    
#metodos
    #up or down quantity
    def up_or_down_quantity(self, quantity: int, up_or_down: str):
       try:
            if up_or_down == "up":
                self.up_quantity(quantity)
            elif up_or_down == "down":
                self.down_quantity(quantity)
       except Exception as e:
            raise Exception("Error al incrementar o decrementar la cantidad del producto")
    
    #up quantity
    def up_quantity(self, quantity: int):
        for _ in range(quantity):
            self.up_button.click()
    
    #down quantity
    def down_quantity(self, quantity: int):
        for _ in range(quantity):
            self.down_button.click()
    
    