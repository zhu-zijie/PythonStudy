import urllib.request
from http import cookiejar

filename = "cookie.txt"


# 获取cookie
def get_cookie():
    # 1. 实例化一个MozillaCookieJar对象
    cookie = cookiejar.MozillaCookieJar(filename)
    # 2. 创建handler对象
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 3. 创建opener对象
    opener = urllib.request.build_opener(handler)
    # 4. 请求网址
    response = opener.open("https://www.baidu.com")
    # 5. 保存cookie到文件
    cookie.save()


# 使用cookie
def use_cookie():
    # 1.实例化MozillaCookieJar对象
    cookie = cookiejar.MozillaCookieJar()
    # 2. 加载cookie文件
    cookie.load(filename)
    print(cookie)


if __name__ == '__main__':
    # get_cookie()
    use_cookie()
