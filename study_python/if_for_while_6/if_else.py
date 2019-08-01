ACCOUNT = 'wangyj'
PASSWORD = 'wangwang'

print("Please input account:")
user_account = input()
print("Please input password:")
user_passwd = input()

if user_account != ACCOUNT or user_passwd != PASSWORD:
    print("输入的用户名或密码错误！")
else:
    print("登录成功")