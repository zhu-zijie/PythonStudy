import requests
import uuid
import time

url = "https://votes.10yan.com.cn/index.php?m=content&c=index&a=vote"
headers = {
    "Referer": "https://votes.10yan.com.cn/show-112-70052-1.html",
    "Content-Type": "application/x-www-form-urlencoded",
    "Sec-Fetch-Mode": "cors",
    # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/4G Language/en",
    "Origin": "https://votes.10yan.com.cn",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Host": "votes.10yan.com.cn",
    "Sec-Fetch-Dest": "empty",
    "Content-Length": "91",
    "Sec-Fetch-Site": "same-origin"
}
def generate_userid():
    return str(uuid.uuid4()).replace('-', '_')

# data = {
#     "newsid": 70052,
#     # "ip": "39.144.208.97",
#     "phone": "undefined",
#     "userid": "o_QmPuP31W9pJBOD_e9DKr02r1Zo",
#     "catid": 112
# }

def shua(times):
    proxies = {
        "http": "http://58.20.248.139:9002",
        # "https": "http://your_proxy_ip:your_proxy_port"
    }
    for i in range(times):
        userid = generate_userid()
        for j in range(3):
            data = {
                "newsid": 70052,
                "phone": "undefined",
                "userid": userid,
                "catid": 112
            }
            resp = requests.post(url, headers=headers, data=data, proxies=proxies)
            print(resp.json())
            time.sleep(1)
        time.sleep(5)


if __name__ == '__main__':
    shua(100)

