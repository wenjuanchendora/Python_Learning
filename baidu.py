import os

from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get("https://www.baidu.com/")
baiduserach = driver.find_element_by_id("kw")

baiduserach.send_keys("helloworld")