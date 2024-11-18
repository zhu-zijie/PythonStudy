from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
import time

# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网址
web.get("http://lagou.com")

# 3.找到元素点击它
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
# 点击
el.click()

time.sleep(1)#睡眠1s,浏览器加载时间

# 4.找到输入框输入Python,通过搜索/回车
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("Python", Keys.ENTER)

time.sleep(1)

# 查找存放数据的位置，用于数据的提取
li_list = web.find_elements(By.XPATH, '//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element(By.TAG_NAME, 'h3').text
    job_price = li.find_element(By.XPATH, './div/div/div[2]/div/span').text
    company = li.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    print(company, job_name, job_price)