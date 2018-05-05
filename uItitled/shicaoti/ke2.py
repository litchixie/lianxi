# coding:utf-8
from selenium import webdriver
import time

# # 打开火狐浏览器
# driver = webdriver.Chrome()  # 打开火狐浏览器
# driver.get("http://www.baidu.com")
# time.sleep(3)
# driver.get("http://news.baidu.com/")
# time.sleep(3)
# driver.back() # 返回上一页
# time.sleep(3)
# driver.forward() # 返回下一页
# time.sleep(3)
# driver.refresh() # 刷新网页
# time.sleep(3)
# driver.quit()  # 退出浏览器

# # 打开浏览器，使用id定位操作
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys("谢家开") # 使用id定位输入框，使用send.keys在输入框内输入信息
# time.sleep(1)
# driver.find_element_by_id("su").click() # 查找到按键，点击一下：click()
# time.sleep(3)
# driver.find_element_by_id("kw").clear() # 查找到该输入框，将原内容清空
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("朝西村") # 使用id定位该输入框再输入搜索信息
# time.sleep(2)
# driver.find_element_by_id("su").click() # 使用id搜索该按键，点击搜索
# driver.quit() # 退出浏览器


# # 打开浏览器，使用name定位操作
# driver = webdriver.Firefox()
# driver.get("https://tieba.baidu.com/index.html")
# time.sleep(2)
# driver.find_element_by_name("kw1").send_keys("陈屋地") # 使用name定位输入框，在输入框输入信息（陈屋地）
# time.sleep(2)
# driver.quit()


# 打开浏览器，使用class属性定位操作
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# time.sleep(2)
# driver.find_element_by_class_name("s_ipt").send_keys("你好") #class定位搜索框，在搜索框输入信息
# time.sleep(2)
# driver.find_element_by_class_name("bg s_btn").click() #class定位按键并点击
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.find_elements_by_link_text("新闻").click() # link属性定位，必须与herf在内才是link属性
# time.sleep(2)
# driver.close()

# # 启动浏览器
# driver = webdriver.Firefox()
# driver.get("https://www.dkdoo.cn/#/login")
# time.sleep(2)
# driver.find_element_by_id("phoneNo").send_keys("18578620478") # 找到账号框id，输入登录账号
# time.sleep(2)
# driver.find_element_by_id("password").send_keys("111111")  # 找到密码输入框，输入登录密码
# time.sleep(2)
# driver.find_element_by_class_name("btn-lg").click() # 找到登录按键tag，并点击登录
# time.sleep(3)
# driver.quit()  # 退出浏览器


# # 启动刘浏览器
# driver = webdriver.Firefox()
# driver.get("https://home.firefoxchina.cn/")
# time.sleep(2)
# driver.find_element_by_xpath(".//*[@id='search-nav']/span[2]").click()  # Xpath定位操作
# time.sleep(2)
# driver.quit()


# # 启动刘浏览器
# driver = webdriver.Firefox()
# driver.get("https://home.firefoxchina.cn/")
# time.sleep(2)
# driver.find_element_by_css_selector("#search-key").send_keys("12")  # css定位操作
# time.sleep(2)
# driver.quit()

# # 打开浏览器
# from selenium.webdriver.common.by import By  #导入By定位元素
# driver = webdriver.Firefox()
# driver.get("https://home.firefoxchina.cn/")
# time.sleep(1)
# driver.f
# time.sleep(3)

# 打开浏览器
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://home.firefoxchina.cn/")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"engine-key").send_keys("你好")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"engine-key").submit()
time.sleep(3)
driver.quit()