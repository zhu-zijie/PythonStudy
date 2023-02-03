# -*- coding:utf-8 -*-
"""
网易云音乐爬虫
功能：
"""
import requests
import execjs
import json

song_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
comment_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
down_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
ci_url = 'https://music.163.com/weapi/song/lyric?csrf_token='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
with open('./music_comments.js', 'r', encoding='utf-8') as f:
    Jsdata = f.read()

word = input("输入歌曲名称：")

song_ss = {"hlpretag": '<span class="s-fc7">', "hlposttag": "</span>", "s": word, "type": "1", "offset": "0",
           "total": "true", "limit": "30", "csrf_token": ""}
comment_ss = {"rid": "R_SO_4_{}", "threadId": "R_SO_4_{}", "pageNo": "1", "pageSize": "20", "cursor": "-1",
              "offset": "0", "orderType": "1", "csrf_token": ""}

song_ss = json.dumps(song_ss)

params1, eskey1 = execjs.compile(Jsdata).call('GEt_2', song_ss)
song_data = {
    'params': params1,
    'encSecKey': eskey1
}
#
song_list = requests.post(url=song_url, data=song_data, headers=headers).json()['result']['songs']

songS = []
b = 0
for song in song_list:
    name = song['name']
    songer = ','.join([ar['name'] for ar in song['ar']])
    songid = song['id']
    song_time = int(song['dt']) // 1000
    song_ = {
        'name': name,
        'songer': songer,
        'id': songid,
        'time': song_time
    }
    songS.append(song_)
    print(f'{b}.', name, '---', songer, f'  时长:{song_time} s')
    b += 1
i = int(input('请选择:'))
comment_ss = {"rid": f"R_SO_4_{songS[i]['id']}", "threadId": f"R_SO_4_{songS[i]['id']}", "pageNo": "1",
              "pageSize": "20", "cursor": "-1", "offset": "0", "orderType": "1", "csrf_token": ""}
s = json.dumps([songS[i]['id']])
down_ss = {"ids": s, "level": "standard", "encodeType": "aac", "csrf_token": ""}

# 评论
params2, eskey2 = execjs.compile(Jsdata).call('GEt_2', json.dumps(comment_ss))
comment_data = {
    'params': params2,
    'encSecKey': eskey2
}

# 下载
params3, eskey3 = execjs.compile(Jsdata).call('GEt_2', json.dumps(down_ss))
down_data = {
    'params': params3,
    'encSecKey': eskey3
}

hot_data_ = requests.post(url=comment_url, data=comment_data, headers=headers).json()['data']['hotComments']

url = requests.post(url=down_url, data=down_data, headers=headers).json()['data'][0]['url']
print("**********下载地址**********")
if url:
    print('下载地址:', url)
else:
    print('付费歌曲，无法下载！')
k = 1
print('**********歌曲热评**********')
for hot in hot_data_:
    user = hot['user']['nickname']
    conent = hot['content']
    like_ = hot['likedCount']
    print(k, '. @', user, ':\n', conent, '   ', like_, '赞同', '\n', sep='')
    k += 1

# 歌词
print('***********歌 词***********')
ci_ss = {"id": songS[i]['id'], "lv": -1, "tv": -1, "csrf_token": ""}
params4, eskey4 = execjs.compile(Jsdata).call('GEt_2', json.dumps(ci_ss))
ci_data = {
    'params': params4,
    'encSecKey': eskey4
}

ci_data_ = requests.post(url=ci_url, data=ci_data, headers=headers).json()
ci = ci_data_['lrc']['lyric']
print(ci)