from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

# 无头浏览器
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)

web.get("")
time.sleep(1)

# 定位到下拉列表
sel_el = web.find_element(By.XPATH, '')
# 对元素进行包装，包装成下拉菜单
sel = Select(sel_el)

# 让浏览器进行调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i)#按照索引进行切换
    time.sleep(2)
    table = web.find_element(By.XPATH, '')
    print(table.text)

print("运行完毕！")
web.close()

# 如何拿到页面源代码elements(经过页面加载以及js执行后的html)
print(web.page_source)