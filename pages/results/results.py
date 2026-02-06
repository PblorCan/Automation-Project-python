from playwright.sync_api import Page, Locator, expect


class Results:
    def __init__(self, page: Page):
        self.page = page

# titulo de resultados de busqueda
    @property
    def results_title(self) -> Locator:
        # Intentamos el selector específico, sino uno más genérico
        return self.page.locator(".category-title, .search-results-title, h1").first
    
# ordernar por:
    @property
    def sort_by(self) -> Locator:
        return self.page.locator(".ais-SortBy-select")
    
# ver cant de resultados 
    @property
    def results_count(self) -> Locator:
        return self.page.locator("ais-HitsPerPage-select")

#lista de productos
    @property
    def products_list(self) -> Locator:
        return self.page.locator(".ais-Hits-list .col-xs-6")

#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

#Complex methods


    def sort_by_lower_price(self, search_term: str) -> Locator:
        #obtenemos el primer elemento antes de ordenar
        first_product = self.page.locator(".ais-Hits-item").first
        #sacamos el precio del primer elemento
        first_price_text = first_product.locator(".display-offer-price").first.text_content()
        # Limpiamos el texto para dejar solo números (por ejemplo, quitamos "$" o puntos/comas si fuera necesario)
        first_price = float(first_price_text.replace("$", "").replace(".", "").replace(",", ".").strip())

        #ordenamos por precio menor a mayor
        self.sort_by.select_option("sb_normal_price_desc_production")
        
        # Esperamos a que la lista se actualice (puedes ajustar el selector si hay uno mejor)
        self.page.wait_for_load_state("networkidle")

        #obtenemos el primer elemento despues de ordenar
        second_product = self.page.locator(".ais-Hits-item").first
        #sacamos el precio del primer elemento
        second_price_text = second_product.locator(".display-offer-price").first.text_content()
        second_price = float(second_price_text.replace("$", "").replace(".", "").replace(",", ".").strip())
        
        #comparamos los precios
        assert first_price <= second_price


        
        