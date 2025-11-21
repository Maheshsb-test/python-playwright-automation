import time

from playwright.sync_api import Page, expect ,Playwright


def test_playwrightBasics(playwright): #playwright is fixture coming from pytest_playwright package
    browser =playwright.chromium.launch(headless=False) #Launching the chromium engine visually
    context =browser.new_context() #opening browser in incognito
    page =context.new_page() #opening new fresh tab in browser
    page.goto("https://rahulshettyacademy.com") #entering url and navigating

#chromium headless mode, 1 single context
def test_playwrightshortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademysddf")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

#Incorrect username/password. - assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)




