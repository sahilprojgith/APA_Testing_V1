from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto("https://www.saucedemo.com")

    print("Website opened successfully!")

    input("Press Enter to close browser...")

    browser.close()