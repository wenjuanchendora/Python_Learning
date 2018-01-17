"""Test_Case_01: 检查必填项全为空的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在注册界面不做任何输入，直接点击 “提交” 按钮
Expected_Result:
系统提示：信息不完整。
"""


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

from selenium import webdriver
import time

username=['','123','username']
password=['','12345','password']
repasswd=['','12345','password']
email=['','12345@qq.com','123456789@qq.com']
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

def register(username,password,repasswd,email):
    # 打开 Cnode 论坛网址
    driver.get("http://118.31.19.120:3000/")

    # 点击注册
    regis = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
    regis.click()
    # 输入用户名
    usernameInput = driver.find_element_by_id("loginname")
    usernameInput.send_keys(username)
    # 输入密码
    passwordInput = driver.find_element_by_id("pass")
    passwordInput.send_keys(password)
    # 确认密码
    confirmpass = driver.find_element_by_id("re_pass")
    confirmpass.send_keys(repasswd)
    # 输入电子邮箱
    emailInput = driver.find_element_by_id("email")
    emailInput.send_keys(email)
    # 点击注册
    cnoderegis = driver.find_element_by_class_name("span-primary")
    cnoderegis.click()

    time.sleep(5)

for i in range(3):
    register(username[i],password[i],repasswd[i],email[i])

driver.quit()
