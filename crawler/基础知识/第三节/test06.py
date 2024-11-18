# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome

# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网址
web.get("http://www.baidu.com")

print(web.title)