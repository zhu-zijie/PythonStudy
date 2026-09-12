# 几乎没有免费下载的歌曲，自行准备cookie
# 2026/09/12 update

# 代码逻辑
'''
加密代码
function() {
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
}();

'''
# 分析
'''
分析：
评论：params和encSecKey是两个参数，需要通过get_params和get_encSecKey方法获取
var bVj1x = window.asrsea(JSON.stringify(i6c), bse8W(["流泪", "强"]), bse8W(RR7K.md), bse8W(["爱心", "女孩", "惊恐", "大笑"]));
    params: bVj1x.encText,
    encSecKey: bVj1x.encSecKey

bse8W(["流泪", "强"]) = '010001'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
bse8W(RR7K.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
bse8W(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'

歌曲搜索：
csrf_token: 5d2041a48d11e68f70e0c675c7286a39

https://music.163.com/weapi/cloudsearch/get/web?csrf_token=5d2041a48d11e68f70e0c675c7286a39
var bVj3x = window.asrsea(JSON.stringify(i1x), bse1x(["流泪", "强"]), bse1x(RR1x.md), bse1x(["爱心", "女孩", "惊恐", "大笑"]));
e1x.data = j1x.cr2x({
        params: bVj3x.encText,
        encSecKey: bVj3x.encSecKey
            })

歌曲信息：
https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=da1db1553a7e3c98b6ef016e39c89d32

歌词：
https://music.163.com/weapi/song/lyric?csrf_token=da1db1553a7e3c98b6ef016e39c89d32


'''

import json
import requests
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
second = '010001'
third = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
fourth = '0CoJUm6Qyw8W8jud'

