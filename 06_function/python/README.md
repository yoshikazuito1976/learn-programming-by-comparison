# 06 Functions

この章では、処理を関数としてまとめる方法を学びます。

同じような処理を何度も書くと、プログラムは読みにくくなります。
関数を使うと、処理に名前をつけて、必要なときに呼び出せます。

---

## この章の目的

この章の目的は、関数の基本を理解することです。

プログラムを書いていると、同じような処理を何度も書きたくなることがあります。

たとえば、次のように何度もあいさつを表示する場合です。

```python
print("Hello, ITO!")
print("Hello, Python!")
print("Hello, Programming!")
```

このような処理は、関数を使うと整理できます。

関数を使うと、処理に名前をつけて、必要なときに呼び出せます。

---

## キーワード

- 関数
- 定義
- 呼び出し
- 引数
- 戻り値
- return
- 再利用
- 処理の分割

---

## 関数とは

関数とは、処理に名前をつけてまとめたものです。

Python では、`def` を使って関数を定義します。

```python
def greet():
    print("Hello!")
```

この例では、`greet` という名前の関数を作っています。

ただし、関数を定義しただけでは実行されません。

関数を実行するには、関数名を書いて呼び出します。

```python
greet()
```

---

## 関数の基本形

Python の関数の基本形は、次のようになります。

```python
def 関数名():
    処理
```

たとえば、次のように書きます。

```python
def greet():
    print("Hello!")


greet()
```

実行結果は次のようになります。

```text
Hello!
```

---

## 関数を呼び出す

関数は、何度も呼び出すことができます。

```python
def greet():
    print("Hello!")


greet()
greet()
greet()
```

実行結果は次のようになります。

```text
Hello!
Hello!
Hello!
```

同じ処理を何度も書かなくても、関数を呼び出すだけで同じ処理を実行できます。

---

## 引数とは

引数とは、関数に渡す値のことです。

次の例では、`name` が引数です。

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

実行結果は次のようになります。

```text
Hello, ITO!
Hello, Python!
```

`greet("ITO")` と書くと、`name` に `"ITO"` が入ります。

`greet("Python")` と書くと、`name` に `"Python"` が入ります。

---

## 引数を使う理由

引数を使うと、関数の中で使う値を外から渡せます。

次のように、似たような処理を少しだけ変えて実行できます。

```python
def introduce(name, language):
    print(f"{name} is learning {language}.")


introduce("ITO", "Python")
introduce("Tanaka", "Shell")
```

実行結果は次のようになります。

```text
ITO is learning Python.
Tanaka is learning Shell.
```

この例では、`name` と `language` という2つの引数を使っています。

---

## 戻り値とは

戻り値とは、関数から返ってくる値のことです。

Python では、`return` を使って値を返します。

```python
def add(a, b):
    return a + b


result = add(3, 5)
print(result)
```

実行結果は次のようになります。

```text
8
```

この例では、`add(3, 5)` の結果として `8` が返ります。

その返ってきた値を `result` という変数に入れています。

---

## print と return の違い

`print` は、画面に表示するための命令です。

`return` は、関数の結果を返すための命令です。

次の例を見てください。

```python
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


add_print(3, 5)

result = add_return(3, 5)
print(result)
```

`print` は画面に表示します。

`return` は値を返します。

返ってきた値は、変数に入れたり、別の計算に使ったりできます。

---

## 戻り値を計算に使う

戻り値は、あとから別の処理に使えます。

```python
def add(a, b):
    return a + b


result = add(3, 5)
double_result = result * 2

print(result)
print(double_result)
```

実行結果は次のようになります。

```text
8
16
```

関数の結果を変数に入れることで、その後の処理に使いやすくなります。

---

## 条件分岐と関数

関数の中で条件分岐を使うこともできます。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


