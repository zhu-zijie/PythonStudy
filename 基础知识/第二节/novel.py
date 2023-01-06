# 1. 登录账号，服务器返回cookie
# 2. 使用cookie获取书架上的数据

import requests

# 会话
session = requests.session()

url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "18471469010",
    "password": "zzj990927"
}
resp1 = session.post(url, data=data)
resp1.encoding = resp1.apparent_encoding
# print(resp1.cookies)

resp2 = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp2.json())

# 方法2
# resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={"cookie": "GUID=49bb7b3c-f037-4fa7-8210-43ab354d7dcb; c_channel=0; c_csc=web; accessToken=avatarUrl=https%3A%2F%2Fcdn.static.17k.com%2Fuser%2Favatar%2F10%2F50%2F78%2F93827850.jpg-88x88%3Fv%3D1647136916000&id=93827850&nickname=%E4%B8%8D%E7%9B%B8%E4%BA%A4%E7%9B%B4%E7%BA%BF&e=1662690327&s=7607484c9cffbc31; _dd_s=logs=1&id=502fb9f9-9770-4112-b257-daad44cb2c1f&created=1647139077189&expire=1647140007031"})
# print(resp.text)