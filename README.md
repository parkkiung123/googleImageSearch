# googleImageSearch

This is python image search program by scrapy.
It use google search engine.

# Development environment
+ python 2.7
+ scrapy 1.5
+ PIL 5.0

# Install
+ clone this project (download zip file and extract it)
+ pip install scrapy pillow

# Usage
+ setting keywords : variable key_words (googleImageSearch/spiders/spider.py)
+ setting the number of images (max limit 100) : variable limit (googleImageSearch/spiders/spider.py)
+ image search command : scrapy crawl imsearch

# Troubleshooting
+ If image cannot load, update PIL library (pip install --upgrade pillow)
