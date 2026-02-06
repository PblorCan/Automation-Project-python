import pytest
import random
from playwright.sync_api import expect
from pages.home.home_page import HomePage


@pytest.mark.smoke
def test_buy_product_as_guest(home_page: HomePage, step_report):
    #buscar producto
    search_term = "ibuprufeno"
    step_report.step("Buscar producto", lambda: home_page.navbar.search(search_term))

    # Esperar a que los resultados sean visibles
    step_report.step("Esperar a que los resultados sean visibles", lambda: home_page.results.products_list.first.wait_for(state="visible", timeout=10000))
    
    #click en el primer producto
    step_report.step("Click en el primer producto", lambda: home_page.results.products_list.nth(1).click())

    #tomar valor del precio internet
    price_text = home_page.item.internet_price.text_content()
    #pasar a float y dar formato
    price = float(price_text.replace("$", "").replace(",", ""))

    # inicializar contador por un valor rnd y subir el contador
    quantity = random.randint(1, 4)
    step_report.step("Subir cantidad", lambda: home_page.item.up_or_down_quantity(quantity, "up"))

    #calcular el precio final
    final_price = price * quantity

    # agregar al carrito
    step_report.step("Agregar al carrito", lambda: home_page.item.add_to_cart_button.click())

    # Pequeña espera para permitir que la redirección o el modal ocurran
    home_page.page.wait_for_timeout(3000)

    # Verificar si redirigió al carrito o si hay un modal
    if "cart" in home_page.page.url:
        # Si ya estamos en el carrito, el botón de ir a pagar está en el objeto 'car'
        step_report.step("Click en ir a pagar (desde el carrito)", lambda: home_page.car.go_to_pay_button.click())
    else:
        # Si hay un modal, seguimos el flujo original
        # tomar valor de la cantidad del producto en el modal
        modal_quantity_text = home_page.item.modal_quantity.text_content()
        # separar el texto del numero y pasar a int
        modal_quantity = int(modal_quantity_text.split(":")[1].strip())
        # click en ir a pagar
        step_report.step("Click en ir a pagar (desde el modal)", lambda: home_page.item.go_to_pay_button.click())

    # click btn continuar como invitado (en la página de login/checkout)
    # Esperar a que la página cargue para encontrar el botón de invitado
    home_page.page.wait_for_load_state("networkidle")
    step_report.step("Click en continuar como invitado", lambda: home_page.checkout.continue_as_guest_button.click())

    # completar informacion del cliente
    step_report.step("Completar informacion del cliente, primer nombre", lambda: home_page.checkout.first_name.fill("pablo"))
    step_report.step("Completar informacion del cliente, apellido", lambda: home_page.checkout.last_name.fill("ortiz"))
    step_report.step("Completar informacion del cliente, email", lambda: home_page.checkout.email.fill("pablo.ortiz.cancino1@gmail.com"))
    step_report.step("Completar informacion del cliente, telefono", lambda: home_page.checkout.phone.fill("991539469"))

    #click btn continuar
    step_report.step("Click en continuar", lambda: home_page.checkout.continue_button.click())

    #click btn continuar
    step_report.step("Click en continuar", lambda: home_page.checkout.continue_button.click())

    #medio de pago
    step_report.step("Click en medio de pago", lambda: home_page.checkout.payment_method.first.click())

    #check de terminos y condiciones
    step_report.step("Click en terminos y condiciones", lambda: home_page.checkout.terms.click())

    #url de pago externo
    url = home_page.page.url
    #comparar url
    assert "https://webpay3g.transbank.cl/" in url

    def assert_error():
        raise Exception("Error en el test")

    step_report.step("Verificar URL de pago externo", assert_error)