def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


score = int(input("点数を入力してください: "))
result = judge(score)

print(result)
