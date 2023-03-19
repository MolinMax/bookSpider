# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from collections import Iterable


class BookspiderPipeline:
    def __init__(self):
        print("====star====")

        self.sql = pymysql.connect(host='localhost', user='root', password='数据库密码', db='py', port=3306,
                                   charset='utf8')
        self.cursor = self.sql.cursor()

    def process_item(self, item, spider):
        tplt = "{0:10}\t{1:{8}^10}\t{2:{8}^10}\t{3:{8}^10}\t{4:{8}^10}\t{5:{8}^10}\t{6:{8}^10}\t{7:{8}^10}"
        print(tplt.format("书名", "作者", "原书名", "出版日期", "页数", "价格", "装帧", "isbn", chr(12288)))
        data = "insert into book(book_name,book_author,origin_name,publish_date,page_count,book_price,wrapping,isbn) value (%s,%s,%s,%s,%s,%s,%s,%s);"
        # print(len(item),type(item["book_author"]),item["book_name"])
        print(tplt.format(item["book_name"],
                          item["book_author"],
                          item["origin_name"],
                          item["publish_date"],
                          item["page_count"],
                          item["book_price"],
                          item["wrapping"],
                          item["isbn"], chr(12288)))
        value = (item["book_name"],
                 item["book_author"],
                 item["origin_name"],
                 item["publish_date"],
                 item["page_count"],
                 item["book_price"],
                 item["wrapping"],
                 item["isbn"])
        try:
            self.cursor.execute(data, value)
            print(value)
            self.sql.commit()
        except:
            self.sql.rollback()
            print("数据库连接失败！")

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.sql.close()
        print("爬虫结束")

    # def open_spider(self, spider):
    #     self.f = open('book.csv', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     content = str(dict(item)) + ',\n'
    #     self.f.write(content)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.f.close()
    #     print("爬虫结束")
