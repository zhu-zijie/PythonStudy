import json

import requests
import random
import string
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

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

'''
分析：
params和encSecKey是两个参数，需要通过get_params和get_encSecKey方法获取
var bVj1x = window.asrsea(JSON.stringify(i6c), bse8W(["流泪", "强"]), bse8W(RR7K.md), bse8W(["爱心", "女孩", "惊恐", "大笑"]));
    params: bVj1x.encText,
    encSecKey: bVj1x.encSecKey

bse8W(["流泪", "强"]) = '010001'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
bse8W(RR7K.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
bse8W(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'




'''
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

first = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
second = '010001'
third = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
fourth = '0CoJUm6Qyw8W8jud'

headers = {
    'cookie': 'NMTID=00OTlmM7WjvWABVNETAsBcsWXtWtOwAAAGTP5y3uQ; JSESSIONID-WYYY=WE5bZZPZeC%5Ctum6ABVFYPMNv%2FpHI0%2Bb6SyBmMCvu8bA1fR2AJaEY%5CCahXO273wBz5O5HZWTZJ8%5CZNJsQMgb%2FxlyB%2FoAVOeWWsWcUCXB9u%2FcZWcEipVN3nR8%2FnCUVQExHQrDeb%5CRvdwspCkgTlK8ozMW%5CgMsME20QCJ2wVNXOjRq%5CmwcB%3A1731940855961; _iuqxldmzr_=32; _ntes_nnid=4e58a15dbc3498ba3ade6ad5a351af88,1731939055981; _ntes_nuid=4e58a15dbc3498ba3ade6ad5a351af88; WEVNSM=1.0.0; WNMCID=qqfphp.1731939056826.01.0; WM_NI=8Cs7p6jY6QfrWfs3d%2BwAH5eP0heJuDuEUOS2la%2FeFqfDGkSSjCy1THsbcw3V4g4qyTMJqHgsTr3yL%2BBnYa1R7j9ZHzGROFKiQBnoEJmjTtJNIW7J0xqwaARn9lBuX9RlMnk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccce6f89eaa5abc74092a88fa3d84a938a9b83db54f4aee198b644ae95fe88b72af0fea7c3b92afc9dbdd8f33eaa87fab2e57a95babdd4e721b59f88d6e85cf4b8ababf850b79b9bb0d23ab0bfe186c57ba69c898cd259aa9db7d2d744b1bead98b25ef8b9fc92fc608f96bfa9e67998aefd9acf2182b29782b45af5b6f7bbcb72858e81a7ca63939ea290c842afb69c95c9468b89f9abb374b3a9afa2d166fbb48e96db3392b4838fea37e2a3; WM_TID=xx%2B0BkKMJGpEUUFBFAOSDg6%2Fk%2FSmLzkp; __snaker__id=gX6pszJu4bCZinGf; gdxidpyhxdE=0scPa5q37zgWGjDAnHwH%5C0SoWsDqWHDkvjh0YoL4BnfV%2FMT9YohhjOf3L9uPi3eBPC1sTA4WT5LMARl3CaoIYJ%2FfxyYJQ8XOdZMwQ2vRq917bB%5CXm0gI03eRMB15hKbSubzMh%5Ch5Opl%5CNN5wvqj5Pga18hDDNiB6e63JzPIJhq9q7Sv7%3A1731939975489',
    'referer': 'https://music.163.com/song?id=2638631898',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


def a(a):
    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    c = ""
    for d in range(a):
        e = int(random.random() * len(b))
        c += b[e]
    return c


def b(a, b):
    c = b.encode('utf-8')
    d = b'0102030405060708'
    e = a.encode('utf-8')
    cipher = AES.new(c, AES.MODE_CBC, d)
    encrypted = cipher.encrypt(pad(e, AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')


def c(a, b, c):
    rsa_key = RSA.construct((int(c, 16), int(b, 16)))
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(a.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')


def d(d, e, f, g):
    h = {}
    # i = a(16)
    i = 'uMdVtJ5vSxRlCM2H'
    h['encText'] = b(d, g)
    h['encText'] = b(h['encText'], i)
    h['encSecKey'] = c(i, e, f)
    return h


def e(a, b, d, e):
    f = {}
    f['encText'] = c(a + e, b, d)
    return f


def get_encSecKey():
    encSecKey = d(first, second, third, fourth)['encSecKey']
    return encSecKey


def get_params():
    params = d(first, second, third, fourth)['encText']
    return params


if __name__ == '__main__':
    # 获取encSecKey
    encSecKey = get_encSecKey()
    # 获取params
    params = get_params()

    data = {
        'params': params,
        'encSecKey': encSecKey
    }

    resp = requests.post(url, headers=headers)

    print(data)
    print(resp.text)
