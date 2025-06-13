import time

from playwright.sync_api import expect, sync_playwright


def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://gamma.app/signin", timeout=60000)
    # Make page loaded
    #page.wait_for_load_state("networkidle")
    page.locator("//input[@id='email']").fill("admin@admin.com")

    time.sleep(10)

    # dispose context once it is no longer needed.
    context.close()
