# Haskell: Hello World

このディレクトリでは、Haskell の基本的な実行方法を確認します。

Haskell は関数型プログラミング言語です。
この教材では、Haskell を深く学ぶことよりも、他の言語との違いを観察することを目的とします。

---

## ファイル構成

```text
01_hello_world/
└── haskell
    ├── README.md
    └── hello.hs
```

---

## サンプルコード

```haskell
main :: IO ()
main = do
    putStrLn "Hello, Haskell!"

    let name = "Yoshikazu"
    putStrLn ("Hello, " ++ name ++ "!")

    let language = "Haskell"
    putStrLn ("This language is " ++ language ++ ".")
```

---

## 実行方法

Haskell は `runghc` を使うと、コンパイルを意識せずにそのまま実行できます。

```bash
runghc hello.hs
```

実行結果：

```text
Hello, Haskell!
Hello, Yoshikazu!
This language is Haskell.
```

---

## コンパイルして実行する方法

Haskell は `ghc` を使ってコンパイルすることもできます。

```bash
ghc hello.hs -o hello.out
./hello.out
```

この教材では、生成された実行ファイルを `.gitignore` で無視しやすくするため、実行ファイル名を `.out` で終わる名前にします。

---

## runghc と ghc の違い

Haskell では、主に2つの実行方法があります。

- runghc hello.hs

これは、スクリプトのように `.hs` ファイルを直接実行する方法です。
学習の最初はこちらが簡単です。

- ghc hello.hs -o hello.out
- ./hello.out

これは、Haskell のソースコードをコンパイルして、実行ファイルを作ってから実行する方法です。

比較すると、次のようになります。

| 方法                          | 説明               |
| --------------------------- | ---------------- |
| `runghc hello.hs`           | そのまま実行する         |
| `ghc hello.hs -o hello.out` | 実行ファイルを作る        |
| `./hello.out`               | 作成された実行ファイルを実行する |

---

## コンパイル時に作られるファイル

`ghc` でコンパイルすると、次のようなファイルが作られます。

```text
hello.hs
hello.hi
hello.o
hello.out
```

それぞれの意味は、おおまかに次の通りです。

| ファイル        | 意味                  |
| ----------- | ------------------- |
| `hello.hs`  | Haskell のソースコード     |
| `hello.hi`  | Haskell のインターフェース情報 |
| `hello.o`   | オブジェクトファイル          |
| `hello.out` | 実行ファイル              |

`hello.hs` は自分で書いたソースコードです。
一方、`hello.hi`、`hello.o`、`hello.out` はコンパイルによって生成されるファイルです。

この教材では、生成されたファイルは Git で管理しません。

`.gitignore` には、次のような設定を入れておきます。

```gitignore
*.hi
*.o
*.out
```

---

## Haskell の Hello World

Haskell では、画面に文字を表示するときに `putStrLn` を使います。

```haskell
putStrLn "Hello, Haskell!"
```

Python の `print()` に近い役割です。

Python:

```python
print("Hello, Python!")
```

Lua:

```lua
print("Hello, Lua!")
```

Haskell:

```haskell
putStrLn "Hello, Haskell!"
```

同じ「画面に文字を表示する」処理でも、言語によって書き方が違います。

---

## main :: IO () とは

Haskell のプログラムには、次のような行が出てきます。

```haskell
main :: IO ()
```

これは、`main` の型を表しています。

最初は難しく考えすぎず、次のように考えれば十分です。

- Haskell では、画面表示などの入出力を行う処理は main の中に書く

`IO` は Input / Output、つまり入出力に関係する処理を表します。

---

## main = do とは

次の部分に、実行したい処理を書きます。

```haskell
main = do
    putStrLn "Hello, Haskell!"
```

`do` の中に、上から順番に処理を書きます。

この例では、まず次の文字列を表示しています。

```haskell
putStrLn "Hello, Haskell!"
```

---

## let による変数のような値の定義

Haskell では、`let` を使って名前をつけることができます。

```haskell
let name = "Yoshikazu"
```

これは、`name` という名前に `"Yoshikazu"` という文字列を対応させています。

そのあと、次のように使っています。

```haskell
putStrLn ("Hello, " ++ name ++ "!")
```

---

## 文字列の結合

Haskell では、文字列をつなげるときに `++` を使います。

```haskell
"Hello, " ++ name ++ "!"
```

Python では `+` を使うことがあります。

```python
"Hello, " + name + "!"
```

Lua では `..` を使います。

```lua
"Hello, " .. name .. "!"
```

Haskell では `++` を使います。

```haskell
"Hello, " ++ name ++ "!"
```

同じ「文字列をつなげる」処理でも、言語によって記号が違います。

---

## Python との比較

Python では、f-string を使うと次のように書けます。

```python
name = "Yoshikazu"
language = "Python"

print(f"Hello, {name}!")
print(f"This language is {language}.")
```

Haskell では、次のように書いています。

```haskell
let name = "Yoshikazu"
putStrLn ("Hello, " ++ name ++ "!")

let language = "Haskell"
putStrLn ("This language is " ++ language ++ ".")
```

Python の f-string のように、文字列の中に直接変数を埋め込む書き方とは少し違います。
Haskell では、ここでは `++` を使って文字列をつなげています。

---

## Haskell の特徴

Haskell は、関数型プログラミング言語です。

Python、Lua、C などでは、処理を上から順番に書いていく感覚が強くあります。
Haskell では、値や関数を組み合わせて考える感覚が強くなります。

この Hello World では、まだ Haskell らしさは少ししか出てきません。

do の中に入出力の処理を書く
しかし、次のような点に違いが見えます。

- main :: IO () のように型を書く
- putStrLn で文字列を表示する
- do の中に入出力の処理を書く
- let で名前をつける
- 文字列結合には ++ を使う

---

## Haskell の位置づけ

この教材では、Haskell をメインの学習言語として深く扱うわけではありません。

Haskell は、比較プログラミングにおける発展的な観察対象です。

目的は、次のことを確認することです。

- 同じ Hello World でも、言語によって書き方が違う
- 同じ文字列表示でも、print / printf / putStrLn など違いがある
- 同じ文字列結合でも、+ / .. / ++ など違いがある
- プログラミングには、命令型だけでなく関数型という考え方もある

---

## まとめ

ghc hello.hs -o hello.out でコンパイルできる
このディレクトリでは、Haskell の Hello World を通して、次のことを確認しました。

- runghc hello.hs でそのまま実行できる
- ghc hello.hs -o hello.out でコンパイルできる
- putStrLn で文字列を表示する
- main :: IO () は入出力を行う main 関数の型を表す
- do の中に処理を書く
- let で名前をつける
- 文字列の結合には ++ を使う

Haskell は Python や Lua と比べると、最初は少し難しく見えます。

しかし、比較することで次のことがわかります。

- 言語が変わっても「値を作る」「文字列を表示する」「処理を実行する」という目的は共通している

この教材では、Haskell を通して、プログラミングにはさまざまな考え方があることを観察します。