headers = {
    'cookie': 'NTES_P_UTID=xVmsD9PA77r5xYGbWJ9s7FZbqTIdeaKC|1788148194; NTES_PASSPORT=WabF9c9JDCV0yQjlE9MRR9lyh3dW5EtjewHNRf6gLbA5d3GbdnHABwpURPPiJRDl3Z3L4qndLl3PkT3sqsM1FBZNXldBYsO4LQVnduhJT9EUDCr7Mbv6zfd.nj_k1aXvBOmbbo3jnIrwHd0a_8RF4Vsj26ZCFfx4HPcGQc5FhDFryCzw1jZi_LhCA; P_INFO=zhupwr@163.com|1788148194|1|mail163|00&99|CN&1788148086&mail163#CN&null#10#0#0|158293&0|mail163&ntesgod_app&urs_mailaq|zhupwr@163.com; MAIL_AGGREGATION_PASSPORT_INFO="zhupwr@163.com|1788148194|1"; hb_MA-BFB6-AC673A756684_source=mail.163.com; JSESSIONID-WYYY=w39%2BUQ7qGON369ugMii8j8CIXdIINCSwWd8MyP1tnVYTefbVo8WPRM8pXZhm1%2BZq43eGVi%2BQCIisNRZWvIJM9oOuUrikDdjQImdSd6jOaMn1j9aTpH%2FHucGfiUsEdOSYC3Dtp%2FXFZErki%2Fv%5C1SxPjwunXfB%5C8nypymAml%2FiU1%2BDSUWj3%3A1789190812779; _iuqxldmzr_=32; _ntes_nnid=d663e8e9acdeff69a47831aff88d4de4,1789189012793; _ntes_nuid=d663e8e9acdeff69a47831aff88d4de4; NMTID=00OlJxda6doIN4lb0QjgIFojzTqRNIAAAGgk_m_-A; WEVNSM=1.0.0; WNMCID=rhybsj.1789189014072.01.0; WM_NI=UeeFQGCyHl3dtW9RgyzeqsrKqHOAzaJd2sa5tYYBgcLz56cCMdPrmxa9AcSgBopxf6widR%2FG%2BmKSH0WWCm%2FD3mICVCBr6Y9B1CZXMWVpJGT8o7aUQ4KBrMBquGBMTp%2F1QVY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8e1709899acbbf16395ef8fb2c45b938b9e82c94a8a92aed7bc48ac9387b6d92af0fea7c3b92a97bbaba7d44d81a7888db270b889f7b3e673babbbf94f141b39881a2f96b8abcfe94e43fb88797a3e66990a6fbd7e2498fbca093f074a3e78f84d26d82b1c099e53eb5b7acb3ae4de9b385b4cb3c95898d8eae50f1b387a4d54982aefababc4af39d96b9d05d96b086a8d734ade9afb6d440899ebeaec17bb7998eaed77cedef9fb7dc37e2a3; WM_TID=Ldi5MV%2FK3YlEVUFUABKZVMJPrtKxYZVZ; sDeviceId=YD-O70mngyi2WhEFgFQFULJQcNfqpPgKxGv; Hm_lvt_1483fb4774c02a30ffa6f0e2945e9b70=1789189020; HMACCOUNT=4F8D5B37A8F4E0AE; ntes_utid=tid._.orrFvHa8nyBBFwVEVFKMENcK64exKIqD._.0; __snaker__id=G2ZpwEfxvdUhqclG; gdxidpyhxdE=k%2B14RuKNzxRLB36UUJlZQt3kiTAD7EiZDqjd4%2Bh5acJKXltA1EW7Ap3aJIm8N207cT0PlVaRuOMeip7oACfN%2FH%2Bymo%5CD%5C5ntEs00SAjxgLzxz%5C85LezLym4acycoEfwwhTdy2%2FGMmVjq8cyUDs79ezH2fpU9rHQmxqiHKQdCUzlixkBP%3A1789189957847; MUSIC_U=00C208A5A745DFF374B2D80B19FBFFEAF7468E78D099FDECCEF97943051F12622B24B04DFC65315EFE3AC834EDD63669B77AED9C2B338CC53C68959C329CDB6780B46A0F04812C8E50B123C11B8DFAB3B79FE0E165BDDA5086F1F8CF69E50494D9A5253F8D18EEC7EB8D6415148BA1CA8043EA274620062FE8FBCA501742ABC09EB4E11164E6DE2D57123433BC516956DB4A8DB80F0842FA94DAFC6E58A8D8AABA75858D97202930B9BF304E5615FBA57312075C4A33506DC034F4EF41A9B5237EAA94A7FF5694340E4BE03E91B9FC879D137179A0421944946D06BF707230D7BA02338A03EE0A62A10419301239E5CDEFE0149B1E2A2C081EB4322824ADA587DEE54DF78C774143065F3BA6749F21A3145B1273BC1C89B008A03EC35D3669F9BA177BFA4B0F519420EE32AC4AD1D0131E280D6E0C0FABEC33E1FA535816395CFF5D76CEA0FC37749FCACA550660977C845F01165B53A679CDF3986DBA9688563E3AC1C8C6301F0ED25F617D129B458EBD3007C579E493D0B1DC3F7D2B8A1CF18D2A545766DD930400F5FFF62185D1AAD2204C2123046A5EE1AEB6DB3057B4A1B2; __csrf=9f45b50c7750ad13d93846f55b82ab9a; Hm_lpvt_1483fb4774c02a30ffa6f0e2945e9b70=1789189115; ntes_kaola_ad=1',
    'referer': 'https://music.163.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


def aes_encrypt(text, key):
    """AES CBC mode encryption"""
    # Convert to bytes
    text = text.encode('utf-8')
    key = key.encode('utf-8')
    iv = b'0102030405060708'
    # Create cipher and encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(text, AES.block_size))
    # Encode as base64
    return base64.b64encode(encrypted).decode('utf-8')


def get_encSecKey():
    # 固定i得到的encSecKey
    encSecKey = 'ab77b55c56b84e2e6a6bf1142b337d64205a51b4149806f9e7e340f09ac366cf339303ed095a0db9a6434a030fa7d87defcad67c6d8781c85a0bd74a8bb943c353bb60bd5ba33f7c4cf314bd6624e9089aabd500b98e016f259b4fca0aabf4860464b3afc0d4f5c54f9835a256d15811116ff03d8feb70ac604a19e77d6008a6'
    return encSecKey


def get_params(data):
    # 固定i的值
    i = '5r7Fojvz1584CFQ0'
    encText = aes_encrypt(data, fourth)
    encText = aes_encrypt(encText, i)
    return encText


def getData(commentData):
    first = json.dumps(commentData)
    encSecKey = get_encSecKey()
    params = get_params(first)
    data = {
        'params': params,
        'encSecKey': encSecKey
    }
    return data


# 下载歌曲
def downloadMusic(songId, songName, singerName):
    url = "https://music.163.com/weapi/song/enhance/player/url/v1"
    songDetailData = {
        "csrf_token": "da1db1553a7e3c98b6ef016e39c89d32",
        "encodeType": "aac",
        "ids": f"[{id}]",
        "level": "standard"
    }
    data = getData(songDetailData)
    try:
        resp = requests.post(url, data=data, headers=headers)
        downloadUrl = resp.json()['data'][0]['url']
        with open(f'data/{singerName}-{songName}.mp3', mode='wb') as f:
            f.write(requests.get(downloadUrl).content)
        print("下载完成！")
    except Exception as e:
        print(e)


# 获取歌曲列表
def getMusicList(singer):
    url = 'https://music.163.com/weapi/cloudsearch/get/web'
    musicData = {
        "csrf_token": "9f45b50c7750ad13d93846f55b82ab9a",
        "hlposttag": "</span>",
        "hlpretag": "<span class=\"s-fc7\">",
        "limit": "30",
        "offset": "0",
        "s": f"{singer}",
        "total": "true",
        "type": "1"
    }
    data = getData(musicData)
    resp = requests.post(url, data=data, headers=headers)
    songs = resp.json()['result']['songs']
    songList = []
    for song in songs:
        id = song['id']
        name = song['name']
        print(f"歌曲名：{name}，歌曲id：{id}")
        songList.append(dict(name=name, id=id))
    return songList


# 热评
def getComments(id):
    url = 'https://music.163.com/weapi/comment/resource/comments/get'
    commentData = {
        "rid": f"R_SO_4_{id}",
        "threadId": f"R_SO_4_{id}",
        "pageNo": "1",
        "pageSize": "20",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "csrf_token": ""
    }
    data = getData(commentData)

    resp = requests.post(url, data=data)
    comments = resp.json()['data']['hotComments']
    num = 1  # 初始化
    for comment in comments:
        print(f"********************************* 第{num}条热评！*********************************")
        print(f"{comment['user']['nickname']}: {comment['content']}")  # 评论内容
        print('\n')
        num += 1


# 下载歌词
def getLyric(songId, songName, singerName):
    url = 'https://music.163.com/weapi/song/lyric'
    lyricData = {
        "csrf_token": "da1db1553a7e3c98b6ef016e39c89d32",
        "id": songId,
        "lv": -1,
        "tv": -1
    }
    data = getData(lyricData)
    try:
        resp = requests.post(url, data=data, headers=headers)
        lyric = resp.json()['lrc']['lyric']
        with open(f'data/{singerName}-{songName}.lrc', mode='w', encoding='utf-8') as f:
            f.write(lyric)
        print("歌词下载完成！")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    singerName = input("请输入歌手的姓名：")
    songList = getMusicList(singerName)
    while True:
        flag = True  # 标记是否找到歌曲
        id = int(input("请输入歌曲id（0.结束任务！）："))
        if id == 0:
            break

        for song in songList:
            songName = song['name']
            songId = song['id']
            if songId == id:
                while True:
                    flag = False  # 标记找到歌曲
                    choice = int(input("请输入您的选择（0.取消任务 1.下载歌曲 2.获取热评 3.下载歌词）："))
                    if choice == 0:
                        break
                    elif choice == 1:
                        downloadMusic(songId, songName, singerName)
                    elif choice == 2:
                        getComments(songId)
                    elif choice == 3:
                        getLyric(songId, songName, singerName)
                    else:
                        print("输入有误！")
        if flag:
            print("您输入的歌曲id有误！")
    print("感谢您的使用！")