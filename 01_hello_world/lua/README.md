# Lua: Hello World

このディレクトリでは、Lua の基本的な実行方法を確認します。

Lua は軽量なスクリプト言語です。
Python や Shell Script のように、コンパイルせずに実行できます。

---

## ファイル構成

```text
01_hello_world/
└── lua
    ├── README.md
    └── hello.lua
```

---

## サンプルコード

```lua
print("Hello, Lua!")

local name = "Yoshikazu"
print("Hello, " .. name .. "!")

local language = "Lua"
print(string.format("This language is %s.", language))
```

---

## 実行方法

次のコマンドで実行します。

```bash
lua hello.lua
```

---

## 実行結果

```text
Hello, Lua!
Hello, Yoshikazu!
This language is Lua.
```

---

## ポイント

Lua では、画面に文字を表示するときに `print()` を使います。

```lua
print("Hello, Lua!")
```

Python の `print()` と似ています。

---

## 変数

Lua では、変数を作るときに `local` をつけることが多いです。

```lua
local name = "Yoshikazu"
```

`local` をつけることで、その変数を使える範囲を限定できます。

最初は、次のように考えるとよいです。

- local は「この場所で使う変数を作る」という意味

---

## 文字列の結合

Lua では、文字列をつなげるときに `..` を使います。

```lua
local name = "Yoshikazu"

print("Hello, " .. name .. "!")
```

Python では `+` を使って文字列をつなげることがあります。

```python
name = "Yoshikazu"

print("Hello, " + name + "!")
```

Lua では `+` ではなく、`..` を使います。

```lua
"Hello, " .. name .. "!"
```

---

## 書式付き文字列

Lua では、`string.format()` を使うと、値を文字列の中に埋め込むことができます。

```lua
local language = "Lua"

print(string.format("This language is %s.", language))
```

`%s` は文字列を表します。

```text
%s  string  文字列
```

実行すると、次のように表示されます。

```text
This language is Lua.
```

---

## 数値を埋め込む

整数を埋め込むときは `%d` を使います。

```lua
local age = 49

print(string.format("age = %d", age))
```

出力：

```text
age = 49
```

`%d` は decimal integer、つまり10進整数を表します。

---

## 小数を埋め込む

小数を埋め込むときは `%f` を使います。

```lua
local score = 87.5

print(string.format("score = %f", score))
```

出力：

```text
score = 87.500000
```

小数点以下の桁数を指定したい場合は、次のように書きます。

```lua
local score = 87.5

print(string.format("score = %.1f", score))
print(string.format("score = %.2f", score))
```

出力：

```text
score = 87.5
score = 87.50
```

よく使う指定は次の通りです。

- %s: string（文字列）
- %d: decimal integer（10進整数）
- %f: floating point（小数）
- %.1f: 小数点以下1桁
- %.2f: 小数点以下2桁

---

## Pythonとの比較

Python では、f-string を使うと変数を文字列に埋め込めます。

```python
name = "Yoshikazu"
language = "Python"

print(f"Hello, {name}!")
print(f"This language is {language}.")
```

Lua には Python の f-string のような標準構文はありません。

Lua では、文字列結合または `string.format()` を使います。

### 文字列結合を使う例

```lua
local name = "Yoshikazu"

print("Hello, " .. name .. "!")
```

### string.format() を使う例

```lua
local name = "Yoshikazu"

print(string.format("Hello, %s!", name))
```

同じ「値を文字列の中に入れて表示する」処理でも、言語によって書き方が違います。

---

## Luaの特徴

Lua は、シンプルで軽量なスクリプト言語です。

この教材では、Luaを深く学ぶことよりも、Python や C などの他の言語と比較しながら、プログラミングの共通点と違いを観察します。

Lua の特徴として、次のようなものがあります。

- コンパイルせずに実行できる
- print() で出力できる
- local で変数を作る
- 文字列結合には .. を使う
- string.format() で書式付き文字列を作れる
- 配列は基本的に1番目から始まる

特に、配列が1番目から始まる点は、Python や C との大きな違いです。

Python や C では、配列やリストの添字は0から始まることが多いです。

```python
items = ["apple", "banana", "orange"]

print(items[0])  # apple
```

Lua では、基本的に1から始まります。

```lua
local items = {"apple", "banana", "orange"}

print(items[1])  -- apple
```

この違いから、配列を扱うときには次を確認することが大切だとわかります。

- その言語では、何番目から数え始めるのか

---

## まとめ

このディレクトリでは、Lua の Hello World を通して、次のことを確認しました。

- lua ファイル名.lua で実行する
- print() で文字を表示する
- local で変数を作る
- 文字列の結合には .. を使う
- string.format() で値を文字列に埋め込める

Lua は Python に近い感覚で実行できますが、文字列結合や配列の添字などに違いがあります。

比較しながら見ることで、言語ごとの書き方の違いと、プログラミングの基本的な考え方の共通点を確認できます。
