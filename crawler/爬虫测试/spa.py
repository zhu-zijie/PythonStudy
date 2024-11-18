import hashlib, time, requests, base64


def get_token(args):

    # 1.在列表中加入当前的时间戳
    timestamp = str(int(time.time()))
    args.append(timestamp)
    # 2.将列表的内容用逗号进行拼接
    args = ','.join(args)
    # 3.将拼接的内容进行sha1编码
    sha1 = hashlib.sha1(args.encode('utf-8')).hexdigest()
    # 4.将编码的结果和时间戳进行拼接
    token = sha1 + ',' + timestamp
    # 5.将拼接的结果进行base64编码
    return base64.b64encode(token.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    # ['/api/movie']是参数
    args = ['/api/movie']
    for index in range(1):
        token = get_token(args)
        url = f'https://spa6.scrape.center/api/movie/?limit=10&offset={index * 10}&token={token}'
        resp = requests.get(url)
        results = resp.json()['results']
        for result in results:
            id = result['id']
            key = base64.b64encode(str(id).encode('utf-8')).decode('utf-8')
            detail_args = [f'/api/movie/{key}']
            detail_token = get_token(detail_args)
            detail_url = f'https://spa6.scrape.center/api/movie/{key}?token={detail_token}'
            print(detail_url)


# ViNWNiYjRkNWE1NzQ4NTg5NiwxNzMxOTM1Njkz

