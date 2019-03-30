# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymysql # mysql version
# from twisted.enterprise import adbapi



from openpyxl import Workbook
class NNSAPipeline(object):
    def open_spider(self, spider):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['类别', '序号', '项目名', '提名单位',
                        '主要完成人', '主要完成人排名','行政职务','技术职称','工作单位','完成项目时所在单位'])
        pass
    def process_item(self,item,spider):
        self.ws.append([item['main_group'], item['rank_num'], item['project_name'],
                        item['nomination_unit'],item['major'],item['major_rank'],
                        item['administrative_duties'],item['technical_title'],
                        item['work_unit'],item['complete_pro_unit']
                        ])
        return item
    def close_spider(self, spider):
        self.wb.save('data.xlsx')  # 保存xlsx文件
