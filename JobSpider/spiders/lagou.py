# -*- coding: utf-8 -*-
import scrapy
from JobSpider import settings
import json
from JobSpider.items import LagouSpiderItem


class LagouSpider(scrapy.Spider):
    """
    拉勾网爬虫
    """
    name = 'lagou'
    allowed_domains = ['lagou.com']
    url = 'http://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false'
    # start_urls = [url]

    # 页码
    offset = 0
    # 更改该值，改变爬取的页数
    limit = 30
    # 搜索关键字
    keyWord = 'python'

    cookies = {
        # 'JSESSIONID': 'ABAAABAACDBABJB9F1D05C3E3578CEC86F0965AC555A37A',
        # 'SEARCH_ID': '66f6dc8dc3de4eadb299cdcad7d4371b',
        # 'TG-TRACK-CODE': 'search_code',
        # 'user_trace_token': '20170707202715-3baa3e93-66fa-4868-a52e-a3f2774e10e5',
        # 'LGRID': '20170707205851-069369f9-6314-11e7-84ae-525400f775ce',
        # 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1499432376',
        # '_ga': 'GA1.2.1571447545.1499430489',
        # '_gid': 'GA1.2.1040512897.1499430489',
        # 'LGUID': '20170707202724-a1e490b7-630f-11e7-a575-5254005c3644',
        # 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1499430491',
        # 'index_location_city': '%E5%8C%97%E4%BA%AC',

        'SEARCH_ID': 'eca19456d41c424b82cda452aaee9903',
        'JSESSIONID': 'ABAAABAABEEAAJAAF77D804691BB12E085B14674B4E3952',
        'TG-TRACK-CODE': 'index_search',
        '_ga': 'GA1.2.1571447545.1499430489',
        '_gid': 'GA1.2.1040512897.1499430489',
        'LGUID': '20170707202724-a1e490b7-630f-11e7-a575-5254005c3644',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1499476187,1499481856,1499569159,1499608634',
        'index_location_city': '%E5%8C%97%E4%BA%AC',
        '_gat': '1',
        'LGSID': '20170709215630-68ff8ebf-64ae-11e7-a6be-5254005c3644',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'user_trace_token': '20170709215631-0e20a69f8a9d4cd1b590a6618590d1ec',
        'LGRID': '20170709215644-713f9f5e-64ae-11e7-a6be-5254005c3644',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1499608648',
    }

    form_data = {
        'pn': str(offset),
        'kd': keyWord,
        'first': 'false'  # 第一页为 false 否则为 true
    }

    def start_requests(self):
        self.form_data['first'] = 'true'
        yield scrapy.FormRequest(url=self.url,
                                 cookies=self.cookies,
                                 formdata=self.form_data,
                                 callback=self.parse_json)

    def parse_json(self, response):
        print(response.url)
        json_obj = json.loads(response.text)
        results = json_obj['content']['positionResult']['result']
        for result in results:
            item = LagouSpiderItem()
            # print('position_id--->', result['positionId'])

            item['keyWord'] = self.keyWord
            item['businessZones'] = self.deal_list(result['businessZones'])
            item['companyFullName'] = self.deal_str(result['companyFullName'])
            item['companySize'] = self.deal_str(result['companySize'])
            item['createTime'] = self.deal_str(result['createTime'])
            item['district'] = self.deal_str(result['district'])
            item['education'] = self.deal_str(result['education'])
            item['financeStage'] = self.deal_str(result['financeStage'])
            item['positionName'] = self.deal_str(result['positionName'])
            item['salary'] = self.deal_str(result['salary'])
            item['workYear'] = self.deal_str(result['workYear'])
            item['companyLogo'] = self.deal_str(result['companyLogo'])
            item['positionId'] = self.deal_str(result['positionId'])

            yield item

        if self.offset < self.limit:
            self.offset += 1

        self.form_data['pn'] = str(self.offset)
        self.form_data['first'] = 'false'
        yield scrapy.FormRequest(self.url,
                                 headers=settings.DEFAULT_REQUEST_HEADERS,
                                 cookies=self.cookies,
                                 formdata=self.form_data,
                                 callback=self.parse_json)

    def deal_list(self, field):
        """
        集合类型 json 处理
        :param field:
        :return:
        """
        if field is not None and len(field):
            return ','.join(field)
        else:
            return 'NULL'

    def deal_str(self, field):
        """
        字符串 json 处理
        :param field:
        :return:
        """
        if field is not None:
            return field
        else:
            return 'NULL'

    def parse(self, response):
        pass
