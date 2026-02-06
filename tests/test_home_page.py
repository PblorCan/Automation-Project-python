import pytest
from playwright.sync_api import expect
from pages.results.results import Results

@pytest.mark.smoke
@pytest.mark.skip
def test_search_product(home_page):
    """Verifica que la búsqueda de un producto devuelva resultados relevantes."""
    search_term = "ibuprufeno"
    home_page.navbar.search(search_term)
    expect(home_page.results.results_title).to_contain_text(search_term, ignore_case=True)

@pytest.mark.smoke
@pytest.mark.skip
def test_keep_location(home_page):
    """Verifica que el botón 'Mantener ubicación' funcione correctamente."""
    #obtenemos la ubicacion actual
    current_location = home_page.header.location_text.text_content()
    #click en el boton de ubicacion
    home_page.header.location_selector.click()
    #mantener la ubicacion
    home_page.header.location("keep","")
    #verificamos que la ubicacion se haya mantenido
    try:
        # comment: verificamos que la ubicacion se haya mantenido
        expect(home_page.header.location_text).to_contain_text(current_location, ignore_case=True)  
    except Exception as e:
        raise Exception("La ubicacion no se ha mantenido")
    # end try

@pytest.mark.smoke
@pytest.mark.skip
def test_change_location(home_page):
    """Verifica el cambio de ubicación a una ciudad específica (Santiago)."""
    target_city = "Santiago"
    #click en el boton de ubicacion
    home_page.header.location_selector.click()
    #cambiamos la ubicacion
    home_page.header.location("change", target_city)
    #verificamos que la ubicacion se haya cambiado
    expect(home_page.header.sucess_message).to_contain_text("exitosamente", ignore_case=True)


    
@pytest.mark.smoke
@pytest.mark.skip
def test_sort_by_lower_price(home_page):
    """Verifica que la ordenación por precio menor a mayor funcione correctamente."""
    search_term = "ibuprufeno"
    home_page.navbar.search(search_term)
    home_page.results.sort_by_lower_price(search_term)   
    
