# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://atjason.com',
    ]

    def parse(self, response):
        for atricle in response.xpath('//article[@class="post post-type-normal"]'):
            yield {
                'title': atricle.xpath('.//a[@class="post-title-link"]/text()').extract_first(),
                'date': atricle.xpath('.//time/text()').extract_first(),
                'content': atricle.xpath('./div/p/text()').extract()
            }

        # next_page_url = response.xpath('//a[@class="page-number"]/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
        for num in range(2,167):
            yield scrapy.Request(response.urljoin('/page/{}'.format(num)))

