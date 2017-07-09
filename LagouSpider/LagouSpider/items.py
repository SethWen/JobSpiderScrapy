# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyWord = scrapy.Field()
    businessZones = scrapy.Field()
    companyFullName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()
    workYear = scrapy.Field()

    """
           "businessZones": [
                           "学院路"
                       ],
                       "city": "北京",
                       "companyFullName": "云蜂科技有限公司",
                       "companyId": 199892,
                       "companyLabelList": [],
                       "companyLogo": "i/image/M00/1B/62/CgpFT1kJeXqACXeMAAAoV3nbMC0350.jpg",
                       "companyShortName": "云蜂科技",
                       "companySize": "15-50人",
                       "createTime": "2017-07-07 09:41:49",
                       "deliver": 0,
                       "district": "海淀区",
                       "education": "本科",
                       "financeStage": "初创型(不需要融资)",
                       "firstType": "开发/测试/运维类",
                       "formatCreateTime": "1天前发布",
                       "imState": "disabled",
                       "industryField": "移动互联网",
                       "industryLables": [],
                       "jobNature": "全职",
                       "lastLogin": 1499408418000,
                       "pcShow": 0,
                       "positionAdvantage": "发展空间大,技术氛围好,办公环境好,简单开放",
                       "positionId": 3085536,
                       "positionLables": [
                           "MySQL",
                           "爬虫"
                       ],
                       "positionName": "Python工程师",
                       "publisherId": 7865651,
                       "salary": "15k-25k",
                       "score": 0,
                       "secondType": "后端开发",
                       "workYear": "3-5年"
           """
    pass
