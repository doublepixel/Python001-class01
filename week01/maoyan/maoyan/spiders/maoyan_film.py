# -*- coding: utf-8 -*-
import scrapy


class MaoyanFilmSpider(scrapy.Spider):
    name = 'maoyan_film'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ['http://https://maoyan.com//']

    def parse(self, response):
        pass
