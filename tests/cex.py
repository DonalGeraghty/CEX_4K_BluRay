import csv, time
from objects.cex_page import CexPage
from playwright.sync_api import Page
from data.manipulate import Manipulate

def test_cex(page: Page):
    cex_page = CexPage(page)
    data = Manipulate()
    cex_page.goto_website()
    cex_page.assert_page_title()
    cex_page.accept_cookies()
    cex_page.filter_blu_ray_4k()
    time.sleep(3)
    cex_page.filter_in_stock_online()
    time.sleep(3)
    blu_ray_all = cex_page.get_all_blu_rays()
    output_blu_rays(blu_ray_all)
    data.read_csv()
    data.compare_old_new()

def output_blu_rays(blu_ray_all):
    with open("data.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "name", "price"])
        for index, blu_ray in enumerate(blu_ray_all):
            writer.writerow([index, blu_ray.title, blu_ray.price])
