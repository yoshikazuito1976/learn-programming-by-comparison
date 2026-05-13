# 02_variable / Go

## 目的

Goで変数を使い、変数名と文字列の違いを理解する。
また、文字列と変数を組み合わせて表示する方法と、複数の変数にまとめて値を代入する方法を確認する。

---

## ソースコード

```go
package main

import "fmt"

func main() {
	name := "yoshikazu"

	fmt.Println(name)
	fmt.Println("name")
	fmt.Println("Hello, " + name)

	fmt.Printf("Hello, %s\n", name)
	fmt.Println(fmt.Sprintf("Hello, %s", name))

	firstName, lastName := "yoshikazu", "ito"

	fmt.Println(firstName)
	fmt.Println(lastName)
	fmt.Printf("%s %s\n", lastName, firstName)
}
```

## 実行方法

直接実行する場合：

```bash
go run hello_variable.go
```

コンパイルして実行する場合：

```bash
go build -o hello_variable.out hello_variable.go
./hello_variable.out
```

## 実行結果

```text
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

```go
name := "yoshikazu"
```

変数 `name` に、文字列 `"yoshikazu"` を代入している。

Goでは、関数の中で `:=` を使うと、型を明示せずに変数を作ることができる。

これは次のように書くこともできる。

```go
var name string = "yoshikazu"
```

Pythonでは次のように書く。

```python
name = "yoshikazu"
```

Javaでは次のように書く。

```java
String name = "yoshikazu";
```

---

### 変数と文字列の違い

```go
fmt.Println(name)
fmt.Println("name")
```

この2つは意味が違う。

```go
fmt.Println(name)
```

これは、変数 `name` の中身を表示する。

```go
fmt.Println("name")
```

これは、`name` という文字そのものを表示する。

つまり、

```text
name   → 変数
"name" → 文字列
```

である。

---

### 文字列の連結

```go
fmt.Println("Hello, " + name)
```

`+` を使うと、文字列と文字列を連結できる。

この場合、`"Hello, "` と変数 `name` の中身をつなげて表示している。

---

### fmt.Printf

```go
fmt.Printf("Hello, %s\n", name)
```

`fmt.Printf()` を使うと、文字列の中に変数の値を埋め込んで表示できる。

`%s` は文字列を入れる場所を表している。

```text
%s → string
```

`\n` は改行を表す。

---

### fmt.Sprintf

```go
fmt.Println(fmt.Sprintf("Hello, %s", name))
```

`fmt.Sprintf()` は、変数を埋め込んだ文字列を作る。

`fmt.Printf()` はそのまま画面に表示するが、`fmt.Sprintf()` は文字列を作るだけである。

そのため、ここでは `fmt.Println()` で表示している。

---

### 複数の変数への代入

Goでも、複数の変数に一度に値を代入できる。

```go
firstName, lastName := "yoshikazu", "ito"
```

これは、次のように代入していると考えることができる。

```go
firstName := "yoshikazu"
lastName := "ito"
```

左側の変数と右側の値が、左から順番に対応する。

```text
firstName ← "yoshikazu"
lastName  ← "ito"
```

そのため、

```go
fmt.Println(firstName)
fmt.Println(lastName)
fmt.Printf("%s %s\n", lastName, firstName)
```

の実行結果は次のようになる。

```text
yoshikazu
ito
ito yoshikazu
```

---

### Pythonとの比較

Pythonでは、変数を作るときに型を書かない。

```python
name = "yoshikazu"
```

Goでは、次のように `:=` を使って変数を作ることができる。

```go
name := "yoshikazu"
```

また、型を明示して書くこともできる。

```go
var name string = "yoshikazu"
```

ただし、どちらの言語でも次の違いは共通している。

```text
name   → 変数の中身を使う
"name" → name という文字そのものを使う
```

---

## まとめ

- Goでは `:=` を使って変数に値を代入できる
- 文字列は `" "` で囲む
- `fmt.Println(name)` は変数の中身を表示する
- `fmt.Println("name")` は文字列 `name` を表示する
- `+` を使うと文字列を連結できる
- `fmt.Printf("Hello, %s\n", name)` のように書くと、文字列の中に変数を埋め込める
- Goでは、複数の変数に一度に値を代入することもできる
- Goでは、Pythonと違って `fmt` パッケージを使って画面表示を行う
