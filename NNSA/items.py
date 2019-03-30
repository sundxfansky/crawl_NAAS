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
    v = re.sub(r"排名：", "", v)
    v = re.sub(r"技术职称：", "", v)
    v = re.sub(r"工作单位：", "", v)
    v = re.sub(r"完成项目时所在单位：", "", v)
    if re.findall(r'对本项目',v):
        v=' '
    if not v:
        v ='unknown'
    return v


class NNSAItem(scrapy.Item):
    main_group = scrapy.Field()
    rank_num = scrapy.Field()
    project_name = scrapy.Field()
    nomination_unit= scrapy.Field()
    major = scrapy.Field()
    major_rank = scrapy.Field()
    administrative_duties = scrapy.Field( )
    technical_title = scrapy.Field()
    work_unit = scrapy.Field()
    complete_pro_unit = scrapy.Field()
    all_messeage = scrapy.Field()
    pass

class NNSAItemLoader(ItemLoader):
    default_input_processor = MapComposeCustom(remove_unuse_msg)
    default_output_processor = TakeFirst()
