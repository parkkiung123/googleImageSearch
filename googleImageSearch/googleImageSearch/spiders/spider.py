# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2
from scrapy.loader import ItemLoader
from ..items import ImagedownloaderItem

# Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:  # If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"', start_line + 1)
        end_content = s.find(',"ow"', start_content + 1)
        content_raw = str(s[start_content + 6:end_content - 1])
        return content_raw, end_content

# Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page, limit):
    items = []
    k = 0
    while (k < limit):
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)  # Append all the links in the list named 'Links'
            time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
            page = page[end_content:]
            k += 1
    return items

class SpiderSpider(scrapy.Spider):
    name = 'imsearch'
    headers = {}
    headers['User-Agent'] \
        = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    key_words = [
        'Cristiano Ronaldo',
        'Lionel Messi'
    ]
    limit = 20

    def start_requests(self):
        url = 'https://www.google.com/search?q=%s&tbs=isz:m,itp:face&tbm=isch&source=lnt&sa=X&ved=0ahUKEwibys6VleHYAhUB57wKHadwC1wQpwUIHg&biw=1366&bih=667&dpr=1'
        for key_word in self.key_words:
            req_url = url%urllib2.quote(key_word).encode("utf-8")
            yield scrapy.Request(url=req_url, headers=self.headers, callback=self.parse, meta={'key_word':key_word})

    def parse(self, response):
        body = response.body
        items = []
        items = items + (_images_get_all_items(body, self.limit))
        il = ItemLoader(item=ImagedownloaderItem())
        il.add_value('image_key_word', response.meta.get('key_word'))
        for k in range(self.limit):
            il.add_value('image_urls', items[k])
        return il.load_item()





