# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import json


class JobSpiderPipeline(object):
    def __init__(self):
        super(JobSpiderPipeline, self).__init__()
        # Connect to the database
        self.connection = pymysql.connect(host='192.168.1.107',
                                          user='root',
                                          password='root',
                                          db='jobs',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

        self.file = open('zhaoping.json', 'w')

    def process_item(self, item, spider):
        print('process_item--->', spider.name)
        if spider.name == 'lagou':
            self.save_lagou_item(item)
        elif spider.name == 'zhilian':
            self.save_zhilian_item(item)
        else:
            pass

        return item

    def close_spiders(self, spider):
        self.connection.close()
        self.file.close()

    def save_lagou_item(self, item):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO jobs_lagou (keyWord, businessZones, companyFullName, companySize, createTime," \
                      "district, education, financeStage, positionName, salary, workYear, companyLogo, positionId) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (item['keyWord'], item['businessZones'], item['companyFullName'],
                                     item['companySize'], item['createTime'], item['district'], item['education'],
                                     item['financeStage'], item['positionName'], item['salary'], item['workYear'],
                                     item['companyLogo'], item['positionId']))
                self.connection.commit()
            print('insert succeed')
        except Exception:
            print('insert failed')

    def save_zhilian_item(self, item):
        json_string = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_string.encode('utf-8') + '\n')

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO jobs_zhilian (keyWord, position, company, salary, address," \
                      "pubDate, detailHref) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (item['keyWord'], item['position'], item['company'],
                                     item['salary'], item['address'], item['pubDate'], item['detailHref']))
                self.connection.commit()
            print('insert succeed')
        except Exception:
            print('insert failed')
        pass
