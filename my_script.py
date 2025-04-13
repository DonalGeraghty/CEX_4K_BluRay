from playwright.sync_api import sync_playwright

from tests.cex import Steps


def main():
    with sync_playwright() as p:
        steps = Steps()

        # setup browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # run test
        steps.test_cex(page)

        # cleanup
        browser.close()


if __name__ == "__main__":
    main()
