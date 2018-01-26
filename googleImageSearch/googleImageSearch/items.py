# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GoogleimagesearchItem(scrapy.Item):
    pass

class ImagedownloaderItem(scrapy.Item):

    image_urls = scrapy.Field()
    image_key_word = scrapy.Field()
    images = scrapy.Field()