# 04_loops / shell

このディレクトリでは、Shell Script における繰り返し処理を学びます。

Shell の繰り返しでは、`do` で処理の本体が始まり、`done` で終わります。

```sh
for 変数 in 値の一覧
do
  繰り返す処理
done
```

```sh
while [ 条件 ]
do
  繰り返す処理
done
```

Shell では、処理のまとまりをキーワードの対応で読みます。

| 処理 | 始まり | 本体の開始 | 終わり |
| --- | --- | --- | --- |
| 条件分岐 | `if` | `then` | `fi` |
| 繰り返し | `for` / `while` / `until` | `do` | `done` |

## ファイル構成

| ファイル名 | 内容 |
| --- | --- |
| for_basic.sh | `for` による繰り返しの基本 |
| while_basic.sh | `while` による繰り返しの基本 |
| while_read_file.sh | ファイルを1行ずつ読む処理 |
| file.txt | `while_read_file.sh` で読み込むサンプルファイル |
| until_basic.sh | `until` による繰り返しの例 |

## for の基本

`for` は、決まった値の一覧を順番に処理するときに使います。

```sh
for name in taro jiro hanako
do
  echo "$name"
done
```

実行すると、次のように表示されます。

```text
taro
jiro
hanako
```

1行で書く場合は、次のように `; do` を使います。

```sh
for name in taro jiro hanako; do
  echo "$name"
done
```

どちらも同じ意味です。

## while の基本

`while` は、条件が成り立っている間、処理を繰り返します。

```sh
count=1

while [ "$count" -le 5 ]
do
  echo "$count"
  count=$((count + 1))
done
```

この例では、`count` が5以下の間、処理を繰り返します。

実行結果は次のようになります。

```text
1
2
3
4
5
```

1行で書く場合は、次のように `; do` を使います。

```sh
while [ "$count" -le 5 ]; do
  echo "$count"
  count=$((count + 1))
done
```

## `do` と `done`

Shell の繰り返しでは、`do` と `done` が重要です。

```sh
while [ 条件 ]
do
  繰り返す処理
done
```

`do` は「ここから繰り返しの本体が始まる」という意味です。

`done` は「ここで繰り返しの本体が終わる」という意味です。

つまり、`do` と `done` はセットで使います。

## ファイルを1行ずつ読む

Shell では、`while` と `read` を組み合わせることで、ファイルを1行ずつ読むことができます。

```sh
while read line
do
  echo "読み取った行: $line"
done < file.txt
```

この例では、`file.txt` の内容を1行ずつ読み取り、変数 `line` に入れて処理します。

重要なのは、`do` がファイルを読んでいるわけではないということです。

`read line` が1行を読み取り、`done < file.txt` によって、その読み取り元がキーボードではなく `file.txt` になります。

流れは次のようになります。

```text
file.txt
  ↓
read line
  ↓
変数 line に1行分の文字列が入る
  ↓
echo "$line"
  ↓
次の行へ
```

`done < file.txt` は、`while ... do ... done` という繰り返し全体に対して、標準入力を `file.txt` に切り替える書き方です。

## `do < file.txt` ではない

ファイルを読み込むときは、次のように書きます。

```sh
while read line
do
  echo "$line"
done < file.txt
```

次のようには書きません。

```sh
while read line
do < file.txt
  echo "$line"
done
```

`do` は、繰り返し本体の始まりを示すキーワードです。

`do` がファイルを読むわけではありません。

ファイルを入力元にしたい場合は、`done < file.txt` のように、ループ全体に対してリダイレクトを指定します。

## until について

Shell には、`until` という繰り返しもあります。

`until` は、条件が成り立つまで処理を繰り返します。

別の言い方をすると、条件が false の間だけ繰り返します。

```sh
count=1

until [ "$count" -gt 5 ]
do
  echo "$count"
  count=$((count + 1))
done
```

この例では、`count` が5より大きくなるまで繰り返します。

実行結果は次のようになります。

```text
1
2
3
4
5
```

`while` と比べると、条件の見方が逆になります。

```text
while 条件
→ 条件が true の間、繰り返す

until 条件
→ 条件が false の間、繰り返す
```

ただし、最初の学習では `while` のほうが意味を理解しやすいため、この教材では主に `for` と `while` を使います。

`until` は、まずは「読めればOK」という位置づけで十分です。

## 実行方法

まず、実行権限を付けます。

```sh
chmod +x *.sh
```

実行します。

```sh
./for_basic.sh
./while_basic.sh
./while_read_file.sh
./until_basic.sh
```

## 学習のポイント

- 繰り返し処理では `do` と `done` をセットで使う
- `for` は、決まった値の一覧を順番に処理するときに使う
- `while` は、条件が true の間、繰り返す
- `until` は、条件が false の間、繰り返す
- `read` は、標準入力から1行読み取る
- `done < file.txt` は、ループ全体の入力元を `file.txt` にする
- Shell では、スペースとキーワードの対応を正確に読むことが大切
