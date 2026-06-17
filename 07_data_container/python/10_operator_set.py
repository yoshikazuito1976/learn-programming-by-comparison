# operator_set.py
# setを使って、トークンが演算子かどうかを判定する

operators = {"+", "-", "*", "/"}

tokens = ["3", "4", "+", "2", "*"]

for token in tokens:
    if token in operators:
        print(f"{token} は演算子です")
    else:
        print(f"{token} は数値です")
