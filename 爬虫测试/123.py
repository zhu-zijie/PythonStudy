import re
import requests
li_obj = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?◎主　　演　(?P<actors>.*?)<br />◎简　　介<br />(?P<brief_introduction>.*?)'
                     r'<br />.*?<td style="WORD-WRAP:.*?href="(?P<download>.*?)">', re.S)
url = 'https://www.dytt89.com/i/105464.html'     # 拼接成子页面的url
resp = requests.get(url)
resp.encoding = "gbk"
# print(resp.text)
movie = li_obj.search(resp.text).group("movie")
actors = li_obj.search(resp.text).group("actors").replace("<br />　　　　　　", "&").replace("&middot;", "_")
brief_introduction = li_obj.search(resp.text).group("brief_introduction").strip()
download = li_obj.search(resp.text).group("download")
print(movie, actors, brief_introduction, download)