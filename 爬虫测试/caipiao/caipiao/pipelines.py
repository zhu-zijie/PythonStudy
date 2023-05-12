# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CaipiaoPipeline:
    def open_spider(self, spider):
        self.f = open("caipiao.csv", mode='a', encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        self.f.write(f"{item['qihao']}, {'_'.join(item['red_ball'])}, {item['blue_ball']}\n")
        return item
