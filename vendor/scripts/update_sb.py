import scrapy

from utils import geolocator

class SBSpider(scrapy.Spider):
    name = 'seebruecke_crawler'
    start_urls = ['https://seebruecke.org/mach-mit/']

    def _item_parse(self, response):
        title = response.css('meta[property="og:title"]::attr(content)').get().split(" | ")[0].strip()
        print(title)
        location = geolocator.geocode(title)

        if not location:
            print("------------------------------------------- NO LOCATION FOUND")
            print(title)
            return
        contact = {}

        for entry in response.css("div.support a.support__item"):
            contact[entry.css(".visually-hidden::text").get()] = entry.attrib["href"]

        contact["email"] = response.css('main a[href^="mailto:"]::attr(href)').get()

        yield {
            "title": title,
            "website": response.url,
            "header": response.css("img.header__image::attr(src)").get(default="").strip(),
            "state": "active",
            'location': {
                'lat': location.latitude,
                'lng': location.longitude
            },
            "contact": contact,
        }

    def parse(self, response):
        for section in response.css(".localgroups__group"):
            sect_name = section.css("h3 ::text").get()

            for url in section.css('h4.action__title > a::attr(href)'):
                yield response.follow(url, self._item_parse)
