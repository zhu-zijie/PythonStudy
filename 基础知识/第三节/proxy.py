# 原理：通过一个第三方的机器发送请求

import requests

proxies = {
    "https:" "https://171.92.20.245:9000"
}
url = "https://www.baidu.com"
resp = requests.get(url, proxies=proxies)
print(resp.text)