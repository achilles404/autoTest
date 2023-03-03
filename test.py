# 导入webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 导入time
import time

# 指定chromedriver位置
chrome_service = Service(r'/user/local/bin')
# 后台开启浏览器
chrome_options = Options()
# chrome_options.add_argument('--headless')
# 打开谷歌浏览器
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# 在浏览器中输入url并打开
driver.get("http://10.0.12.125:18080/#/portal/app")
# 浏览器最大化
driver.maximize_window()

# 等待2秒
time.sleep(2)
# driver.find_element定位元素，send_keys输入用户名
driver.find_element(By.ID, "emailValue").send_keys('admin')
driver.find_element(By.ID, 'pwdValue').send_keys('Cloudwise_654321')
driver.find_element(By.ID, 'loginBtn').click()
time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='用户中心']").click()
driver.find_element(By.XPATH, "//button[text()='全局工作台管理']").click()
time.sleep(3)


def addGongzuotai(name, enName):
    driver.find_element(By.XPATH, "//button[text()='新建工作台']").click()
    time.sleep(1)

    # driver.find_element(By.XPATH,
    #                     '/html/body/div[3]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys(
    #     "p工作台" + str(name))
    driver.find_element(By.XPATH,'//input[@id="name"and@maxlength="40"]').send_keys("p工作台" + str(name))
    driver.find_element(By.ID, "enName").send_keys("eName" + str(enName))
    driver.find_element(By.XPATH, "//button[text()='确定']").click()


for i in range(1):
    addGongzuotai(i, i)

time.sleep(5)
# 关闭浏览器结束进程
driver.quit()
