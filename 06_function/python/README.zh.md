# 06 函数

在本章中，你将学习如何把处理步骤整理为函数。

如果反复写相似的处理，程序会变得难以阅读。
使用函数可以给处理命名，并在需要时调用它。

---

## 本章目标

本章的目标是理解函数的基础。

在编写程序时，你常常会想重复写同样的处理。

例如，像下面这样多次输出问候语：

```python
print("Hello, ITO!")
print("Hello, Python!")
print("Hello, Programming!")
```

这种处理可以用函数来整理。

使用函数后，可以给处理命名，并在需要时调用。

---

## 关键词

- 函数
- 定义
- 调用
- 参数
- 返回值
- return
- 复用
- 处理拆分

---

## 什么是函数

函数是把处理步骤命名并打包起来的机制。

在 Python 中，使用 `def` 定义函数。

```python
def greet():
    print("Hello!")
```

在这个例子里，你创建了名为 `greet` 的函数。

但是，仅仅定义函数并不会执行它。

要执行函数，需要写函数名并调用它。

```python
greet()
```

---

## 函数的基本形式

Python 函数的基本形式如下。

```python
def 函数名():
    处理
```

例如：

```python
def greet():
    print("Hello!")


greet()
```

执行结果如下：

```text
Hello!
```

---

## 调用函数

函数可以被多次调用。

```python
def greet():
    print("Hello!")


greet()
greet()
greet()
```

执行结果如下：

```text
Hello!
Hello!
Hello!
```

不需要反复写同样的处理，只要调用函数即可。

---

## 什么是参数

参数是传给函数的值。

在下面的例子中，`name` 是参数。

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

执行结果如下：

```text
Hello, ITO!
Hello, Python!
```

写 `greet("ITO")` 时，`"ITO"` 会传给 `name`。

写 `greet("Python")` 时，`"Python"` 会传给 `name`。

---

## 为什么要用参数

使用参数后，可以把函数内部要用的值从外部传入。

这样就能在类似处理中只改少量内容。

```python
def introduce(name, language):
    print(f"{name} is learning {language}.")


introduce("ITO", "Python")
introduce("Tanaka", "Shell")
```

执行结果如下：

```text
ITO is learning Python.
Tanaka is learning Shell.
```

这个例子里使用了两个参数：`name` 和 `language`。

---

## 什么是返回值

返回值是函数执行后返回出来的值。

在 Python 中，使用 `return` 返回值。

```python
def add(a, b):
    return a + b


result = add(3, 5)
print(result)
```

执行结果如下：

```text
8
```

在这个例子中，`add(3, 5)` 返回 `8`。

返回的值被放入变量 `result`。

---

## print 和 return 的区别

`print` 用于在屏幕上显示内容。

`return` 用于返回函数的结果。

请看下面的例子。

```python
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


add_print(3, 5)

result = add_return(3, 5)
print(result)
```

`print` 会显示值。

`return` 会返回值。

返回的值可以放进变量，也可以用于其他计算。

---

## 在计算中使用返回值

返回值可以在后续处理中继续使用。

```python
def add(a, b):
    return a + b


result = add(3, 5)
double_result = result * 2

print(result)
print(double_result)
```

执行结果如下：

```text
8
16
```

把函数结果放进变量后，后续使用会更方便。

---

## 条件分支与函数

你也可以在函数里使用条件分支。

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


result = judge(75)
print(result)
```

执行结果如下：

```text
及格
```

如果 `score` 大于等于 60，返回 `"及格"`。

否则返回 `"不及格"`。

---

## 输入与函数

也可以把 `input` 和函数结合使用。

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


score = int(input("请输入分数: "))
result = judge(score)
print(result)
```

执行示例如下：

```text
请输入分数: 80
及格
```

函数会根据输入的值进行判定。

---

## 循环与函数

函数也可以和循环组合使用。

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

执行结果如下：

```text
92: 及格
85: 及格
74: 及格
66: 及格
39: 不及格
```

程序会逐个取出分数，并用函数进行判定。

---

## 函数化之前的代码

下面代码用于判定分数。

```python
score = 75

if score >= 60:
    result = "及格"
else:
    result = "不及格"

print(result)
```

这段代码可以运行。

但是如果要多次判定分数，就会重复写类似处理。

---

## 函数化之后的代码

把同样的处理整理成函数后，如下所示。

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


result = judge(75)
print(result)
```

函数化后，就能给分数判定这段处理命名为 `judge`。

---

## 函数化的优点

函数化有以下优点。

- 不必反复写同样处理
- 程序更易读
- 需要修改的位置更少
- 可以给处理命名
- 可以按模块思考程序

程序越长，越需要用函数来整理。

---

## 函数命名方法

函数名应当能看出它在做什么。

好的例子：

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"
```

```python
def add(a, b):
    return a + b
```

不太好的例子：

```python
def x(a):
    return a + 10
```

```python
def test(data):
    print(data)
```

名字太短或含义太宽，后续会变得难读。

---

## 编写函数时的注意点

写函数时要注意缩进。

在 Python 中，函数内部处理必须缩进。

```python
def greet():
    print("Hello!")
```

如果像下面这样没有缩进，就会报错。

```python
def greet():
print("Hello!")
```

在 Python 中，缩进非常重要。

---

## 练习 1: 问候函数

请创建满足以下要求的函数。

- 函数名是 `greet`
- 参数是 `name`
- 显示 `Hello, 名字!`

示例：

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

---

## 练习 2: 加法函数

请创建满足以下要求的函数。

- 函数名是 `add`
- 参数是 `a` 和 `b`
- 返回 `a + b` 的结果

示例：

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

---

## 练习 3: 分数判定函数

请创建满足以下要求的函数。

- 函数名是 `judge`
- 参数是 `score`
- 60 分及以上返回 `"及格"`
- 60 分以下返回 `"不及格"`

示例：

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


print(judge(80))
print(judge(45))
```

---

## 练习 4: 列表与函数

有如下分数列表。

```python
scores = [92, 85, 74, 66, 39]
```

请使用 `judge` 函数判定每个分数。

示例：

```python
def judge(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

---

## 练习 5: 等级判定函数

请创建一个按分数返回等级的函数。

- 90 分及以上: A
- 80 分及以上: B
- 70 分及以上: C
- 60 分及以上: D
- 60 分以下: F

示例：

```python
def rank(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = rank(score)
    print(f"{score}: {result}")
```

执行结果如下：

```text
92: A
85: B
74: C
66: D
39: F
```

---

## 本章总结

本章学习了函数。

函数是给处理命名并进行整理的机制。

使用函数后，可以避免反复写同样处理。

同时还能让程序结构更清晰、更易读。

---

## 重点

- 用 `def` 定义函数
- 函数不调用就不会执行
- 参数可以向函数传值
- 用 `return` 从函数返回值
- 函数化后更容易整理程序

---

## 下一步学习内容

掌握函数后，你就能把程序看作多个部件的组合。

下一步将连接到更长程序相关内容，例如文件输入输出和错误处理。
