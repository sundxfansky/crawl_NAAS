# -*- coding:utf-8 -*-
__author__ = "sundxfansky@sjtu.edu.cn"

import scrapy
from scrapy.http import Request
from NNSA.items import NNSAItem
from NNSA.items import NNSAItemLoader
import re


class NNSASpider(scrapy.Spider):
    name = 'nnsa'
    allowed_domains = ['nosta.gov.cn']
    start_urls = ['http://www.nosta.gov.cn/upload/2019slxmgb/showProject.html']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    def parse(self,response):

        # 爬取所有的
        # group_urls = response.css('td:nth-child(2) > a::attr(href)').extract()
        # for group_u in group_urls:
        #     group_u = response.urljoin(group_u)
        #     yield Request(group_u, headers=self.header,callback=self.parse_main_group)

        #爬取机械
        group_url = 'fm_308/fmIndex.html'
        group_url = response.urljoin(group_url)
        yield Request(group_url, headers=self.header, callback=self.parse_main_group)

    def parse_main_group(self, response):
        for j in range(100): # 0-99
            i = j+2
            id = 'tr:nth-child('+str(i)+') > td:nth-child(2) > a::attr(href)'
            project_url = response.css(id).extract_first()

            project_url = response.urljoin(project_url)
            main_group = response.css('#page_title::text').extract_first()
            rank_num = i-1
            unnormal1 = response.css('tr:nth-child('+str(i)+') > td:nth-child(3)::text').extract_first()
            if rank_num>=1:
                if unnormal1:
                    if re.findall(r'专家', unnormal1):
                        yield Request(project_url,headers=self.header,meta={'id':rank_num,'main_group':main_group,'nomination_unit': unnormal1},callback=self.parse_project_F)
                    else:
                        yield Request(project_url,headers=self.header,meta={'id':rank_num,'main_group':main_group,'nomination_unit': unnormal1},callback=self.parse_project_T)



    def parse_project_F(self, response):
        rank_num = response.meta.get('id','')
        main_group = response.meta.get('main_group','')
        nomination_unit = response.meta.get('nomination_unit','')
        item_loader = NNSAItemLoader(item=NNSAItem(), response=response)
        item_loader.add_value('main_group', main_group)
        item_loader.add_value('rank_num', rank_num)
        item_loader.add_xpath('project_name', '//tr[1]/td[2]/text()')
        item_loader.add_value('nomination_unit', nomination_unit)
        for j in range(6):
            i = j + 1
            item_loader.add_xpath('major' + str(i),
                                    '//tr[6]//li['+str(i)+']/b/text()')
            item_loader.add_xpath('administrative_duties' + str(i),
                                  '//tbody/tr[6]/td[2]/ol//li[' + str(i) + ']/text()[3]')
            item_loader.add_xpath('technical_title' + str(i),
                                  '//tbody/tr[6]/td[2]/ol//li[' + str(i) + ']/text()[4]')
            item_loader.add_xpath('work_unit' + str(i), '//tbody/tr[6]/td[2]/ol//li[' + str(i) + ']/text()[5]')
            item_loader.add_xpath('complete_pro_unit' + str(i),
                                  '//tbody/tr[6]/td[2]/ol//li[' + str(i) + ']/text()[6]')
            item_loader.add_xpath('all_messeage' + str(i), '//tbody/tr[6]/td[2]/ol//li[' + str(i) + ']')
        nnsa_item = item_loader.load_item()
        yield nnsa_item

    def parse_project_T(self, response):
        rank_num = response.meta.get('id', '')
        main_group = response.meta.get('main_group', '')
        item_loader = NNSAItemLoader(item=NNSAItem(), response=response)
        item_loader.add_value('main_group', main_group)
        item_loader.add_value('rank_num', rank_num)
        item_loader.add_xpath('project_name', '//tr[1]/td[2]/text()')
        item_loader.add_xpath('nomination_unit', '//tr[2]/td[2]/text()')
        for j in range(6):
            i = j+1
            item_loader.add_css('major'+str(i), 'ol > li:nth-child('+str(i)+') > b::text')
            item_loader.add_xpath('administrative_duties'+str(i), '//li['+str(i)+']/text()[3]')
            item_loader.add_xpath('technical_title'+str(i), '//li['+str(i)+']/text()[4]')
            item_loader.add_xpath('work_unit'+str(i), '//li['+str(i)+']/text()[5]')
            item_loader.add_xpath('complete_pro_unit'+str(i), '//li['+str(i)+']/text()[6]')
            # item_loader.add_xpath('all_messeage'+str(i), '//li['+str(i)+']')
        nnsa_item = item_loader.load_item()
        yield nnsa_item





