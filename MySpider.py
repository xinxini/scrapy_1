# -*- encoding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem
class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = ["http://tieba.baidu.com/f?kw=%E6%B1%B6%E4%B8%8A%E4%B8%80%E4%B8%AD&fr=index&red_tag=i3568020782"]
    def parse(self, response):
        item = TiebaItem()
        for box in response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a[@class="j_th_tit "]'):
            item['url'] = 'http://tieba.baidu.com' + box.xpath('.//@href').extract()[0]
            item['title'] = box.xpath('.//@title').extract()[0].strip()
            yield item