# 导入webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 导入time
import time

# 指定chromedriver位置
chrome_service = Service(r'/user/local/bin')
# 后台开启浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
# 打开谷歌浏览器
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# 在浏览器中输入url并打开
driver.get("http://10.0.9.144:18080/")
# 浏览器最大化
driver.maximize_window()

# 等待2秒
time.sleep(2)
# driver.find_element定位元素，send_keys输入用户名
driver.find_element(By.ID, "emailValue").send_keys('admin')
driver.find_element(By.ID, 'pwdValue').send_keys('Cloudwise_654321')
driver.find_element(By.ID, 'loginBtn').click()
time.sleep(5)
# 关闭浏览器结束进程
driver.quit()
