# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class TiebaPipeline(object):
    def process_item(self, item, spider):
        f=open('12.txt','a+')
        f.write(item['title']+':'+item['url']+'\n')
        return item