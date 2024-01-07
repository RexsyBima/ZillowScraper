from app.PlayWright import PlayWright
from app.Parser import Parser

# {"data-testid": "price"})
if __name__ == "__main__":
    browser = PlayWright("https://www.zillow.com/telford-pa/")
    html = browser.goto()
    url = Parser(html)
    urls = url.scrape_url()
    print(urls)

    for url in urls:
        print(url)
        html = PlayWright(url).goto()
        url = Parser(html)
        try:
            url = url.scrape_product()
        except AttributeError:
            url = url.scrape_product_comingsoon()
