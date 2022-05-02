import requests
from lxml import etree
import csv
from time import sleep
import os
from concurrent.futures import ThreadPoolExecutor

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
f = open('tulishe.csv', mode='w', encoding='utf-8')
csvwriter = csv.writer(f)


def download_one_page(url):
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    post_list = tree.xpath('//div[@id="posts"]/div')
    print('------开始爬取第' + str(page_num) + '页------')
    for div in post_list:
        try:
            link = div.xpath('./div/a/@href')[0]  # 文章链接
            title = div.xpath('./div/a/@title')[0]  # 标题
            img = div.xpath('./div/a/img/@data-src')[0]  # 封面图
            img1 = img.split('=')[1]  # 处理封面图url前缀
            img2 = img1.split('&')[0]  # 处理封面图url后缀
            print('------开始下载---【' + title + '】---图片------')
            headers2 = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
                'Referer': link
            }
            # print(link,title)
            # 开始请求详情页数据
            page2_text = requests.get(url=link, headers=headers).text
            tree2 = etree.HTML(page2_text)
            item = tree2.xpath('/html/body/div[2]/div/div[2]/div/article/header/div/span[3]/a/text()')  # 分类
            article_tags = tree2.xpath('/html/body/div[2]/div/div[2]/div/article/div[3]/a')  # 标签组
            tags = []
            for a in article_tags:
                tag = a.xpath('./text()')
                tags.append(tag)
            # print(item,tags)
            all_pic_url = []  # 详情页全部图片
            pic_urls = []
            pic_list = tree2.xpath(
                '//*[@id="gallery-2"]/div[@class="gallery-item gallery-fancy-item"]')  # 详情页4图
            a = 0
            for div in pic_list:
                try:
                    pic_url = div.xpath('./a/@href')[0]
                    pic_urls.append(pic_url)
                    all_pic_url.append(pic_url)  # 添加预览4图片到all_pic_url_

                    # 下载4预览图
                    a = int(a) + 1
                    # print('--开始下载第', a, '预览图片--')
                    img_data = requests.get(url=pic_url, headers=headers2).content

                    dir_name = pic_url.rsplit('.')[2].rsplit('/', 1)[0]
                    if not os.path.isdir(dir_name):
                        try:
                            original_umask = os.umask(0)
                            os.makedirs(dir_name, mode=0o777)
                        finally:
                            os.umask(original_umask)

                    with open(pic_url.split(".", 2)[2], 'wb') as fp:
                        fp.write(img_data)
                except Exception as e:
                    continue
            # print('--', title, '-------', len(pic_urls), '张预览图--下载完成------')

            pic_list2 = tree2.xpath(
                '//*[@id="gallery-2"]/div[@class="gallery-item gallery-blur-item"]')  # 详情页隐藏图
            pic_url3s = []
            for div in pic_list2:
                try:
                    pic_url = div.xpath('./img/@src')[0]
                    pic_url2 = pic_url.split('=')[1]  # 解析隐藏链接图片
                    pic_url3 = pic_url2.split('&')[0]  # 解析隐藏链接图片
                    pic_url3s.append(pic_url3)
                    all_pic_url.append(pic_url3)  # 添加隐藏图片到all_pic_url_
                    # 下载隐藏图
                    a = int(a) + 1
                    # print('--开始下载第', a, '隐藏图片--')
                    img_data = requests.get(url=pic_url3, headers=headers2).content
                    dir_name = pic_url3.rsplit('.')[2].rsplit('/', 1)[0]
                    if not os.path.isdir(dir_name):
                        try:
                            original_umask = os.umask(0)
                            os.makedirs(dir_name, mode=0o777)
                        finally:
                            os.umask(original_umask)
                    with open(pic_url3.split(".", 2)[2], 'wb') as fp:
                        fp.write(img_data)
                except Exception as e:
                    continue
            # print(title, '-------', len(pic_url3s), '张隐藏图--下载完成------')
            csvwriter.writerow([title, link, img2, item, tags, all_pic_url])  # 【标题；链接；封面图；分类；标签；详情页图片】保存到csv
            sleep(0.01)
            print(link, title, "爬取完毕！！！")

            # 下载封面图
            img_data = requests.get(url=img2, headers=headers2).content
            dir_name = img2.rsplit('.')[2].rsplit('/', 1)[0]

            if not os.path.isdir(dir_name):
                try:
                    original_umask = os.umask(0)
                    os.makedirs(dir_name, mode=0o777)
                finally:
                    os.umask(original_umask)
            with open(img2.split(".", 2)[2], 'wb') as fp:
                fp.write(img_data)
            print('--', title, '封面图------下载完成------')
        except Exception as e:
            continue

    print('第' + str(page_num) + '页，爬取完毕！！！')


# except Exception as e:
#     continue

if __name__ == '__main__':
    with ThreadPoolExecutor(100) as t:
        for page_num in range(1, 842):  # 一共841页
            t.submit(download_one_page, f'http://www.tulishe.com/all/page/{page_num}')

f.close()
print("恭喜，全部爬取完毕！！！（文件为当前目录的tulishe.csv）")