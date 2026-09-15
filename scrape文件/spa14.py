# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2026/9/15 15:59
# @Author  : zijie
# @Desc    : https://spa14.scrape.center   网站的爬取，练习webAsssembly
# --------------------------------------

# 建表语句
"""
    CREATE DATABASE IF NOT EXISTS scrape DEFAULT CHARACTER SET utf8mb4;
    USE scrape;

    CREATE TABLE IF NOT EXISTS movies (
        id INT PRIMARY KEY,                  -- 接口返回的电影 id，作为主键
        name VARCHAR(255) NOT NULL,
        cover VARCHAR(500),
        categories VARCHAR(255),             -- 列表拼成字符串，如 "剧情,爱情"
        published_at VARCHAR(50),            -- 上映日期
        minute INT,                          -- 片长（分钟）
        score DECIMAL(3,1),
        regions VARCHAR(255),                -- 列表拼成字符串，如 "中国内地,中国香港"
        raw_json JSON,                       -- 原始 JSON 备份
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# 加密处
"""
    var n = (this.page - 1) * this.limit
    , e = this.$wasm.asm.encrypt(n, parseInt(Math.round((new Date).getTime() / 1e3).toString()));
"""

import requests, pywasm, time, pymysql, json

DB_CONFIG = {
    'host': '192.168.0.1',
    'port': 3306,
    'user': '',
    'password': '',
    'database': 'scrape',
    'charset': 'utf8mb4',
}

page = 10
all_movies = []

for i in range(page):
    offset = i * 10
    runtime = pywasm.core.Runtime()
    module = runtime.instance_from_file("./Wasm.wasm")
    sign = runtime.invocate(module, 'encrypt', [offset, int(time.time())])
    url = f"https://spa14.scrape.center/api/movie/?limit10&offset={offset}&sign={sign[0]}"
    response = requests.get(url)
    resp = response.json()
    movies = resp.get('results', [])
    all_movies.extend(movies)
    print(f"第 {i + 1} 页抓取到 {len(movies)} 条")

print(f"共抓取 {len(all_movies)} 条")

conn = pymysql.connect(**DB_CONFIG)
cur = conn.cursor()

sql = """
      INSERT INTO movies
      (id, name, cover, categories, published_at, minute, score, regions, raw_json)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY
      UPDATE
          name =
      VALUES (name), cover =
      VALUES (cover), categories =
      VALUES (categories), published_at =
      VALUES (published_at), minute =
      VALUES (minute), score =
      VALUES (score), regions =
      VALUES (regions), raw_json =
      VALUES (raw_json) \
      """

rows = []
for movie in all_movies:
    rows.append((
        movie.get('id'),
        movie.get('name'),
        movie.get('cover'),
        ','.join(movie.get('categories') or []),  # 列表 -> 字符串
        movie.get('published_at') or '未知',
        movie.get('minute'),
        movie.get('score'),
        ','.join(movie.get('regions') or []),  # 列表 -> 字符串
        json.dumps(movie, ensure_ascii=False),  # 原始 JSON 备份
    ))

try:
    cur.executemany(sql, rows)
    conn.commit()
    print(f"✅ 成功写入/更新 {cur.rowcount} 条记录")
except Exception as e:
    conn.rollback()
    print("❌ 写入失败：", e)
finally:
    cur.close()
    conn.close()
