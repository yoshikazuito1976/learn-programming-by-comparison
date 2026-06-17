# operator_priority.py
# dictを使って、演算子の優先順位を管理する

priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

print(priority["+"])
print(priority["*"])

if priority["*"] > priority["+"]:
    print("* は + より優先度が高いです")
