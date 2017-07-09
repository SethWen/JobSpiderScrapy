# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from random import random

from scrapy import signals
from scrapy.http import HtmlResponse

from LagouSpider.settings import USER_AGENTS

from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys


class LagouspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 随机 User-Agent 中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        """
        添加随机 User-Agent 中间件
        :param request:
        :param spider:
        """
        print('RandomUserAgent')
        user_agent = random.choice(USER_AGENTS)
        # print user_agent
        request.headers.setdefault('User-Agent', user_agent)
        # request.headers.setdefault('If-Modified-Since', date)


class JsDriver(object):
    def process_request(self, request, spider):
        print "PhantomJS is starting..."
        # 如果没有设置环境变量，指定 phantomjs 所在位置
        # driver = webdriver.PhantomJS(executable_path="D:/Develop/phantomjs-2.1.1-windows/bin/phantomjs")
        # driver = webdriver.Chrome('D:\WorkSpace\python\LagouSpider\chromedriver.exe')
        driver = webdriver.Chrome('D:\WorkSpace\python\LagouSpider\chromedriver.exe')
        # 指定浏览器
        # driver = webdriver.Chrome('D:\WorkSpace\python\LagouSpider\chromedriver.exe')

        driver.get(request.url)

        body = driver.page_source

        print("JsDriver-----" + request.url)
        print('current_url-----' + driver.current_url)
        # 爬完该页数据关闭，防止 chrome-driver 发生异常退出
        # driver.close()

        with open('lagoujs.html', 'w') as f:
            f.write(body.encode('utf-8'))

        driver.find_element_by_class_name('pager_next ').click()

        return HtmlResponse(url=request.url, body=body, encoding='utf-8', request=request)
