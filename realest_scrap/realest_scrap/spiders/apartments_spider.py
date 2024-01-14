from json import loads

from scrapy import Spider, Request

from realest_scrap.models import Posting


class SrealitySpider(Spider):
    name = "sreality"
    page = 1
    per_page = 100
    start_urls = [
        ("https://www.sreality.cz/api/cs/v2/estates?"
        f"category_main_cb=1&category_type_cb=1&per_page={per_page:d}")
    ]
    scraped = 0

    def parse(self, response, **kwargs):
        scrap_limit = self.settings.getint('SCRAP_LIMIT')
        if scrap_limit == 0 or self.scraped < scrap_limit:
            response_dict = loads(response.text)
            for posting in response_dict['_embedded']['estates']:
                picture = None
                if len(picture_arr := posting['_links']['images']) > 0:
                    picture = picture_arr[0]['href']

                yield dict(
                    id = posting['hash_id'],
                    name = posting['name'],
                    location = posting['locality'],
                    image_link = picture,
                    insertion_order = self.scraped
                )
                self.scraped += 1

            if self.page * self.per_page < response_dict['result_size'] and \
                (scrap_limit == 0 or self.scraped < scrap_limit):
                self.page += 1
                yield Request(
                    url=f"{self.start_urls[0]:s}&page={self.page:d}", callback=self.parse
                )
