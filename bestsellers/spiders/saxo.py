from datetime import datetime

import scrapy
from bestsellers.items import BestsellersItem
from bestsellers.itemsloaders import BookLoader
from scrapy_splash import SplashRequest


class SaxoSpider(scrapy.Spider):
    """Spider for scraping the bestseller books of the first 10 pages"""

    name = "saxo"
    allowed_domains = ["saxo.com"]
    base_domain = "https://www.saxo.com"
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "FEEDS": {
            f"{name}.json": {"format": "json"},
        },
    }

    def start_requests(self):
        urls = ["https://www.saxo.com/dk/bestsellere?page=%d" % i for i in range(1, 11)]
        for url in urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                args={
                    "wait": 3,
                    "http_method": "GET",
                },
            )

    def parse(self, response):
        # Scrape all books listed
        for link in response.css("a.btn-icon-rounded::attr('href')"):
            yield SplashRequest(
                url=self.base_domain + link.get(),
                callback=self.parse_book,
                args={"wait": 3, "http_method": "GET"},
            )

    def parse_book(self, response):
        book_info = BookLoader(item=BestsellersItem(), selector=response)

        # Book description
        book_info.add_css(
            "price",
            "#prices-holder > div:nth-child(1) > label:nth-child(2) > span:nth-child(2)::text",
        )
        book_info.add_css(
            "member_price",
            "#prices-holder > div:nth-child(2) > label:nth-child(2) > span:nth-child(2)::text",
        )
        book_info.add_css("book_name", "h1.text-xl::text")
        book_info.add_css("author_name", "div.text-s > ul > li > a:link::text")
        book_info.add_css(
            "book_format", "ul.product-detail:nth-child(1) > li:nth-child(2)::text"
        )
        book_info.add_css(
            "pages", "ul.product-detail:nth-child(1) > li:nth-child(4)::text"
        )
        book_info.add_css(
            "publication_date", ".description-dot-list > li:nth-child(3)::text"
        )

        # Spider info
        book_info.add_value("url", response.url)
        book_info.add_value("spider", self.name)
        book_info.add_value("date", datetime.now())

        yield book_info.load_item()
