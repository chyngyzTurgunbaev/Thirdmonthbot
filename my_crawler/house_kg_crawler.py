import requests
from parsel import Selector

class HouseParser:
    MAIN_URL = 'https://www.house.kg/snyat-kvartiru'
    BASE_URL = 'https://www.house.kg'

    def get_page(self):
        response = requests.get(HouseParser.MAIN_URL)
        response.raise_for_status()
        self.page = response.text

    def get_page_title(self):
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_house_links(self):
        selector = Selector(text=self.page)
        links = selector.css('div.left-image a::attr(href)').getall()
        links = list(map(lambda l: f"{HouseParser.BASE_URL}{l}", links))
        return links[:3]