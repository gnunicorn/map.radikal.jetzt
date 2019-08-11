import scrapy

from utils import geolocator

class ERSpider(scrapy.Spider):
    name = 'extinction_rebellion'
    start_urls = ['https://extinctionrebellion.de/og/']

    def parse(self, response):
        for group in response.css('.local-group'):
            info_sel = group.css(".local-group__info")

            contact = {}

            # info["state = 
            # if state == "Aktiv":
            #     info["state"] = "active"
            # elif state == "Inaktiv":
            #     info["state"] = "inactive"
            # else:
            #     info["state"] = "starting"
            
            email = info_sel.css(".local-group__email a span ::text").get()
            if email:
                contact["email"] = email

            pgp = info_sel.css("i.svg-container__lock + span ::text")
            if pgp:
                contact["pgp_key_id"] = pgp.split(":", 2)[-1]

            for node in info_sel.css("ul.icon-list ul.icon-list li"):
                href = node.css("a::attr(href)").get()
                icon_cls = node.css("i.svg-container::attr(class)").get()
                contact[icon_cls.split("__")[-1].strip()] = href

            title = group.css('h3 ::text').get().strip()

            location = geolocator.geocode(title + ", Germany")

            info = {
                'title':title,
                'location': {
                    'lat': location.latitude,
                    'lng': location.longitude
                },
                'state': group.css("::attr(class)").get().split("--", 1)[-1],
                'contact': contact
            }

            url = info_sel.css(".local-group__url a::attr(href)").get()
            if url:
                if url.startswith("/"):
                    info["website"] = "https://extinctionrebellion.de" + url
                else:
                    info["website"] = url

            yield info
