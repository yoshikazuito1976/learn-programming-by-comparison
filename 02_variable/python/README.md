# 02_variable / Python

## 目的

Pythonで変数を使い、変数名と文字列の違いを理解する。  
また、文字列と変数を組み合わせて表示する方法と、複数の変数にまとめて値を代入する方法を確認する。

---

## ソースコード

```python
name = "yoshikazu"

print(name)
print("name")
print("Hello, " + name)

print(f"Hello, {name}")
print("Hello, {}".format(name))

first_name, last_name = "yoshikazu", "ito"

print(first_name)
print(last_name)
print(f"{last_name} {first_name}")
実行方法
python3 hello_variable.py
実行結果
yoshikazu
name
Hello, yoshikazu
Hello, yoshikazu
Hello, yoshikazu
yoshikazu
ito
ito yoshikazu
```
---
## 確認ポイント
### 変数への代入
```python
name = "yoshikazu"
```

変数 name に、文字列 "yoshikazu" を代入している。

Pythonでは、Javaのように String などの型名を明示しない。

```java
String name = "yoshikazu";
```

Pythonでは次のように書く。

```python
name = "yoshikazu"
```
---

### 変数と文字列の違い
```python
print(name)
print("name")
```

この2つは意味が違う。

```python
print(name)
```

これは、変数 name の中身を表示する。

```python
print("name")
```

これは、name という文字そのものを表示する。

つまり、

```text
name   → 変数
"name" → 文字列
```

である。
---

### 文字列の連結
```python
print("Hello, " + name)
```

+ を使うと、文字列と文字列を連結できる。

この場合、"Hello, " と変数 name の中身をつなげて表示している。

### f文字列
```python
print(f"Hello, {name}")
```

f"..." を使うと、文字列の中に変数の値を埋め込むことができる。

{name} の部分に、変数 name の中身が入る。

---
### formatメソッド
```python
print("Hello, {}".format(name))
```

.format() を使っても、文字列の中に変数の値を埋め込むことができる。
{}の部分に.format(name)で指定した値が入る。


---

### アンパック代入

Pythonでは、複数の変数に一度に値を代入できる。

```python
first_name, last_name = "yoshikazu", "ito"
```

これは、次のように代入していると考えることができる。

```python 
first_name = "yoshikazu"
last_name = "ito"
```

左側の変数と右側の値が、左から順番に対応する。

```python
first_name ← "yoshikazu"
last_name  ← "ito"
```
そのため、

```python
print(first_name)
print(last_name)
print(f"{last_name} {first_name}")
```

の実行結果は次のようになる。

```bash
yoshikazu
ito
ito yoshikazu
```

### Javaとの比較

Javaでは、変数を宣言するときに型を書く。

```java
String name = "yoshikazu";
```

Pythonでは、型名を書かずに代入する。

```python
name = "yoshikazu"
```

ただし、どちらの言語でも次の違いは共通している。

name   → 変数の中身を使う
"name" → name という文字そのものを使う

---
まとめ
- Pythonでは 変数名 = 値 の形で変数に値を代入する
- 文字列は " " または ' ' で囲む
- print(name) は変数の中身を表示する
- print("name") は文字列 name を表示する
- \+ を使うと文字列を連結できる
- f"Hello, {name}" のように書くと、文字列の中に変数を埋め込める
- Pythonでは、複数の変数に一度に値を代入することもできる
