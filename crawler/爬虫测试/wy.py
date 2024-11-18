import requests
from Cryptodome.Cipher import AES
from base64 import b64encode
import json

# 加密代码
'''


buV3x(["流泪", "强"])
'010001'
buV3x(Rg7Z.md)
'00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
buV3x(["爱心", "女孩", "惊恐", "大笑"])
'0CoJUm6Qyw8W8jud'


function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
'''

e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "HYGZuaCxycd6KCw9"  # 手动固定

headers = {
    'cookie': 'NMTID=00O6j1Bh5pZOvMoQEkKgIvpTTgfjQ4AAAGAay1cVg; _ntes_nnid=b31f49eb27d22dcb60a94843372c433d,1651065587582; _ntes_nuid=b31f49eb27d22dcb60a94843372c433d; WEVNSM=1.0.0; WNMCID=utnvzz.1651065590822.01.0; WM_TID=DHS%2BhhhY0PZERFFVQUfFBDjbWaOW01xR; __csrf=ec623bb8af85bb072a2f4bb86ec0f8cd; MUSIC_U=c6c38d4a65df466eb8e147df132c4842fd1298f0097873e516cf9e8fe2db08c9c84e8a4f4ba4f13e0810b1fde2140d597140b1208feb40d6c8d4657e893eeaeb19d751b7953c76e7d4dbf082a8813684; _iuqxldmzr_=32; WM_NI=0LcoGtKKUqWTlMkn9MAZYVwwzlWB%2FqDyZ6C5rTDMc4laAfiXzhE5rZEzBboSwdpr3cIt3VeXq%2BVSXQ8gvbJ0b1PzQCSDdL1GtEuNDFBRPH7KgKD4BNk%2FWdhIqIsi563XZk8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9af14ef1b4a9a2c6449ab88ba3c84e969f9aacc84a8a97af85e26fa8eefb8bae2af0fea7c3b92af494ad90c68089959b92d660b093a58fbc47838697b7f67dbab499a3ae7b88a796d7c23fb28c8caee240b0bf8f87ec54bab88bd6f15287a68e83ee59b5bcc093b2698bacfdb7e854b3f59ab4db5bfcb9ba83c93ca2efa09bd449919cacadb44db89bbbafc74e828ea0a9b641a5958cd5c146a9f19985eb43b397bd8ab83ef188968cbb37e2a3; playerid=92112125; JSESSIONID-WYYY=606NCXEbtfWPob3e%5CEOPdPUQG8%2FOAI3euyNBt6r017kgGDxawXxtnR%5Cc%2FJFw2E0hZgP3dQKbtiIwSIk8e3OvO9thPp42HUGO%5CJP%2FOBslIxVw0r%5C9%5CwWiNVMVejHUSq9IqB4j3buK%5C5fObD5ornOe67JBFTTMCZu%5CTripVJEAG9QeVivz%3A1651744256418; _dd_s=logs=1&id=97075300-f2cb-438f-a5a3-f7dc28347530&created=1651742456154&expire=1651743754236',
    'origin': 'https://music.163.com/',
    'referer': 'https://music.163.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}


# 得到encSecKey
def get_encSecKey():
    return "999a773a6efa1df654605807bcf7b2d59beda2c864c29815b2f2a27be75d9ae82f7ed5e3a0f612912fee805d816f5f142fb1d6489d23153d152fdf9c1c5dcbe1419615557f55cae34fa63a50fa1a35777b9a0282d9fa43c37eb6edadaee1b85c14e342ed59a837c9eb3faa1f3f513dceb1f5ecf792f052ac5d4d861f8d832078"


# 转化为16的倍数
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# 得到params
def enc_params(data, key):
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data.encode('utf-8'))  # 加密
    return str(b64encode(bs), 'utf-8')


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回params


def get_comment(id, name):
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    # 参数列表，获取歌曲，评论等均需要修改
    data = {
        'csrf_token': "ec623bb8af85bb072a2f4bb86ec0f8cd",
        'cursor': "-1",
        'offset': "0",
        'orderType': "1",
        'pageNo': "1",
        'pageSize': "20",
        'rid': f"R_SO_4_{id}",
        'threadId': f"R_SO_4_{id}"
    }
    # 请求参数
    data = {
        'params': get_params(json.dumps(data)),
        'encSecKey': get_encSecKey()
    }
    resp = requests.post(url, data=data)
    # 2.解析数据
    hotComments = json.loads(resp.text)['data']['hotComments']
    num = 1
    for hotComment in hotComments:
        print(f"*********************************{name}的第{num}条热评！*********************************")
        print(hotComment['content'])
        print('\n')
        num += 1


# 接收的为字典
def get_data(data):
    data = {
        'params': get_params(json.dumps(data)),
        'encSecKey': get_encSecKey()
    }
    return data


# 显示歌曲信息
def get_song_list(singer):
    url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    song_data = {
        "hlpretag": '<span class="s-fc7">',
        'hlposttag': '</span>',
        'id': '31445772',
        's': f'{singer}',
        'type': '1',
        'offset': '0',
        'total': 'true',
        'limit': '30'
    }

    resp = requests.post(url, headers=headers, data=get_data(song_data))
    # print(resp.text)
    songs = json.loads(resp.text)['result']['songs']
    num = 1
    song_list = []
    for song in songs:
        id = song['id']
        name = song['name']
        print(f"第{num}首：", name, id)
        song_list.append(dict(name=name, id=id))
        num += 1
    return song_list


# 下载歌曲
def download_song(id, name, singer):
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    data = {
        "ids": f"[{id}]",
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": "ec623bb8af85bb072a2f4bb86ec0f8cd"
    }
    resp = requests.post(url, headers=headers, data=get_data(data))
    # print(resp.text)
    # 解析数据
    try:
        url = json.loads(resp.text)['data'][0]['url']
        response = requests.get(url).content
        with open('song/' + name + '-' + singer + '.mp3', mode='wb') as file:
            file.write(response)
            print(name + '-' + singer + " 下载完毕！")
    except:
        print("您还不是会员！")


# 获取歌词
def get_lyric(id):
    url = 'https://music.163.com/weapi/song/lyric?csrf_token='
    data = {
        "id": f'{id}',
        "lv": -1,
        "tv": -1,
        "csrf_token": ""
    }
    resp = requests.post(url, data=get_data(data))
    # print(resp.text)
    lyric = json.loads(resp.text)['lrc']['lyric']
    print(lyric)


def main():
    # 1.搜索歌手获取歌曲信息和id
    singer = input('请输入歌手名字：')
    song_list = get_song_list(singer)
    shuru = input("请输入歌曲的名字或id:")
    flag = False
    for song in song_list:
        name = song['name']
        id = str(song['id'])
        if shuru == id or shuru == name:
            flag = True
            choice = int(input("请输入你的选择（1：获取评论，2：下载歌曲，3：获取歌词）>"))
            if choice == 1:
                # 2.根据id获取歌曲的热评
                get_comment(id, name)
            elif choice == 2:
                # 3.根据id下载歌曲
                download_song(id, name, singer)
            elif choice == 3:
                # 4.获取歌词
                get_lyric(id)
            else:
                break
            if True:
                break
    if not flag:
        print("你的输入有误，请重新输入！")


if __name__ == '__main__':
    main()
