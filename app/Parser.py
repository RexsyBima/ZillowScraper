from bs4 import BeautifulSoup
from app.Models import House
from app.Functions import rent


class Parser(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, "html.parser")

    def scrape_url(self, output: list = []):
        urls = self.find("ul", class_="List-c11n-8-84-3__sc-1smrmqp-0")
        li = urls.find_all("a", href=True)
        for i in li:
            if i["href"] not in output:
                output.append(i["href"])
        return output

    def scrape_product_comingsoon(self):
        item = House()
        item.price = (
            self.find("div", {"data-testid": "home-info"}).find("span").getText()
        )
        print(item.location)

    def scrape_product(self):
        item = House()
        p_bed_baths_sqft_loc_rent = self.find(
            "div", {"data-testid": "home-details-chip-container"}
        )
        item.price = (
            p_bed_baths_sqft_loc_rent.find("span", {"data-testid": "price"})
            .find("span")
            .getText()
        )
        item.location = p_bed_baths_sqft_loc_rent.find(
            "div", class_="styles__AddressWrapper-sc-13x5vko-0"
        ).h1.getText()
        beds_bath_sqft = p_bed_baths_sqft_loc_rent.findAll(
            "div", {"data-testid": "bed-bath-sqft-fact-container"}
        )
        item.beds = beds_bath_sqft[0].span.getText()
        item.baths = beds_bath_sqft[1].span.getText()
        item.area = beds_bath_sqft[2].span.getText()
        item.rent = rent(p_bed_baths_sqft_loc_rent)
        print(item.location)
        print(item.price)
        print(item.beds)
        print(item.baths)
        print(item.area)
        print(item.rent)
