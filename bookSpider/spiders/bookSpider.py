import scrapy
from bookSpider.items import BookspiderItem
import copy

class bookSpider(scrapy.Spider):
    name = "bookSpider"
    allowed_domains = ['book.douban.com']
    start_urls = ["https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={}".format(i) for i in range(1,11,1)]
    # start_urls = ["https://book.douban.com/latest?p=1"]

    def parse(self, response):
        if response.status == 200 and len(response.text) > 10:
            # 使用xpath解析网页，获取所需元素
            titles = response.xpath('//a[@class="fleft"]/text()').extract()
            urls = response.xpath('//a[@class="fleft"]/@href').extract()
            for i in range(0, len(titles)):
                item = BookspiderItem()
                url = urls[i]
                title = titles[i]
                # 测试输出
                # print(url, title)
                # 将解析到的 内容详情页url 拿去 获取页面中的内容
                item["book_name"] = title
                yield scrapy.Request(url=url, callback=self.html, meta={'item': copy.deepcopy(item)})
            """
                获取url详情页中的数据
            """


    # 处理字段空值
    def try_except(self, response, xpath_str):
        try:
            field = response.xpath(xpath_str).extract_first()
        except:
            field = '无'
        if field==None:
            field = "无"
        return field

    def html(self, response):
        item = response.meta['item']
        # 判断请求的链接返回的状态码和文本内容长度
        if response.status == 200 and len(response.text) > 10:
            info = response.xpath('//div[@id="info"]')
            # 使用xpath解析内容详情页，获取所需元素
            item["book_author"] = self.try_except(response,'//div[@id="info"]/span[1]/a/text()')
            item["origin_name"] = self.try_except(response,u'//span[contains(./text(), "原作名:")]/following::text()[1]')
            item["publish_date"] = self.try_except(response,u'//span[contains(./text(), "出版年:")]/following::text()[1]')
            item["page_count"] = self.try_except(response,u'//span[contains(./text(), "页数:")]/following::text()[1]')
            item["book_price"] = self.try_except(response,u'//span[contains(./text(), "定价:")]/following::text()[1]')
            item["wrapping"] = self.try_except(response,u'//span[contains(./text(), "装帧:")]/following::text()[1]')
            item["isbn"] = self.try_except(response,u'//span[contains(./text(), "ISBN:")]/following::text()[1]')
            # 测试输出
            # print(info,origin_name)
            yield item
