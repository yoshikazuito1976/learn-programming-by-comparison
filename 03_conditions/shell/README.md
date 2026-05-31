# 03_conditions / shell

このディレクトリでは、Shell Script における条件分岐を学びます。

条件分岐とは、条件によって処理を変えるための仕組みです。

たとえば、点数が60点以上なら「合格」、そうでなければ「不合格」と表示するような処理です。

## ファイル構成

| ファイル名 | 内容 |
| --- | --- |
| conditions_basic.sh | 条件分岐の基本 |
| age_check.sh | 年齢による条件分岐 |
| string_check.sh | 文字列の比較 |
| input_condition.sh | 入力と条件分岐 |

## 基本形

Shell の条件分岐は、次のように書きます。

```sh
if [ 条件 ]; then
  条件が成り立つときの処理
else
  条件が成り立たないときの処理
fi
```

`if` で始まり、`fi` で終わります。

`fi` は `if` を逆から書いたものです。

## 数値の比較

Shell では、数値を比較するときに専用の記号を使います。

| 意味 | Shell |
| --- | --- |
| 等しい | `-eq` |
| 等しくない | `-ne` |
| より大きい | `-gt` |
| 以上 | `-ge` |
| より小さい | `-lt` |
| 以下 | `-le` |

例:

```sh
score=75

if [ "$score" -ge 60 ]; then
  echo "合格です"
else
  echo "不合格です"
fi
```

## 文字列の比較

文字列を比較するときは、次のように書きます。

```sh
name="taro"

if [ "$name" = "taro" ]; then
  echo "こんにちは、taroさん"
else
  echo "別の名前です"
fi
```

文字列を比較するときは、変数を `"$name"` のようにダブルクォートで囲むのが安全です。

## 入力と条件分岐

`read` を使うと、キーボードから入力された値を変数に入れることができます。

```sh
printf "名前を入力してください: "
read name

if [ "$name" = "taro" ]; then
  echo "こんにちは、taroさん"
else
  echo "こんにちは、$name さん"
fi
```

## 注意点：スペースが大事

Shell の条件式では、スペースがとても重要です。

正しい例:

```sh
if [ "$score" -ge 60 ]; then
```

間違った例:

```sh
if ["$score" -ge 60]; then
```

`[` の後ろ、`]` の前にはスペースが必要です。

Shell では、スペースも構文の一部です。

## `; then` について

1行で書く場合は、条件のあとに `; then` を書きます。

```sh
if [ "$score" -ge 60 ]; then
  echo "合格です"
fi
```

複数行で書く場合は、次のようにも書けます。

```sh
if [ "$score" -ge 60 ]
then
  echo "合格です"
fi
```

どちらも同じ意味です。

## ブロックの区切り: `if` / `fi` と `do` / `done`

Shell では、処理のかたまり（ブロック）をキーワードで明示します。

- 条件分岐は `if` で始まり、`fi` で終わる
- 反復処理は `do` で始まり、`done` で終わる

### 条件分岐の例

```sh
score=75

if [ "$score" -ge 60 ]; then
  echo "合格です"
else
  echo "不合格です"
fi
```

### 反復処理の例

```sh
for n in 1 2 3; do
  echo "番号: $n"
done
```

Python では、インデント（字下げ）でブロックを表します。

```python
for n in [1, 2, 3]:
    print("番号:", n)
```

Shell は「キーワードでブロックを閉じる」、Python は「インデントでブロックを表す」という違いがあります。

## 他の言語との違い

Python では、数値比較を次のように書きます。

```python
if score >= 60:
    print("合格です")
```

Shell では、次のように書きます。

```sh
if [ "$score" -ge 60 ]; then
  echo "合格です"
fi
```

同じ「60点以上なら合格」という処理でも、言語によって書き方が違います。

## 実行方法

まず、実行権限を付けます。

```sh
chmod +x *.sh
```

実行します。

```sh
./conditions_basic.sh
./age_check.sh
./string_check.sh
./input_condition.sh
```

## 学習のポイント

- `if` は条件分岐を始める命令
- `else` は条件が成り立たなかった場合の処理
- `fi` は条件分岐の終わり
- 数値比較では `-ge` や `-lt` などを使う
- 文字列比較では `=` を使う
- 変数は `"$name"` のようにダブルクォートで囲むと安全
- Shell ではスペースが構文上とても重要
