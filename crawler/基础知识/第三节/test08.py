from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
import time

web = Chrome()
web.get("http://lagou.com")
time.sleep(1)
el = web.find_element(By.XPATH, '//*[@id="cboxClose"]').click()#关闭弹窗
time.sleep(1)
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("Python", Keys.ENTER)
time.sleep(1)
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(1)

# 进入新的窗口
# 切换到最右端窗口
web.switch_to.window(web.window_handles[-1])

# 打印岗位的要求
job_detail = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
time.sleep(1)
# 关闭子窗口
web.close()
# 回到原窗口
web.switch_to.window(web.window_handles[0])
