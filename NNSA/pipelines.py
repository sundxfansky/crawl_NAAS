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
                        '1主要完成人', '1行政职务','1技术职称','1工作单位','1完成项目时所在单位',
                        '2主要完成人', '2行政职务','2技术职称','2工作单位','2完成项目时所在单位',
                        '3主要完成人', '3行政职务','3技术职称','3工作单位','3完成项目时所在单位',
                        '4主要完成人', '4行政职务','4技术职称','4工作单位','4完成项目时所在单位',
                        '5主要完成人', '5行政职务','5技术职称','5工作单位','5完成项目时所在单位',
                        '6主要完成人', '6行政职务','6技术职称','6工作单位','6完成项目时所在单位'])
        pass
    def process_item(self,item,spider):
        self.ws.append([item['main_group'], item['rank_num'], item['project_name'], item['nomination_unit'],
                        item['major1'],item['administrative_duties1'],item['technical_title1'],item['work_unit1'],item['complete_pro_unit1'],
                        item['major2'],item['administrative_duties2'],item['technical_title2'],item['work_unit2'],item['complete_pro_unit2'],
                        item['major3'],item['administrative_duties3'],item['technical_title3'],item['work_unit3'],item['complete_pro_unit3'],
                        item['major4'],item['administrative_duties4'],item['technical_title4'],item['work_unit4'],item['complete_pro_unit4'],
                        item['major5'],item['administrative_duties5'],item['technical_title5'],item['work_unit5'],item['complete_pro_unit5'],
                        item['major6'],item['administrative_duties6'],item['technical_title6'],item['work_unit6'],item['complete_pro_unit6']])  # 将数据以行的形式添加到xlsx中
        return item
    def close_spider(self, spider):
        self.wb.save('data.xlsx')  # 保存xlsx文件
