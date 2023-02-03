# -*- coding:utf-8 -*-
import execjs
import requests
import re

# 获取数据
url = 'https://music.163.com/discover/toplist?id=3778678'
resp = requests.get(url)
# print(resp.text)
headers = {
    'cookie': 'NMTID=00O6j1Bh5pZOvMoQEkKgIvpTTgfjQ4AAAGAay1cVg; _ntes_nnid=b31f49eb27d22dcb60a94843372c433d,1651065587582; _ntes_nuid=b31f49eb27d22dcb60a94843372c433d; WEVNSM=1.0.0; WNMCID=utnvzz.1651065590822.01.0; WM_TID=DHS%2BhhhY0PZERFFVQUfFBDjbWaOW01xR; __csrf=ec623bb8af85bb072a2f4bb86ec0f8cd; MUSIC_U=c6c38d4a65df466eb8e147df132c4842fd1298f0097873e516cf9e8fe2db08c9c84e8a4f4ba4f13e0810b1fde2140d597140b1208feb40d6c8d4657e893eeaeb19d751b7953c76e7d4dbf082a8813684; _iuqxldmzr_=32; WM_NI=%2FdjiKa6TfVxNwDOHHx39bv7%2Bavi%2FXiDplK5ZMYSFYOMmkIsocyw4yd%2FDFIf9nw8P9RyQd7blNVs1FcE2grgzbfkJCr9%2BrdyTVWg%2Bk462VFOjx58nR%2Bj2vavrkpiy3ShYV24%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebaf240948cfb89bc3d86e78fb7d84b829a9b86c15ba18a85aaea5cfc9586a3c72af0fea7c3b92aedbca68aca6bf68caab7fb46b59c81a9cb74f1e7ae97b621a3aaa7d0db6388b0a4acb8528f879da7dc458fb3a5aaf265a1a7b9d5fc70ed9c8aaae533aea9f8b1bc5abb8facd8e1688e8abdd2c56987eea993e672a2baa5abc27afbf5be85fc609689a9ccea40f6ee9aa7ce62bcebf88fd121aaeeba82f57aa9b0a79ab259ac879ad3b737e2a3; JSESSIONID-WYYY=0ChIF0fSjBFkujSb%2Bdzsy4NmMW89A8h%2Fx%5CGXJ3ltFvZK5ahPmerRb7cwvqHdroieJa485JMkK6xMO97Gj4YqrUosqiBXKhdh9sgpOMu2rr%2F9hs%2FIlCgK11w1sB9wA7Gt3EhiWaDAsRxu7Stv3mWb31ElnXv%2F9wmFgsEnGMqsN64CeCxZ%3A1651496249760; playerid=85463784; _dd_s=logs=1&id=e06245ce-fff8-4e97-abf3-226d5b317783&created=1651494450776&expire=1651496848470',
    'origin': 'https://music.163.com/',
    'referer': 'https://music.163.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}
# 解析数据
lis = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', resp.text, re.S)

# 下载数据
js = open('demo.js', mode='r', encoding='utf-8').read()
ctx = execjs.compile(js)
for li in lis:
    href = li[0]
    title = li[1]
    result = ctx.call('start', href)
    # print(result)
    url1 = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=ec623bb8af85bb072a2f4bb86ec0f8cd'
    data = {
        'csrf_token': 'ec623bb8af85bb072a2f4bb86ec0f8cd',
        'params': result['encText'],
        'encSecKey': result['encSecKey']
    }
    response = requests.post(url1, headers=headers, data=data)
    # print(response.text,title)
    song_url = response.json()['data'][0]['url']
    try:
        resp1 = requests.get(song_url).content
    except:
        print(title+"无法下载！")
        continue
    with open('song/'+title+'.mp3', mode='wb') as file:
        file.write(resp1)
        print(song_url, title+"下载完毕！")
