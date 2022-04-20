import requests
import json


url = 'https://api.zzzmh.cn/bz/v3/getData'

data = {
    'category': 0,
    'categoryId': 0,
    'color': 0,
    'current': 1,
    'resolution': 0,
    'size': 24,
    'sort': 0
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '85',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://bz.zzzmh.cn',
    'referer': 'https://bz.zzzmh.cn/index',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'

}

resp = requests.post(url=url, headers=headers, data=json.dumps(data))
resp.encoding = 'utf-8'
print(resp.text)