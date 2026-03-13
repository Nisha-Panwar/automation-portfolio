from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert page.url == "https://www.saucedemo.com/inventory.html"
        print("✅ Login test passed!")
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "wrong_user")
        page.fill("#password", "wrong_pass")
        page.click("#login-button")
        error = page.locator("[data-test='error']")
        assert error.is_visible()
        print("✅ Invalid login test passed!")
        browser.close()

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert page.url == "https://www.saucedemo.com/inventory.html"
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        cart = page.locator("[data-test='shopping-cart-badge']")
        assert cart.is_visible()
        print("✅ Add to cart test passed!")
        browser.close()
