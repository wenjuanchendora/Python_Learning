from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

"""Test_Case_01: 检查必填项全为空的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在注册界面不做任何输入，直接点击 “提交” 按钮
Expected_Result:
系统提示：信息不完整。
"""
# # 打开 Cnode 论坛网址
# driver.get("http://118.31.19.120:3000/")

# # 点击注册
# regis = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
# regis.click()
# # 点击注册
# cnoderegis = driver.find_element_by_class_name("span-primary")
# cnoderegis.click()



"""Test_Case_02: 检查必填项 “用户名” 不符合要求的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在 “用户名” 文本框中输入 “123”
4. 在 “密码” 文本框中输入 “password”
5. 在 “确认密码” 文本框中输入 “password”
6. 在 “电子邮箱” 文本框中输入 “123456789@qq.com”
7. 点击 “提交” 按钮
Expected_Result:
系统提示：用户名至少需要5个字符。
"""
# # 打开 Cnode 论坛网址
# driver.get("http://118.31.19.120:3000/")

# # 点击注册
# regis = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
# regis.click()
# # 输入用户名
# username = driver.find_element_by_id("loginname")
# username.send_keys("123")
# # 输入密码
# password = driver.find_element_by_id("pass")
# password.send_keys("password")
# # 确认密码
# confirmpass = driver.find_element_by_id("re_pass")
# confirmpass.send_keys("password")
# # 输入电子邮箱
# email = driver.find_element_by_id("email")
# email.send_keys("123456789@qq.com")
# # 点击注册
# cnoderegis = driver.find_element_by_class_name("span-primary")
# cnoderegis.click()



"""Test_Case_03: 检查必填项全符合要求的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在 “用户名” 文本框中输入 “username”
4. 在 “密码” 文本框中输入 “password”
5. 在 “确认密码” 文本框中输入 “password”
6. 在 “电子邮箱” 文本框中输入 “123456789@qq.com”
7. 点击 “提交” 按钮
Expected_Result:
系统提示：欢迎加入 Nodeclub！我们已给您的注册邮箱发送了一封邮件，请点击里面的链接来激活您的帐号。
"""
# # 打开 Cnode 论坛网址
# driver.get("http://118.31.19.120:3000/")

# # 点击注册
# regis = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
# regis.click()
# # 输入用户名
# username = driver.find_element_by_id("loginname")
# username.send_keys("username")
# # 输入密码
# password = driver.find_element_by_id("pass")
# password.send_keys("password")
# # 确认密码
# confirmpass = driver.find_element_by_id("re_pass")
# confirmpass.send_keys("password")
# # 输入电子邮箱
# email = driver.find_element_by_id("email")
# email.send_keys("123456789@qq.com")
# # 点击注册
# cnoderegis = driver.find_element_by_class_name("span-primary")
# cnoderegis.click()
