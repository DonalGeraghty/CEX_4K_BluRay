from message.email import Email
from objects.cex_page import CexPage
from playwright.sync_api import Page
from actions.manipulate import Manipulate

import time


class Steps:
    def test_cex(self, page: Page):
        cex_page = CexPage(page)
        email = Email()
        data = Manipulate()
        cex_page.goto_website()
        cex_page.assert_page_title()
        cex_page.accept_cookies()
        cex_page.filter_blu_ray_4k()
        time.sleep(3)
        cex_page.filter_in_stock_online()
        time.sleep(3)
        blu_ray_all = cex_page.get_all_blu_rays()
        data.output_blu_rays(blu_ray_all)
        blu_ray_list = data.return_diff_yesterday_today()
        name_price_df = data.get_prices_from_list(blu_ray_list)
        data.cleanup_files()
        email.send_mail(name_price_df)
