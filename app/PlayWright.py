from playwright.sync_api import sync_playwright


class PlayWright:
    def __init__(self, url: str) -> None:
        assert isinstance(url, str)
        self.url = url

    def goto(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            html = page.inner_html("body")
        return html
