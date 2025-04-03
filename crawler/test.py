import requests

url = 'https://api.vvhan.com/api/wyMusic/热歌榜?type=json'
resp = requests.get(url)
print(resp.text)