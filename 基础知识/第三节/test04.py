import json

import requests
import aiohttp
import asyncio
import aiofiles

# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

async def aiodownload(cid, book_id, title):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open("novel/"+title+".txt", mode = "w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])

async def getCatalog(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Referer": "https://dushu.baidu.com/pc/reader?gid=4306063500&cid=1569782244"  # 防盗链：溯源,当前请求的上一级是谁
    }
    resp = requests.get(url, headers = headers)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        #准备异步任务
        task = asyncio.create_task(aiodownload(cid, book_id, title))
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+book_id+'"}'
    asyncio.run(getCatalog(url))
