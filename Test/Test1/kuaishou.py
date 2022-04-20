'''
爬取快手视频
https://www.kuaishou.com/
'''

import requests
import json
import re
import os


# 处理请求头
headers = {
    'accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '656',
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_19df07f6588fb0767596ad275237eea1; userId=2198925574; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB5dUdND5RpuAN_mh6y_FAOYZTmlKjamh4FxNzuhX5J0Vn6tmRCyLfMdqVq0CBQYnlWAnnwG4XxkyTWBhny0zBXhnFXVoywqvvq65mQjUD53L63SGUA5wCIF8ykfGgIrvFSuwZKKSi-FP-H4W0UNjT3ovy3b-V7_hQ4FB0RTX1ooZGEZdikzU3xe0M1llBch4ThGk6R78Zhy7-6m1aK2uF_xoSS2UWrTnDahVDKzRYjzjLpJM-IiBn7Z8yz8aDReDcjXYn539UyM_-XgnBJSza4UPGjgUJaigFMAE; kuaishou.server.web_ph=a189ab8dba856ec1cbd517758f04f4dbc994; _dd_s=logs=1&id=35a1f9ca-e8d4-42f5-b3b6-c8707ee7e7ab&created=1650008052892&expire=1650013199283',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/search/video?searchKey=%E7%BE%8E%E5%A5%B3',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}
keyword = input("请输入你想下载的类型：")
page = int(input("请输入你想下载的页数："))

# 判断文件夹路径是否存在，没有就创建
path = "video/"+keyword+"/"
isExists=os.path.exists(path)
if not isExists:
    os.mkdir(path)
    print("文件夹创建成功")
else:
    print("文件夹已存在")

for pcursor in range(1,page):
    data = {
        "operationName":"visionSearchPhoto",
        "variables":{"keyword":keyword,"pcursor":str(pcursor),"page":"search", "searchSessionId": "MTRfMjE5ODkyNTU3NF8xNjUwMDE1NjUxMzk5X-e-juWls183OTc2"},
        "query":"query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    # 将data转化为json
    data = json.dumps(data)

    url = 'https://www.kuaishou.com/graphql'
    # post请求方式
    resp = requests.post(url, headers=headers, data=data)

    # 打印状态码
    # print(resp.status_code)
    print(f'----------开始下载第{pcursor}页----------')
    resp_json = resp.json()
    feeds = resp_json['data']['visionSearchPhoto']['feeds']
    for feed in feeds:
        title = feed['photo']['caption']    # 标题
        url = feed['photo']['photoUrl']     # 链接地址
        new_title = re.sub(r'[\/"?*:|\n]', '_', title)
        video_data = requests.get(url).content
        with open(path+new_title+'.mp4', mode='wb') as f:
            f.write(video_data)
        print("保存成功", new_title)


