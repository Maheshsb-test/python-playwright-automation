

from playwright.sync_api import Page, expect



def test_placeholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()



    #Alert popups

    page.on("dialog", lambda dialog:dialog.accept())
    #anonymous function - function without name is called and which is declared by keyword lamda
    page.get_by_role("button", name="Confirm").click()


    #mouseHover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()


    #FrameHandling

    Pageframe = page.frame_locator("#courses-iframe")
    Pageframe.get_by_role("link", name="All-Access").first.click()
    expect(Pageframe.locator("body")).to_contain_text("Choose Your All-Access Plan")


    #check the price of the rice is equal to 37
    #identify the price column
    #identify the rice row
    #extract price the of the rice
def test_webtable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            Pricecolvalue = index
            print(f"price column value is {Pricecolvalue} ")
            break

    ricerow = page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(Pricecolvalue)).to_have_text("37")











