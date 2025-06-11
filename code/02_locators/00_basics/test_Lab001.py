import time
from playwright.sync_api import expect,sync_playwright

# Page - class -> Help you interact with HTML
# expect - Validate the message Expected Result == Actual Result
# Validation -> pytest - assert also available.
#This is my own test tried in gamma website

def test_gamma_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gamma.app/signin", timeout=60000)


    #page.wait_for_load_state("networkidle")

    page.locator("#email").fill("admin")

    page.locator("#password").fill("1234")

    page.locator('button[type="submit"]').click()

    error_message = page.locator("text=Invalid email or password")
    expect(error_message).to_have_text("Invalid email or password")

    time.sleep(5)

    context.close()