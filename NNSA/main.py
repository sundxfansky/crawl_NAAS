# -*- coding:utf-8 -*-
__author__ = "sundxfansky@sjtu.edu.cn"


from scrapy.cmdline import execute
import sys
import os


# 获取当前目录的父目录

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "nnsa"])
