from pyquery import PyQuery as pq

# 字符串的方式
html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample HTML Page</title>
    </head>
    <body>
        <h1>Welcome to My Website</h1>
        <p>This is a sample HTML page.</p>
        <ul>
            <li id='main'>Home</li>
            <li>About</li>
            <li>Contact</li>
        </ul>
    </body>
    </html>
'''
doc = pq(html)
print(doc('title').text())
print(doc('#main').text())

# url的方式
# doc = pq(url='https://cuiqingcai.com', encoding='utf-8')
# print(doc('title').text())

# 文件的方式
# doc = pq(filename='demo.html')
# print(doc('title').text())
