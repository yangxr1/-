#导入webdriver驱动
import time

from selenium import webdriver
# 导入Service服务
from selenium.webdriver.chrome.service import Service
# 导入显示等待
from selenium.webdriver.support.wait import WebDriverWait
# 导入expected_conditions 模块并取别名为ec
from selenium.webdriver.support import  expected_conditions as ec

#webdriver的路径
chrome_driver_path = r'C:\Users\肖老师\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe'
#固定搭配直接用就行了
service = Service(executable_path=chrome_driver_path)
#实例化浏览器
driver=webdriver.Chrome(service=service)
# 实例化显示等待，并设置超时时间为30秒
wait=WebDriverWait(driver,30)
# 设置浏览器最大化
driver.maximize_window()

#打开网页
driver.get("https://www.feishu.cn/")

#等待欢迎界面加载完毕
wait.until(ec.presence_of_element_located(('xpath','/html/body/div[2]/div[2]/div/div/div')))
#关闭欢迎窗口
driver.find_element('xpath','/html/body/div[2]/div[2]/div/div/div').click()

#定位登录按钮
driver.find_element('link text','登录').click()

# 等待跳转至登录页面
wait.until(ec.presence_of_element_located(('css selector','.universe-icon.switch-icon')))
# 点击使用账号登录
driver.find_element('css selector','.universe-icon.switch-icon').click()

# 输入手机号
driver.find_element('name','mobile_input').send_keys('15871036064')
# 勾选同意协议
driver.find_element('css selector','.ud__checkbox__input').click()

# 点击下一步
driver.find_element('css selector','.step-box__body > button').click()

wait.until(ec.visibility_of_element_located(('xpath','/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/button')))

# 输入验证码
pwd=input('验证码')
boxs=driver.find_elements('name','code_box_input_item')
for i in range(len(pwd)):
    boxs[i].send_keys(pwd[i])

wait.until(ec.visibility_of_element_located(('css selector','.user-list-item')))

# 选择test1登录
users=driver.find_elements('css selector','.user-list-item')
users[1].click()

# 进入飞书网页版
driver.find_element('link text','飞书网页版').click()

# 切换标签页
driver.switch_to.window(driver.window_handles[1])

# 点击通讯录
driver.find_element('css selector','.larkc-badge').click()

# 点击外部联系人
driver.find_element('css selector','.larkc-sidebar-card-name').click()

# 点击test2
driver.find_element('css selector','.avatarMsgCard_body').click()

# 发送消息
driver.find_element('css selector','.larkc-usercard__footer__input.larkc-usercard__footer__message-input').send_keys('helloworld!')


