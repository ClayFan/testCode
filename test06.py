username = input("请输入账号")
password = input("请输入密码")
if len(username) > 5 and len(username) < 8:
    if username == "张三12345" and password == "123456":
        print("登录成功")
    else:
        print("登录失败")
else:
    print("请输入账号长度大于5位,并且小于8位")