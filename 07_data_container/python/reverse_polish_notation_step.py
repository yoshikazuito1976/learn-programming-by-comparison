# reverse_polish_notation_step.py
# 逆ポーランド記法を手順で確認する

stack = []

stack.append(3)
print(stack)

stack.append(4)
print(stack)

a = stack.pop()
b = stack.pop()
result = b + a

stack.append(result)
print(stack)
