from tests import cex
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        cex.test_cex(page)
        browser.close()

if __name__ == "__main__":
        main()