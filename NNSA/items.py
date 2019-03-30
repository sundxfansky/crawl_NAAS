# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.common import wrap_loader_context
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import re
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.datatypes import MergeDict

class MapComposeCustom(MapCompose):
    #自定义MapCompose，当value没元素时传入" "
    def __call__(self, value, loader_context=None):
        if not value:
            value.append(" ")
        values = arg_to_iter(value)
        if loader_context:
            context = MergeDict(loader_context, self.default_loader_context)
        else:
            context = self.default_loader_context
        wrapped_funcs = [wrap_loader_context(f, context) for f in self.functions]
        for func in wrapped_funcs:
            next_values = []
            for v in values:
                next_values += arg_to_iter(func(v))
            values = next_values
        return values

class TakeFirstCustom(TakeFirst):
    def __call__(self, values):
        for value in values:
            if value is not None and value != '':
                return value.strip() if isinstance(value, str) else value


def remove_black(a):
    a = a.replace(" ", "")
    a = a.replace("\r", "")
    a = a.replace("\n", "")
    a = a.replace("\t", "")
    if not a:
        a = 'unknown'
    return a
def remove_unuse_msg(v):
    v = str(v)
    v = re.sub(r"行政职务：", "", v)
    v = re.sub(r"技术职称：", "", v)
    v = re.sub(r"工作单位：", "", v)
    v = re.sub(r"完成项目时所在单位：", "", v)
    if not v:
        v ='unknown'
    return v


class NNSAItem(scrapy.Item):
    # define the fields for your item here like:
    main_group = scrapy.Field()
    rank_num = scrapy.Field(
        # output_processor = MapCompose(int)
    )
    project_name = scrapy.Field()
    nomination_unit= scrapy.Field()
    major1 = scrapy.Field()
    administrative_duties1 = scrapy.Field( )
    technical_title1 = scrapy.Field()
    work_unit1 = scrapy.Field()
    complete_pro_unit1 = scrapy.Field()
    all_messeage1 = scrapy.Field()
    major2 = scrapy.Field()
    administrative_duties2 = scrapy.Field()
    technical_title2 = scrapy.Field()
    work_unit2 = scrapy.Field()
    complete_pro_unit2 = scrapy.Field()
    all_messeage2 = scrapy.Field()
    major3 = scrapy.Field()
    administrative_duties3 = scrapy.Field()
    technical_title3 = scrapy.Field()
    work_unit3 = scrapy.Field()
    complete_pro_unit3 = scrapy.Field()
    all_messeage3 = scrapy.Field()
    major4 = scrapy.Field()
    administrative_duties4 = scrapy.Field()
    technical_title4 = scrapy.Field()
    work_unit4 = scrapy.Field()
    complete_pro_unit4 = scrapy.Field()
    all_messeage4 = scrapy.Field()
    major5 = scrapy.Field()
    administrative_duties5 = scrapy.Field()
    technical_title5 = scrapy.Field()
    work_unit5 = scrapy.Field()
    complete_pro_unit5 = scrapy.Field()
    all_messeage5 = scrapy.Field()
    major6 = scrapy.Field()
    administrative_duties6 = scrapy.Field()
    technical_title6 = scrapy.Field()
    work_unit6 = scrapy.Field()
    complete_pro_unit6 = scrapy.Field()
    all_messeage6 = scrapy.Field()
    pass

class NNSAItemLoader(ItemLoader):
    default_input_processor = MapComposeCustom(remove_unuse_msg)
    default_output_processor = TakeFirst()
