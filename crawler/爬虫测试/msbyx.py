# 爬取马士兵商城的数据保存到数据库

import pymysql
import requests


def get_data(index):
    url = f'https://you-gateway.mashibing.com/mall/product/app/product/page?pageIndex={index}&length=20'
    resp = requests.get(url)
    return resp.json()


def parse_data(data):
    items = data['data']['records']
    lst = []
    for item in items:
        lst.append((item.get('id'), item.get('name'), item.get('startingPrice')))

    return lst


# 保存数据到数据库
def save_data(sql, lst):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='msbyx')
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, lst)
    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()


if __name__ == '__main__':
    for i in range(1, 3):
        data = get_data(i)
        lst = parse_data(data)
        sql = 'insert into yx values(%s, %s, %s)'
        save_data(sql, lst)
    print("保存完毕！ ")
