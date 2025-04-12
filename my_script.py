from tests import cex
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # setup browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # run test
        cex.test_cex(page)

        # cleanup
        browser.close()

if __name__ == "__main__":
        main()