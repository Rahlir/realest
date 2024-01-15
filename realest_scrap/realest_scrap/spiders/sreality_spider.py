from json import loads
from typing import Any, Generator

from scrapy import Spider, Request
from scrapy.http import Response


class SrealitySpider(Spider):
    name = "sreality"
    page = 1
    per_page = 100
    url_template = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb={}&category_type_cb=1&per_page={}"
    scraped = 0
    scrap_limit: int | None = None

    def __init__(self, scrap_limit: str | None = None,
                 posting_category: int = 1,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.posting_category = posting_category
        if scrap_limit:
            try:
                self.scrap_limit = int(scrap_limit)
            except ValueError:
                raise ValueError("The scrap_limit must be a valid integer")
            if self.scrap_limit < self.per_page:
                self.per_page = self.scrap_limit
        self.start_urls = [self.url_template.format(self.posting_category, self.per_page)]

    def parse(self, response: Response) -> Generator[Request | dict[str, Any], None, None]:
        """Parse the posting from sreality if we are still within scrap_limit parameter."""
        if not self.scrap_limit or self.scraped < self.scrap_limit:
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

            # Only yield new request if we are not over limit and there are still
            # data to scrap
            if self.page * self.per_page < response_dict['result_size'] and \
                (not self.scrap_limit or self.scraped < self.scrap_limit):
                self.page += 1
                yield Request(
                    url=f"{self.start_urls[0]:s}&page={self.page:d}", callback=self.parse
                )
