import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["4399.com"]
    start_urls = ["https://www.4399.com/flash/"]

    def parse(self, response):
        # print(response.text)
        # txt = response.xpath('//*[@id="skinbody"]/div[8]/ul/li/a/b/text()').extract()
        # print(txt)

        lis = response.xpath("//ul[@class='n-game cf']/li")
        for li in lis:
            name = li.xpath("./a/b/text()").extract_first()
            categroy = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()
            dic = {
                "name": name,
                "categroy": categroy,
                "date": date
            }
            yield dic

