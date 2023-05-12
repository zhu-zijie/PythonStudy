import scrapy
from caipiao.items import CaipiaoItem


class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response, **kwargs):
        # print(response.text)
        trs = response.xpath('//tbody[@id="tdata"]/tr')
        for tr in trs:
            if tr.xpath('./@class').extract_first() == 'tdbck':
                continue
            qihao = tr.xpath('./td[1]/text()').extract_first()
            # red_ball = tr.xpath('./td[@class="chartBall01"]/text()').extract()
            red_ball = tr.css(".chartBall01::text").extract()
            blue_ball = tr.xpath('./td[@class="chartBall02"]/text()').extract_first()
            # 不建议这么写
            # dic = {
            #     "qihao": qihao,
            #     "red_ball": red_ball,
            #     "blue_ball": blue_ball
            # }
            # yield dic

            caipiao = CaipiaoItem()
            caipiao['qihao'] = qihao
            caipiao['red_ball'] = red_ball
            caipiao['blue_ball'] = blue_ball
            yield caipiao
