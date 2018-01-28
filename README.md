# googleImageSearch

This is python image search & download program by scrapy.

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
+ image search command : scrapy crawl imsearch (cd googleImageSearch)

# Troubleshooting
+ If image cannot be loaded, update PIL library (pip install --upgrade pillow)

# Reference
+ https://github.com/hardikvasa/google-images-download
