import requests
import json

url = "http://117.145.189.131:48081/api/generate"
headers = {"X-API-Key": "yxjfl", "Content-Type": "application/json"}

data = {"model": "deepseek-r1:70b", "prompt": "描述一下新疆大学", "stream": False}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failedtogetresponse.Statuscode:", response.status_code)
