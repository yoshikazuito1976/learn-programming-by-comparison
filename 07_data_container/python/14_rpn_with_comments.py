# rpn_with_comments.py
# コメントは「何をしているか」ではなく「なぜそうするか」を書く

tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
operators = {"+", "-", "*", "/"}

stack = []

for token in tokens:
    if token in operators:
        # 後から入れた値が右側の数になるため、先に取り出す
        right = stack.pop()

        # 次に取り出した値が左側の数になる
        left = stack.pop()

        if token == "+":
            result = left + right
        elif token == "-":
            result = left - right
        elif token == "*":
            result = left * right
        elif token == "/":
            result = left / right

        # 計算結果を次の演算で使うため、stackに戻す
        stack.append(result)
    else:
        # 文字列のままだと計算できないため、整数に変換して積む
        stack.append(int(token))

print(stack[0])
