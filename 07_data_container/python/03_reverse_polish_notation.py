# reverse_polish_notation.py
# 逆ポーランド記法の計算

tokens = ["3", "4", "+"]

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

        stack.append(result)

print(stack[0])
