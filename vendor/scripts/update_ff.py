import scrapy

from utils import geolocator

class FFSpider(scrapy.Spider):
    name = 'fridaysforfuture_crawler'
    start_urls = ['https://fridaysforfuture.de/regionalgruppen/']

    def parse(self, response):
        for section in response.css(".su-spoiler"):
            if section.attrib['data-anchor'] == "de": continue
            
            for li in section.css("li"):
                contact = {}
                name = "".join(li.css("::text").getall()).split(":")[0].strip()
                location = geolocator.geocode(name)

                if not location:
                    print("------------------------------------------- NO LOCATION FOUND")
                    print(name)
                    continue

                for entry in li.css("a[href]"):
                    title = entry.css("::text").get()
                    if not title:
                        continue
                    if '@' in title:
                        contact["email"] = title
                        continue

                    contact[title.lower()] = entry.attrib["href"]


                yield {
                    "title": name,
                    "state": "active",
                    'location': {
                        'lat': location.latitude,
                        'lng': location.longitude
                    },
                    "contact": contact,
                }