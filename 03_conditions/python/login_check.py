# login_check.py
# Python: and を使った条件分岐

username = input("ユーザー名: ")
password = input("パスワード: ")

if username == "admin" and password == "python":
    print("ログイン成功")
else:
    print("ログイン失敗")
