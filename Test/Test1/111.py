import json
import requests
import execjs

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
    'cookie': 'NMTID=00O6j1Bh5pZOvMoQEkKgIvpTTgfjQ4AAAGAay1cVg; _ntes_nnid=b31f49eb27d22dcb60a94843372c433d,1651065587582; _ntes_nuid=b31f49eb27d22dcb60a94843372c433d; WEVNSM=1.0.0; WNMCID=utnvzz.1651065590822.01.0; WM_TID=DHS%2BhhhY0PZERFFVQUfFBDjbWaOW01xR; __csrf=ec623bb8af85bb072a2f4bb86ec0f8cd; MUSIC_U=c6c38d4a65df466eb8e147df132c4842fd1298f0097873e516cf9e8fe2db08c9c84e8a4f4ba4f13e0810b1fde2140d597140b1208feb40d6c8d4657e893eeaeb19d751b7953c76e7d4dbf082a8813684; _iuqxldmzr_=32; WM_NI=%2FdjiKa6TfVxNwDOHHx39bv7%2Bavi%2FXiDplK5ZMYSFYOMmkIsocyw4yd%2FDFIf9nw8P9RyQd7blNVs1FcE2grgzbfkJCr9%2BrdyTVWg%2Bk462VFOjx58nR%2Bj2vavrkpiy3ShYV24%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebaf240948cfb89bc3d86e78fb7d84b829a9b86c15ba18a85aaea5cfc9586a3c72af0fea7c3b92aedbca68aca6bf68caab7fb46b59c81a9cb74f1e7ae97b621a3aaa7d0db6388b0a4acb8528f879da7dc458fb3a5aaf265a1a7b9d5fc70ed9c8aaae533aea9f8b1bc5abb8facd8e1688e8abdd2c56987eea993e672a2baa5abc27afbf5be85fc609689a9ccea40f6ee9aa7ce62bcebf88fd121aaeeba82f57aa9b0a79ab259ac879ad3b737e2a3; JSESSIONID-WYYY=0ChIF0fSjBFkujSb%2Bdzsy4NmMW89A8h%2Fx%5CGXJ3ltFvZK5ahPmerRb7cwvqHdroieJa485JMkK6xMO97Gj4YqrUosqiBXKhdh9sgpOMu2rr%2F9hs%2FIlCgK11w1sB9wA7Gt3EhiWaDAsRxu7Stv3mWb31ElnXv%2F9wmFgsEnGMqsN64CeCxZ%3A1651496249760; playerid=85463784; _dd_s=logs=1&id=e06245ce-fff8-4e97-abf3-226d5b317783&created=1651494450776&expire=1651496848470',
    'origin': 'https://music.163.com/',
    'referer': 'https://music.163.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

data = {
    'encText': 'kHGSfuyNpyuve8rD7OwPacbapCD+78Hre5SsACymsDzNBVo8Av4XgKybSo2s9fS53z2A8/+nCfCuY0+NakX0FbZ9+7FOuJbWydK/BSNlIl45CBJmN5Wir3TxtxaayAY8qh1y8u3tEL4nWs9aTyGOzZMNlb09XNRrvqToLJLAirilm1CLgEXmjlDC6YD33B8sgTSQiloLirTF/phGp8MvUw==',
    'encSecKey': '763bc461f963df891d66cc3331c063e19677f50bbbdcdc69045fa95da1c7d1245dc998318bb39a6b92763696067c45d0842c1edfcef4f4cf3e88b66468a144ed939139281cf9c0341c057c4d822818f4332e86ffd9516979000fbeab92a0519dcd8c2aff3b20d18d518e28369467afeade3618f4456663c38ce596983575a29d'
}


resp = requests.post(url, data=data)
print(resp.text)