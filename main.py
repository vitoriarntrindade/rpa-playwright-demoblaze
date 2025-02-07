from playwright.sync_api import sync_playwright
import random
import time


def run_demo_blaze_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.demoblaze.com/")
        time.sleep(5)

        # Seleciona produtos disponíveis na página inicial
        product_elements = page.locator(".hrefch").all()

        if len(product_elements) < 2:
            print("Não há produtos suficientes para realizar o teste.")
            browser.close()
            return

        selected_products = random.sample(product_elements, 2)

        cart_products = []

        for product in selected_products:
            product_name = product.inner_text()
            print(f"Selecionando produto: {product_name}")
            product.click()
            time.sleep(5)

            page.click("text=Add to cart")
            time.sleep(5)

            page.on("dialog", lambda dialog: dialog.accept())
            print(f"Produto adicionado ao carrinho: {product_name}")
            cart_products.append(product_name)

            page.click("text=Home")
            time.sleep(5)

        page.click("text=Cart")
        time.sleep(10)

        # Valida se os produtos estão no carrinho
        cart_items = page.locator("#tbodyid tr td:nth-child(2)").all_text_contents()

        for product in cart_products:
            assert product in cart_items, f"Erro: {product} não encontrado no carrinho!"

        print("Todos os produtos foram adicionados ao carrinho com sucesso!")

        browser.close()


if __name__ == "__main__":
    run_demo_blaze_bot()
