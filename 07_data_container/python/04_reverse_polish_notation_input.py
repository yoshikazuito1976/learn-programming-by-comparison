# reverse_polish_notation_input.py
# 入力された逆ポーランド記法を計算する

text = input("逆ポーランド記法で式を入力してください: ")

tokens = text.split()
stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        a = stack.pop()
        b = stack.pop()

        if token == "+":
            result = b + a
        elif token == "-":
            result = b - a
        elif token == "*":
            result = b * a
        elif token == "/":
            result = b / a
        else:
            print("知らない演算子です")
            exit()

        stack.append(result)

print(stack[0])
