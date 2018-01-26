# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline

class GoogleimagesearchPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,
                                 meta={'key_word':item['image_key_word']})

    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return '%s/%s.jpg' % (request.meta.get('key_word')[0].decode('utf-8'), image_guid)