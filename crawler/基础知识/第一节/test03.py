import requests

url = "https://fanyi.baidu.com/sug"
word = input("请输入你要查询的单词：")
data = {

    "kw": word
}
resp = requests.post(url, data=data)#发送post请求

print(resp)
print(resp.json())#将服务器返回的数据处理成json
resp.close()