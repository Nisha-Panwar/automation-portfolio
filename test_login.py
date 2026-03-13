# Taking sync_playwright tool from playwright toolbox
from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        # Open chromium browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Go to the website
        page.goto("https://www.saucedemo.com")
        # Fill the username
        page.fill("#user-name", "standard_user")
        # Fill the password
        page.fill("#password", "secret_sauce")
        # Click on login
        page.click("#login-button")
        # Confirm url is open
        assert page.url == "https://www.saucedemo.com/inventory.html"
        print("✅ Login test passed!")
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        # Open chromium browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Go to the website
        page.goto("https://www.saucedemo.com")
        # Fill wrong username
        page.fill("#user-name", "wrong_user")
        # Fill wrong password
        page.fill("#password", "wrong_pass")
        # Click on login
        page.click("#login-button")
        # Confirm error message is visible
        error = page.locator("[data-test='error']")
        assert error.is_visible()
        print("✅ Invalid login test passed!")
        browser.close()

def test_add_to_cart():
    with sync_playwright() as p:
        # Open chromium browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Go to the website
        page.goto("https://www.saucedemo.com")
        # Fill the username
        page.fill("#user-name", "standard_user")
        # Fill the password
        page.fill("#password", "secret_sauce")
        # Click on login
        page.click("#login-button")
        # Confirm url is open
        assert page.url == "https://www.saucedemo.com/inventory.html"
        # Click add to cart button
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        # Confirm cart badge is visible
        cart = page.locator("[data-test='shopping-cart-badge']")
        assert cart.is_visible()
        print("✅ Add to cart test passed!")
        browser.close()
