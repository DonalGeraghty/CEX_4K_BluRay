import time, re, csv
from playwright.sync_api import Page, expect

class Bluray:
    def __init__(self, title, price):
        self.title = title
        self.price = price

def get_all_blu_rays(page):
    print(2)
    old_url = page.url
    my_list = []

    while True:
        # add blu-rays to list
        bluray_all = page.locator(".search-product-card").all()
        for index, blueray in enumerate(bluray_all):
            title = blueray.locator(".card-title").inner_text()
            price = blueray.locator(".product-prices").inner_text()
            blu = Bluray(title, price)
            my_list.append(blu)

        # change page
        page.locator('[aria-label="Next Page"]').click()
        time.sleep(1)

        # get new_url
        new_url = page.url

        # if new_url is old_url then break
        if old_url is new_url:
            break
        else:
            old_url = new_url

    return my_list

def test_cex(page: Page):
    print("-----START-----")
    page.goto("https://ie.webuy.com/search?productLineId=41&productLineName=Blu-Ray")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("CeX"))

    # Accept cookies
    page.locator("#cmpbntyestxt:has-text('Accept All Cookies')").click()

    # Open only Blu-Ray 4K
    page.locator('span.item-label:has-text("Blu-Ray 4K")').first.locator('..').locator(".checkmark").click()
    time.sleep(3)

    # Open only In Stock Online
    page.locator('span.item-label:has-text("In Stock Online")').first.locator('..').locator(".checkmark").click()
    time.sleep(3)

    # Get Blu-Ray numbers
    results = page.locator(".products-listing-panel").locator(".ais-Stats").first
    print(results.inner_text())

    # Get all Blu-Rays
    blueray_all = get_all_blu_rays(page)

    # output Blue-Rays to csv
    output_file = "output.csv"

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for index, blueray in enumerate(blueray_all):
            print("writing..." + str(index) + "\t" + blueray.title + "\t" + blueray.price)
            writer.writerow([index, blueray.title, blueray.price])

    print("-----END-----")
