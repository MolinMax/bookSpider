# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #书名
    book_name = scrapy.Field()
    #作者名
    book_author = scrapy.Field()
    #原书名
    origin_name = scrapy.Field()
    #出版日期
    publish_date = scrapy.Field()
    #页数
    page_count = scrapy.Field()
    #价格
    book_price = scrapy.Field()
    #装帧
    wrapping = scrapy.Field()
    #isbn
    isbn = scrapy.Field()

    # pass
