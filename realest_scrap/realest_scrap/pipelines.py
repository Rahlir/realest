# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
from scrapy.crawler import Crawler
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

from realest_scrap.models import db_connect, setup_tables, Posting


class SrealityToPsgPipeline:
    def __init__(self, url: URL):
        engine = db_connect(url)
        setup_tables(engine)
        self.session = sessionmaker(bind=engine)

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(url=crawler.settings.get('DATABASE_URL'))


    def process_item(self, item, spider):
        session = self.session()
        with session:

            instance = session.query(Posting).filter_by(id=item['id']).one_or_none()
            if instance:
                return instance

            posting_item = Posting(**item)

            session.add(posting_item)
            session.commit()

            return posting_item
