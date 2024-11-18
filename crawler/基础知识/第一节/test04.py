import requests

url = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(url, params=param, headers=header)
#print(resp.request.url)
print(resp.json())
resp.close()