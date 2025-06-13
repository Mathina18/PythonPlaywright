import time
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

@pytest.mark.negative
def test_vwo_login_negative(setUp):
    page = setUp
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.wait_for_load_state("networkidle")
    page.locator()