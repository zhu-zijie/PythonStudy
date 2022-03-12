# 1.获取contId
# 2.拿到VideoStatus返回的json
# 3.srcUrl链接进行修改
# 4.下载视频

import requests

# 拉去视频的网址
url = "https://www.pearvideo.com/video_1753748"
# 1.获取contId
contId = url.split('_')[1]

VideoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.9412371536144419"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Referer": url   #防盗链：溯源,当前请求的上一级是谁
}

resp = requests.get(VideoStatusUrl, headers = headers)
# print(resp.text)
dic = resp.json()

srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, "cont-"+contId)

# 下载视频
with open("a.mp4", mode="wb") as file:
    file.write(requests.get(srcUrl).content)
print("Over!!!")
resp.close()
file.close()