result = judge(75)
print(result)
```

実行結果は次のようになります。

```text
合格
```

`score` が60以上なら `"合格"` を返します。

そうでなければ `"不合格"` を返します。

---

## 入力と関数

`input` と関数を組み合わせることもできます。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


score = int(input("点数を入力してください: "))
result = judge(score)

print(result)
```

実行例は次のようになります。

```text
点数を入力してください: 80
合格
```

入力された値を使って、関数で判定しています。

---

## 繰り返しと関数

関数は、繰り返し処理と組み合わせることもできます。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

実行結果は次のようになります。

```text
92: 合格
85: 合格
74: 合格
66: 合格
39: 不合格
```

点数のリストを1つずつ取り出して、関数で判定しています。

---

## 関数化する前のコード

次のコードは、点数を判定するプログラムです。

```python
score = 75

if score >= 60:
    result = "合格"
else:
    result = "不合格"

print(result)
```

これでも動きます。

しかし、点数判定を何度も使いたい場合は、同じような処理を何度も書くことになります。

---

## 関数化したコード

同じ処理を関数にまとめると、次のようになります。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


result = judge(75)
print(result)
```

関数にすることで、点数判定の処理に `judge` という名前をつけることができます。

---

## 関数化のよいところ

関数化には、次のようなよいところがあります。

- 同じ処理を何度も書かなくてよい
- プログラムが読みやすくなる
- 修正する場所を少なくできる
- 処理に名前をつけられる
- プログラムを部分ごとに分けて考えられる

プログラムが長くなるほど、関数を使って整理することが大切になります。

---

## 関数名のつけ方

関数名は、その関数が何をするのか分かる名前にします。

よい例です。

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"
```

```python
def add(a, b):
    return a + b
```

あまりよくない例です。

```python
def x(a):
    return a + 10
```

```python
def test(data):
    print(data)
```

短すぎる名前や、意味が広すぎる名前は、あとから読みにくくなります。

---

## 関数を書くときの注意

関数を書くときは、インデントに注意します。

Python では、関数の中の処理はインデントして書きます。

```python
def greet():
    print("Hello!")
```

次のようにインデントがないと、エラーになります。

```python
def greet():
print("Hello!")
```

Python では、インデントがとても大切です。

---

## 練習 1: あいさつ関数

次のような関数を作ってください。

- 関数名は `greet`
- 引数は `name`
- `Hello, 名前!` と表示する

例です。

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

---

## 練習 2: 足し算関数

次のような関数を作ってください。

- 関数名は `add`
- 引数は `a` と `b`
- `a + b` の結果を返す

例です。

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

---

## 練習 3: 点数判定関数

次のような関数を作ってください。

- 関数名は `judge`
- 引数は `score`
- 60点以上なら `"合格"` を返す
- 60点未満なら `"不合格"` を返す

例です。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


print(judge(80))
print(judge(45))
```

---

## 練習 4: リストと関数

次の点数リストがあります。

```python
scores = [92, 85, 74, 66, 39]
```

`judge` 関数を使って、それぞれの点数を判定してください。

例です。

```python
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

---

## 練習 5: ランク判定関数

点数に応じて、次のようにランクを返す関数を作ってください。

- 90点以上: A
- 80点以上: B
- 70点以上: C
- 60点以上: D
- 60点未満: F

例です。

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

実行結果は次のようになります。

```text
92: A
85: B
74: C
66: D
39: F
```

---

## この章のまとめ

この章では、関数について学びました。

関数は、処理に名前をつけてまとめるための仕組みです。

関数を使うと、同じ処理を何度も書かずにすみます。

また、プログラムを読みやすく整理できます。

---

## 重要なポイント

- 関数は `def` で定義する
- 関数は呼び出さないと実行されない
- 引数を使うと、関数に値を渡せる
- `return` を使うと、関数から値を返せる
- 関数化すると、プログラムを整理しやすくなる

---

## 次に学ぶこと

関数を使えるようになると、プログラムを部品に分けて考えられるようになります。

次は、ファイル入出力やエラー処理など、少し長いプログラムを書くための内容につなげていきます。