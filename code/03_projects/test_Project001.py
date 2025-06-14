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
def test_katalon_studio_appointment_booking(setUp):
    page = setUp
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    page.wait_for_load_state("networkidle")
    expect(page).to_have_title("CURA Healthcare Service")
    page.locator("//a[@id='btn-make-appointment']").click()
    page.locator("//input[@id='txt-username']").fill("John Doe")
    page.locator("//input[@id='txt-password']").fill("ThisIsNotAPassword")
    page.locator("//button[@id='btn-login']").click()

    page.wait_for_load_state("networkidle")
    expect(page).to_have_url("https://katalon-demo-cura.herokuapp.com/#appointment")
    page.locator("//textarea[@id='txt_comment']").fill("I have fever")
    page.locator("//input[@id='txt_visit_date']").fill("04/04/2025")
    page.locator("//input[@id='txt_visit_date']").press('Enter')
    time.sleep(5)
    page.locator("//button[@id='btn-book-appointment']").click()

    result = page.locator("//h2[normalize-space()='Appointment Confirmation']").text_content()
    assert result == "Appointment Confirmation"
    time.sleep(5)

