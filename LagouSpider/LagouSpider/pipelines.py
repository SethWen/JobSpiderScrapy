# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class LagouspiderPipeline(object):
    def __init__(self):
        super(LagouspiderPipeline, self).__init__()
        # Connect to the database
        self.connection = pymysql.connect(host='192.168.1.104',
                                          user='root',
                                          password='root',
                                          db='jobs',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO jobs_lagou (keyWord, businessZones, companyFullName, companySize, createTime," \
                      "district, education, financeStage, positionName, salary, workYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (item['keyWord'], item['businessZones'], item['companyFullName'],
                                     item['companySize'], item['createTime'], item['district'], item['education'],
                                     item['financeStage'], item['positionName'], item['salary'], item['workYear']))
                self.connection.commit()
            print('insert succeed')
        except Exception:
            print('insert failed')

        return item

    def close_spiders(self, spider):
        self.connection.close()
