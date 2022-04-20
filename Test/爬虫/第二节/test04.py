#xpath解析

from lxml import etree

xml = '''
<html>
    <head>
        <name>周大生</name>
        <name>周芷若</name>
    </head>
    <body>
        <name>周杰伦</name>
        <name>蔡依林</name>
        <div>
            <name>林俊杰</name>
        </div>
        <span>
            <name>汪苏泷</name>
        </span>
        <nick>王力宏</nick>
  </body>
</html>
'''

tree = etree.XML(xml)
# result = tree.xpath("/html/head/name/text()")#/表示层级关系，第一个是根节点。text()表示拿文本
# result = tree.xpath("/html/head")
# result = tree.xpath("/html/body/div/name/text()")
# result = tree.xpath("/html/body//name/text()")#//表示拿后代
result = tree.xpath("/html/body/*/name/text()")# *通配符
# @xxx:拿到属性值，@属性

print(result)
