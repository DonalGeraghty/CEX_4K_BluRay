import csv, time
from page_objects.cex_page import CexPage
from playwright.sync_api import Page
from data_manipulation.data import Data

def test_cex(page: Page):
    cexpage = CexPage(page)
    data = Data()
    cexpage.goto_website()
    cexpage.page_title_contains("CeX")
    cexpage.accept_cookies()
    cexpage.filter_blu_ray_4k()
    time.sleep(3)
    cexpage.filter_in_stock_online()
    time.sleep(3)
    blu_ray_all = cexpage.get_all_blu_rays()
    output_blu_rays(blu_ray_all)
    data.read_csv()

def output_blu_rays(blu_ray_all):
    with open("data.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for index, blu_ray in enumerate(blu_ray_all):
            writer.writerow([index, blu_ray.title, blu_ray.price])
