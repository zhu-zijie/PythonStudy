from urllib.request import build_opener
from urllib.request import ProxyHandler

# Set up a proxy handler with the specified proxy server
proxy = ProxyHandler({"https": "183.164.243.174:8089"})

# Create an opener object with the proxy handler
opener = build_opener(proxy)

# URL to be accessed
url = "https://www.baidu.com"

# Open the URL using the opener and read the response
resp = opener.open(url)
print(resp.read().decode("utf-8"))
