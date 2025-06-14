import time
import pytest
from playwright.sync_api import expect, sync_playwright


@pytest.fixture()
def setup():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()


@pytest.mark.negative
def test_vwo_Login_negative(setup):
    page = setup
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    #page.wait_for_load_state("netwokidle")
    page.locator("//button[@onclick='jsAlert()']").click()
    result = page.locator("//p[@id='result']").text_content()
    assert result == "You successfully clicked an alert"
    time.sleep(5)
