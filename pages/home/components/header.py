from playwright.sync_api import Page, Locator, expect

class Header:
    def __init__(self, page: Page):
        self.page = page
    #mantener ubicacion
    @property
    def keep_location_button(self) -> Locator:
        return self.page.locator(".row .btn-light").first

    #formulario de cambio de ubicacion
    @property
    def change_location_form(self) -> Locator:
        return self.page.locator(".select-commune__form input[type='text']:visible")
    
    #lista de resultados al buscar
    @property
    def result_list(self) -> Locator:
        return self.page.locator(".select-commune__results .b-radius")
    
    #boton confirmar
    @property
    def confirm_button(self) -> Locator:
        return self.page.locator(".form-wrapper .btn-main")
    
    #input para rellenar region
    @property
    def fill_region(self) -> Locator:
        return self.page.locator(".dropdown-location input[type='text']")
    
    #mensaje de exito
    @property
    def sucess_message(self) -> Locator:
        return self.page.locator(".select-commune__wrapper.open p.mb-0")
    
    @property
    def location_text(self) -> Locator:
        return self.page.locator(".visible-sm .commune-name")
    
    #selector de ubicacion
    @property
    def location_selector(self) -> Locator:
        return self.page.locator(".dropdown-menu.dropdown-location button.btn-main:visible")
    
    #-----------------------------------------
    #Methods
    #-----------------------------------------
    def location(self, value: str, city: str):
        if value == "keep":
            self.keep_location(city)
        elif value == "change":
            self.change_location(city)
        

    def keep_location(self, city: str):
        try:
            # Esperamos brevemente a que el modal aparezca
            self.keep_location_button.wait_for(state="visible", timeout=5000)
            self.keep_location_button.click()
        except Exception:
            # Si no aparece en 5s, asumimos que no es necesario
            pass
        region = self.location_text.text_content()
        return region
        

    def change_location(self, city: str):
        # 1. Clic en el botón para cambiar ubicación
        self.change_location_form.wait_for(state="visible", timeout=5000)
        self.change_location_form.click()

        # 2. rellenar y presionar enter para mostar resultados
        self.fill_region.wait_for(state="visible", timeout=5000)
        self.fill_region.fill(city)
        self.fill_region.press("Enter")

        # 3. seleccionar el resultado
        self.result_list.wait_for(state="visible", timeout=5000)
        self.result_list.click()
        
        # 4. Confirmar el cambio
        self.confirm_button.wait_for(state="visible", timeout=5000)
        self.confirm_button.click()

        # 5. Verificar mensaje de éxito
        self.sucess_message.wait_for(state="visible", timeout=5000)

        # Esperar a que el modal desaparezca o que la UI se actualice
        self.page.wait_for_load_state("load")