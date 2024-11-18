import hashlib, time, requests, base64


def get_token():
    # 1.将/api/movie放到一个列表里
    args = ['/api/movie']
    # 2.在列表中加入当前的时间戳
    timestamp = str(int(time.time()))
    args.append(timestamp)
    # 3.将列表的内容用逗号进行拼接
    args = ','.join(args)
    # 4.将拼接的内容进行sha1编码
    sha1 = hashlib.sha1(args.encode('utf-8')).hexdigest()
    # 5.将编码的结果和时间戳进行拼接
    token = sha1 + ',' + timestamp
    # 6.将拼接的结果进行base64编码
    return base64.b64encode(token.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    for index in range(10):
        token = get_token()
        url = f'https://spa6.scrape.center/api/movie/?limit=10&offset={index * 10}&token={token}'
        resp = requests.get(url)
        print(resp.json())
