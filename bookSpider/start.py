from scrapy import cmdline
cmdline.execute("scrapy crawl bookSpider -o book.json".split())
# cmdline.execute("scrapy crawl bookSpider".split())