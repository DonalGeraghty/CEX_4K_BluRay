import csv, time
from page_objects.cex_page import CexPage
from playwright.sync_api import Page

def test_cex(page: Page):
    cexpage = CexPage(page)
    cexpage.goto_website()
    cexpage.page_title_contains("CeX")
    cexpage.accept_cookies()
    cexpage.filter_blu_ray_4k()
    time.sleep(3)
    cexpage.filter_in_stock_online()
    time.sleep(3)
    blu_ray_all = cexpage.get_all_blu_rays()
    output_blu_rays(blu_ray_all)

def output_blu_rays(blu_ray_all):
    with open("output.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for index, blu_ray in enumerate(blu_ray_all):
            writer.writerow([index, blu_ray.title, blu_ray.price])
