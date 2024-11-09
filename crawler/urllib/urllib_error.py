import urllib.request
import urllib.error

url = "https://www.bilibili.com"
try:
    resp = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print("原因", e.reason)
    print("响应状态码", str(e.code))
    print("响应头数据", e.headers)
