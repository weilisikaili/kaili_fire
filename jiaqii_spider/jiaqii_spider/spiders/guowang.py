# -*- coding: utf-8 -*-
import scrapy


class GuowangSpider(scrapy.Spider):
    name = 'guowang'
    allowed_domains = ['http://ecp.sgcc.com.cn/']
    start_urls = ['http://http://ecp.sgcc.com.cn//']

    def parse(self, response):
        pass
