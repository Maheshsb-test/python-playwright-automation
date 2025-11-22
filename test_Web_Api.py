from playwright.sync_api import Playwright, expect

from utils.api_Base import ApiUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    apiutils = ApiUtils()
    orderId = apiutils.createOrder(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("maheshbadakal8@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Aa123456@#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    #order history page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()