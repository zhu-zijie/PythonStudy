import requests

query = input("请输入你喜爱的明星：")
url = f"https://www.sogou.com/web?query={query}"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(url, headers=header)
print(resp)
print(resp.text)
resp.close()




