# -*- coding: utf-8 -*-
import scrapy
from JobSpider.items import ZhilianSpiderItem
import re


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']

    offset = 0
    site = '北京'
    keyWord = 'python'
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&sm=0&p=' % (site, keyWord)

    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        print(response.url)

        nodes = response.xpath('//table')
        # 弹出第一个表头元素
        nodes.pop(0)
        # print('length = ' + str(len(nodes)))
        for node in nodes:
            item = ZhilianSpiderItem()

            item['keyWord'] = self.keyWord

            position = node.xpath('.//td[@class="zwmc"]//a').extract()
            for p in position:
                pattern = re.compile(r'>.*</a>')
                dealedPosition = pattern.findall(p)[0].replace('<b>', '').replace('</b>', '').replace('</a>', '').replace('>', '')
                item['position'] = dealedPosition

            company = node.xpath('.//td[@class="gsmc"]//a/text()').extract()
            item['company'] = self.deal_detail(company)

            salary = node.xpath('.//td[@class="zwyx"]/text()').extract()
            item['salary'] = self.deal_detail(salary)

            address = node.xpath('.//td[@class="gzdd"]/text()').extract()
            item['address'] = self.deal_detail(address)

            pubDate = node.xpath('.//td[@class="gxsj"]/span/text()').extract()
            item['pubDate'] = self.deal_detail(pubDate)

            detailHref = node.xpath('.//td[@class="gsmc"]/a/@href').extract()
            item['detailHref'] = self.deal_detail(detailHref)
            yield item

        if self.offset < 20:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def deal_detail(self, list):
        if len(list):
            return list[0]
        else:
            return 'NULL'
