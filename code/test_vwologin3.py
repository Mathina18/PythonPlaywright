import pytest
import allure

from playwright.sync_api import expect, sync_playwright


# Page - class -> Help you interact with HTML
# expect - Validate the message Expected Result == Actual Result
# Validation -> pytest - assert also available.

def test_vwo_login():
    # 1. Browser and Page
    browser = sync_playwright().start().chromium.launch(headless=False)
    # create a new incognito browser context
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()

    # 2. Code Interaction with the HTML Web page
    page1.goto("https://app.vwo.com")
    page2.goto("https://www.google.com")
    #breakpoint()


    # 3. Validation
    expect(page1).to_have_title("Login - VWO")
    # dispose context once it is no longer needed.
    context.close()


