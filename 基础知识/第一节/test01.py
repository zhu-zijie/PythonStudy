from urllib.request import urlopen

resp = urlopen("http://www.baidu.com")
#print(resp.read().decode("utf-8"))
with open("mybaidu.html", mode ='w', encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("Over")
resp.close()