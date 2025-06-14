import time
import pytest
from playwright.sync_api import expect,sync_playwright

@pytest.fixture()
def setUp():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()

@pytest.mark.positive
def test_vwo_login(setUp):
    page = setUp
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on('dialog',lambda dialog: dialog.accept("Mathina"))
    page.locator("//button[@onClick='jsPrompt()']").click()
    result = page.locator("//p[@id='result']").text_content()
    assert result == "You entered: Mathina"
    time.sleep(5)

