# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader


class BasicSpider(scrapy.Spider):
    name = 'basic_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        blog_headers = response.xpath("//span[@class='text']//text()")
        for 
        pass
