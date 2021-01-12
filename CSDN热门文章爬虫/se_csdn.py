import os
import time
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

# 创建WebDriver对象(通常默认为wd)，指明Chrome浏览器驱动，并添加上述配置
wd = webdriver.Chrome()
# 窗口最大化
wd.maximize_window()
# 设置最大等待时间
wait = WebDriverWait(wd, 15)

# 访问网址
wd.get('https://so.csdn.net/so/search/all?q=python&t=all&p=1&s=0&tm=0&lv=-1&ft=0&l=&u=')

wd.find_elements_by_class_name('ni-top')[1].click()


time.sleep(2)
wd.close()	# 关闭当前窗口
wd.quit()	# 关闭浏览器