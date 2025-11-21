#launch firefox browser
import time

from playwright.sync_api import Playwright


def test_firefoxBrowser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)  # Launching the chromium engine visually
    context = browser.new_context()  # opening browser in incognito
    page = context.new_page()  # opening new fresh tab in browser
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademysddf")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    time.sleep(5)
