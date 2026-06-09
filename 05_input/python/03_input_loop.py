scores = []

for i in range(3):
    score = int(input(f"{i + 1}人目の点数を入力してください: "))
    scores.append(score)

print(scores)
print(f"合計点: {sum(scores)}")
print(f"平均点: {sum(scores) / len(scores)}")
