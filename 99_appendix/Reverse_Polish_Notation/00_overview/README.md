# 逆ポーランド記法を理解する

この教材では、Python を使って **逆ポーランド記法** を理解します。

逆ポーランド記法は、演算子を数字の後ろに書く記法です。

通常の式:

```text
3 + 4
```

逆ポーランド記法:

```text
3 4 +
```

通常の式:

```text
( 3 + 4 ) * 2
```

逆ポーランド記法:

```text
3 4 + 2 *
```

この教材では、Python のリストを **スタック** として使いながら、逆ポーランド記法の計算と、普通の式から逆ポーランド記法への変換を学びます。

## 目的

この教材の目的は、単に電卓を作ることではありません。

次の内容を、プログラムを通して理解することを目的とします。

- リスト
- `append()`
- `pop()`
- 条件分岐
- 繰り返し
- 関数
- 文字列処理
- スタック
- 演算子の優先順位
- 式の変換

## 逆ポーランド記法とは

通常の式では、演算子を数字の間に書きます。

```text
3 + 4
```

このような書き方を **中置記法** と呼びます。

逆ポーランド記法では、演算子を数字の後ろに書きます。

```text
3 4 +
```

この式は、次のように読みます。

> 3 と 4 を足す

もう少し複雑な例です。

```text
3 4 + 2 *
```

これは、次の式と同じ意味です。

```text
( 3 + 4 ) * 2
```

計算結果は `14` です。

## スタックとは

スタックとは、後から入れたものが先に出てくるデータ構造です。

英語では **Last In, First Out** と言います。略して **LIFO** です。

Python では、リストを使ってスタックのような動きを表現できます。

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

実行結果:

```text
['A', 'B', 'C']
C
['A', 'B']
```

最後に入れた `"C"` が最初に取り出されています。

## Step 1: スタックを確認する

まずは、計算ではなくスタックの動きを確認します。

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

実行結果:

```text
[3, 4]
4
3
[]
```

`append()` で値を入れ、`pop()` で値を取り出します。

## Step 2: 逆ポーランド記法を手で読む

次の式を考えます。

```text
3 4 +
```

読み方は次の通りです。

| 読んだもの | スタック |
|---|---|
| 3 | 3 |
| 4 | 3, 4 |
| + | 7 |

`+` が出てきたら、スタックから数字を2つ取り出して計算します。

```text
3 + 4 = 7
```

計算結果の `7` を、もう一度スタックに入れます。

## Step 3: 逆ポーランド記法を計算する

まずは、`3 4 +` を計算するプログラムを書きます。

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

実行結果:

```text
7
```

## Step 4: 四則演算に対応する

`+` だけでなく、`-`, `*`, `/` にも対応します。

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

実行結果:

```text
14
```

この式は、次の通常の式と同じ意味です。

```text
( 3 + 4 ) * 2
```

## Step 5: 関数にする

同じ処理を何度も使えるように、関数にします。

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

実行結果:

```text
7
14
7
```

## Step 6: 普通の式を逆ポーランド記法に変換する

次は、普通の式を逆ポーランド記法に変換します。

通常の式:

```text
3 + 4 * 2
```

逆ポーランド記法:

```text
3 4 2 * +
```

ここでは、次の2つのリストを使います。

```python
output = []  # 変換後の式を入れる
stack = []   # 演算子を一時的に入れる
```

演算子には優先順位があります。

```python
priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
```

`*` と `/` は、`+` と `-` より先に計算します。

## Step 7: 括弧なしの変換

まずは、括弧なしの式を変換します。

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

実行結果:

```text
3 4 +
3 4 2 * +
3 4 * 2 +
```

## Step 8: 括弧に対応する

次に、括弧つきの式にも対応します。

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

実行結果:

```text
3 4 + 2 *
3 4 2 + *
```

## Step 9: 変換してから計算する

最後に、普通の式を逆ポーランド記法に変換し、その結果を計算します。

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

print("普通の式:", normal_expression)
print("逆ポーランド記法:", rpn_expression)
print("計算結果:", answer)
```

実行結果:

```text
普通の式: ( 3 + 4 ) * 2
逆ポーランド記法: 3 4 + 2 *
計算結果: 14
```

## 入力のルール

この教材では、式は空白区切りで入力するものとします。

OK:

```text
3 + 4
3 + 4 * 2
( 3 + 4 ) * 2
```

NG:

```text
3+4
3+4*2
(3+4)*2
```

空白なしの式に対応する処理は、発展課題とします。

## 課題

### 必須課題

逆ポーランド記法の式を計算する関数 `calc_rpn()` を作成してください。

次の式を計算できるようにしてください。

```text
3 4 +
3 4 + 2 *
10 3 -
10 2 /
```

### 標準課題

普通の式を逆ポーランド記法に変換する関数 `infix_to_rpn()` を作成してください。

次の式を変換できるようにしてください。

```text
3 + 4
3 + 4 * 2
3 * 4 + 2
```

### 発展課題

括弧つきの式にも対応してください。

次の式を変換できるようにしてください。

```text
( 3 + 4 ) * 2
3 * ( 4 + 2 )
( 10 - 3 ) * ( 2 + 1 )
```

## 提出内容

次の内容を提出してください。

- スタックの動作確認
- `calc_rpn()` のプログラム
- `infix_to_rpn()` のプログラム
- 自分で作った式を3つ以上使った実行結果
- このプログラムの説明

## ふりかえり

次の内容について、自分の言葉で説明してください。

- スタックとは何か
- `append()` は何をしているか
- `pop()` は何をしているか
- 逆ポーランド記法では、なぜスタックを使うのか
- 普通の式を逆ポーランド記法に変換するとき、なぜ演算子の優先順位が必要なのか

## 発展

さらに挑戦したい人は、次の内容にも取り組んでください。

- 小数に対応する
- 負の数に対応する
- 空白なしの式に対応する
- エラー処理を追加する
- `**` に対応する
- 他のプログラミング言語で同じ処理を書く
