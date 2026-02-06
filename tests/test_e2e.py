import pytest
import random
from playwright.sync_api import expect
from pages.home.home_page import HomePage


@pytest.mark.smoke
def test_buy_product_as_guest(home_page: HomePage):
    #buscar producto
    search_term = "ibuprufeno"
    home_page.navbar.search(search_term)

    # Esperar a que los resultados sean visibles
    home_page.results.products_list.first.wait_for(state="visible", timeout=10000)
    
    #click en el primer producto
    home_page.results.products_list.nth(1).click()

    #tomar valor del precio internet
    price_text = home_page.item.internet_price.text_content()
    #pasar a float y dar formato
    price = float(price_text.replace("$", "").replace(",", ""))

    # inicializar contador por un valor rnd y subir el contador
    quantity = random.randint(1, 4)
    home_page.item.up_or_down_quantity(quantity, "up")

    #calcular el precio final
    final_price = price * quantity

    #agregar al carrito
    home_page.item.add_to_cart_button.click()

    #tomar valor de la cantidad del producto en el modal
    modal_quantity_text = home_page.item.modal_quantity.text_content()

    #separar el texto del numero y pasar a int
    modal_quantity = int(modal_quantity_text.split(":")[1].strip())

     #click en ir a pagar
    home_page.item.go_to_pay_button.click()

    # click btn ir a pagar
    home_page.checkout.go_to_pay_button.click()

    # completar informacion del cliente
    home_page.checkout.first_name.fill("pablo")
    home_page.checkout.last_name.fill("ortiz")
    home_page.checkout.email.fill("pablo.ortiz.cancino1@gmail.com")
    home_page.checkout.phone.fill("991539469")

    #click btn continuar
    home_page.checkout.continue_button.click()

    #click btn continuar
    home_page.checkout.continue_button.click()

    #medio de pago
    home_page.checkout.payment_method.first.click()

    #check de terminos y condiciones
    home_page.checkout.terms.click()

    #url de pago externo
    url = home_page.page.url
    #comparar url
    assert "https://webpay3g.transbank.cl/" in url