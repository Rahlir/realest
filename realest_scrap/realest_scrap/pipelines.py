from scrapy.crawler import Crawler, Spider
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

from realest_scrap.models import db_connect, setup_tables, Posting


class SrealityToPsgPipeline:
    def __init__(self, url: URL):
        engine = db_connect(url)
        setup_tables(engine)
        self.session = sessionmaker(bind=engine)

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'SrealityToPsgPipeline':
        """Build crawler using data from settings"""
        return cls(url=crawler.settings.get('DATABASE_URL'))


    def process_item(self, item: dict, spider: Spider) -> Posting:
        """If the crawled item isn't already in the database, save it there.

        Parameters
        ----------
        item : dict
            posting item
        spider : Spider
            spider object such as SRealitySpider

        Returns
        -------
        Posting
            SQLAlchemy model for posting

        """
        session = self.session()
        with session:

            instance = session.query(Posting).filter_by(id=item['id']).one_or_none()
            if instance:
                return instance

            # If the database isn't empty, the insertion order returned by the crawler
            # isn't correct.
            item['insertion_order'] = session.query(Posting).count()

            posting_item = Posting(**item)

            session.add(posting_item)
            session.commit()

            return posting_item
