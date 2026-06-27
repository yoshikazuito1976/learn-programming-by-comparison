# 理解逆波兰表示法

在本教材中，我们使用 Python 来理解**逆波兰表示法（RPN）**。

逆波兰表示法是一种将运算符写在数字后面的记法。

普通表达式：

```text
3 + 4
```

逆波兰表示法：

```text
3 4 +
```

普通表达式：

```text
( 3 + 4 ) * 2
```

逆波兰表示法：

```text
3 4 + 2 *
```

在本教材中，我们将 Python 的列表作为**栈**来使用，学习如何计算逆波兰表示法的表达式，以及如何将普通表达式转换为逆波兰表示法。

## 目标

本教材的目的不仅仅是制作一个计算器。

我们的目标是通过编程来理解以下内容：

- 列表
- `append()`
- `pop()`
- 条件分支
- 循环
- 函数
- 字符串处理
- 栈
- 运算符优先级
- 表达式转换

## 什么是逆波兰表示法？

在普通表达式中，运算符写在数字之间。

```text
3 + 4
```

这种写法称为**中缀表示法**。

在逆波兰表示法中，运算符写在数字后面。

```text
3 4 +
```

这个表达式的含义是：

> 将 3 和 4 相加。

一个稍复杂的例子：

```text
3 4 + 2 *
```

这与下面的表达式含义相同：

```text
( 3 + 4 ) * 2
```

计算结果为 `14`。

## 什么是栈？

栈是一种后进先出的数据结构。

英文称为 **Last In, First Out**，缩写为 **LIFO**。

在 Python 中，可以使用列表来模拟栈的行为。

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

x = stack.pop()
print(x)
print(stack)
```

输出结果：

```text
['A', 'B', 'C']
C
['A', 'B']
```

最后加入的 `"C"` 最先被取出。

## Step 1：确认栈的行为

首先，我们不进行计算，只确认栈的工作方式。

```python
stack = []

stack.append(3)
stack.append(4)

print(stack)

x = stack.pop()
print(x)

y = stack.pop()
print(y)

print(stack)
```

输出结果：

```text
[3, 4]
4
3
[]
```

使用 `append()` 压入值，使用 `pop()` 取出值。

## Step 2：手动读取逆波兰表达式

考虑以下表达式：

```text
3 4 +
```

读取方式如下：

| 读取内容 | 栈 |
|---|---|
| 3 | 3 |
| 4 | 3, 4 |
| + | 7 |

遇到 `+` 时，从栈中取出两个数字并进行计算。

```text
3 + 4 = 7
```

将计算结果 `7` 再次压入栈中。

## Step 3：计算逆波兰表达式

编写一个计算 `3 4 +` 的程序。

```python
tokens = ["3", "4", "+"]

stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b

        stack.append(result)

print(stack[0])
```

输出结果：

```text
7
```

## Step 4：支持四则运算

除了 `+`，还支持 `-`、`*`、`/`。

```python
tokens = ["3", "4", "+", "2", "*"]

stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b
        elif token == "-":
            result = a - b
        elif token == "*":
            result = a * b
        elif token == "/":
            result = a / b

        stack.append(result)

print(stack[0])
```

输出结果：

```text
14
```

这个表达式与下面的普通表达式含义相同：

```text
( 3 + 4 ) * 2
```

## Step 5：封装为函数

将相同的处理封装为函数，以便重复使用。

```python
def calc_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)

    return stack[0]


print(calc_rpn("3 4 +"))
print(calc_rpn("3 4 + 2 *"))
print(calc_rpn("10 3 -"))
```

输出结果：

```text
7
14
7
```

## Step 6：将普通表达式转换为逆波兰表示法

接下来，将普通表达式转换为逆波兰表示法。

普通表达式：

```text
3 + 4 * 2
```

逆波兰表示法：

```text
3 4 2 * +
```

使用以下两个列表：

```python
output = []  # 存放转换后的表达式
stack = []   # 临时存放运算符
```

运算符有优先级：

```python
priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
```

`*` 和 `/` 比 `+` 和 `-` 优先计算。

## Step 7：不含括号的转换

首先，转换不含括号的表达式。

```python
def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while stack and priority[stack[-1]] >= priority[token]:
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


print(infix_to_rpn("3 + 4"))
print(infix_to_rpn("3 + 4 * 2"))
print(infix_to_rpn("3 * 4 + 2"))
```

输出结果：

```text
3 4 +
3 4 2 * +
3 4 * 2 +
```

## Step 8：支持括号

接下来，支持含括号的表达式。

```python
def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while (
                stack
                and stack[-1] != "("
                and priority[stack[-1]] >= priority[token]
            ):
                output.append(stack.pop())

            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

    while stack:
        output.append(stack.pop())

    return " ".join(output)


print(infix_to_rpn("( 3 + 4 ) * 2"))
print(infix_to_rpn("3 * ( 4 + 2 )"))
```

输出结果：

```text
3 4 + 2 *
3 4 2 + *
```

## Step 9：转换后计算

最后，将普通表达式转换为逆波兰表示法后进行计算。

```python
def calc_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)

    return stack[0]


def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while (
                stack
                and stack[-1] != "("
                and priority[stack[-1]] >= priority[token]
            ):
                output.append(stack.pop())

            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

    while stack:
        output.append(stack.pop())

    return " ".join(output)


normal_expression = "( 3 + 4 ) * 2"

rpn_expression = infix_to_rpn(normal_expression)
answer = calc_rpn(rpn_expression)

print("普通表达式:", normal_expression)
print("逆波兰表示法:", rpn_expression)
print("计算结果:", answer)
```

输出结果：

```text
普通表达式: ( 3 + 4 ) * 2
逆波兰表示法: 3 4 + 2 *
计算结果: 14
```

## 输入规则

在本教材中，表达式必须用空格分隔每个符号。

正确：

```text
3 + 4
3 + 4 * 2
( 3 + 4 ) * 2
```

错误：

```text
3+4
3+4*2
(3+4)*2
```

处理无空格表达式的内容作为发展课题。

## 练习题

### 必做题

编写函数 `calc_rpn()`，用于计算逆波兰表达式。

请确保能够处理以下表达式：

```text
3 4 +
3 4 + 2 *
10 3 -
10 2 /
```

### 标准题

编写函数 `infix_to_rpn()`，将普通表达式转换为逆波兰表示法。

请确保能够处理以下表达式：

```text
3 + 4
3 + 4 * 2
3 * 4 + 2
```

### 发展题

支持含括号的表达式。

请确保能够处理以下表达式：

```text
( 3 + 4 ) * 2
3 * ( 4 + 2 )
( 10 - 3 ) * ( 2 + 1 )
```

## 提交内容

请提交以下内容：

- 栈行为的确认
- `calc_rpn()` 的程序
- `infix_to_rpn()` 的程序
- 使用自己设计的3个以上表达式的运行结果
- 对程序的说明

## 回顾

请用自己的话解释以下内容：

- 什么是栈？
- `append()` 做了什么？
- `pop()` 做了什么？
- 为什么逆波兰表示法需要使用栈？
- 将普通表达式转换为逆波兰表示法时，为什么需要运算符优先级？

## 发展挑战

如果想进一步挑战，请尝试以下内容：

- 支持小数
- 支持负数
- 支持无空格的表达式
- 添加错误处理
- 支持 `**`（幂运算）
- 用其他编程语言实现相同的逻辑
