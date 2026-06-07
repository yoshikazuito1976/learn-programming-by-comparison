# Goのループ

このディレクトリでは、Goの繰り返し処理を学びます。

Goには `while` 文がありません。
繰り返し処理は、基本的にすべて `for` で書きます。

---

## このディレクトリで扱う内容

| file | purpose |
| --- | --- |
| `for_count.go` | 1から5まで数える |
| `for_items.go` | スライスの中身を順番に取り出す |
| `while_style.go` | `for` を `while` のように使う |
| `loop_until_ok.go` | `ok` が入力されるまで繰り返す |

---

## ビルドと実行

Goのプログラムは、`go build` でコンパイルできます。

```bash
go build -o for_count.out for_count.go
go build -o for_items.out for_items.go
go build -o while_style.out while_style.go
go build -o loop_until_ok.out loop_until_ok.go
```

`-o` は、出力する実行ファイル名を指定するオプションです。

例:

```bash
go build -o for_count.out for_count.go
```

これは、`for_count.go` をコンパイルして `for_count.out` という実行ファイルを作る、という意味です。

コンパイルした実行ファイルは次のように実行します。

```bash
./for_count.out
./for_items.out
./while_style.out
./loop_until_ok.out
```

---

## go run

Goでは、`go run` を使ってプログラムをすぐに実行することもできます。

```bash
go run for_count.go
```

`go run` も内部ではコンパイルしていますが、実行ファイルを現在のディレクトリには残しません。

| command | meaning | output file |
| --- | --- | --- |
| `go run for_count.go` | コンパイルしてすぐ実行する | 残らない |
| `go build -o for_count.out for_count.go` | コンパイルして実行ファイルを作る | 残る |
| `./for_count.out` | 作成済みの実行ファイルを実行する | - |

---

## 1. 基本のfor文

Goの基本的な `for` 文です。

```go
package main

import "fmt"

func main() {
	for i := 1; i <= 5; i++ {
		fmt.Println(i)
	}
}
```

ポイント:

```go
for i := 1; i <= 5; i++ {
	// repeated process
}
```

これは、C言語の `for` 文とよく似ています。

---

## 2. rangeを使うループ

スライスの中身を順番に取り出すときは、`range` を使います。

```go
package main

import "fmt"

func main() {
	items := []string{"apple", "banana", "orange"}

	for i, item := range items {
		fmt.Println(i, item)
	}
}
```

出力例:

```text
0 apple
1 banana
2 orange
```

`i` には番号、`item` には中身が入ります。
Pythonの `enumerate()` に近い考え方です。

```python
items = ["apple", "banana", "orange"]

for i, item in enumerate(items):
    print(i, item)
```

---

## 3. whileのように使うfor

Goには `while` 文がありません。
ただし、`for 条件` と書くことで `while` のような繰り返しを書けます。

```go
package main

import "fmt"

func main() {
	count := 1

	for count <= 5 {
		fmt.Println(count)
		count++
	}
}
```

これは、Pythonで書くと次の処理です。

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 4. 無限ループ

Goでは、条件を書かずに `for` だけを書くと無限ループになります。

```go
for {
	// repeat forever
}
```

無限ループを止めるには、`break` を使います。

```go
package main

import "fmt"

func main() {
	var input string

	for {
		fmt.Print("Type ok: ")
		fmt.Scanln(&input)

		if input == "ok" {
			fmt.Println("OK!")
			break
		}

		fmt.Println("Try again.")
	}
}
```

実行例:

```text
Type ok: no
Try again.
Type ok: hello
Try again.
Type ok: ok
OK!
```

---

## まとめ

Goのループ処理のポイントは次の通りです。

- Goには `while` 文がない
- Goの繰り返し処理は `for` で書く
- `for i := 1; i <= 5; i++` で回数を決めた繰り返しが書ける
- `range` を使うとスライスの中身を順番に取り出せる
- `for 条件` で `while` のような処理が書ける
- `for {}` で無限ループが書ける
- `break` でループを抜けられる

## 比較

| language | loop style |
| --- | --- |
| C | `for`, `while` |
| Python | `for`, `while` |
| Shell | `for`, `while`, `until` |
| Go | `for` |

Goは、繰り返し処理を `for` に統一している言語です。
最初は少し不思議に見えますが、慣れるとシンプルに書けます。
