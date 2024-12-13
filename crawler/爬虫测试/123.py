from DrissionPage import ChromiumPage
import requests
import re

# 抖音用户主页
main_url = 'https://www.douyin.com/user/MS4wLjABAAAA2SxrgkbkZyv40AX5DSGs2q1Z5pa4cuNoOIY9KARCkG8?from_tab_name=main'
# 创建一个浏览器对象
tab = ChromiumPage()
# 访问网址，这行产生的数据包不监听
tab.get(main_url)
# 开始监听，指定获取包含该文本的数据包
tab.listen.start('aweme/v1/web/aweme/post')

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'referer': 'https://www.douyin.com/'
}

for page in range(2):
    # 等待数据包加载
    resp = tab.listen.wait()
    # 获取响应数据
    info_json = resp.response.body

    aweme_list = info_json['aweme_list']
    for aweme in aweme_list:
        name = aweme['desc']
        # 规避几个特殊符号
        name = re.sub(r'[\/:*?"<>|]', '_', name)
        video_url = aweme['video']['play_addr']['url_list'][0]
        with open(f'data/{name}.mp4', mode='wb') as file:
            response = requests.get(video_url, headers=headers)
            file.write(response.content)
        print(name + "   保存完毕！")

    # 滚动到底部
    tab.scroll.to_bottom()

