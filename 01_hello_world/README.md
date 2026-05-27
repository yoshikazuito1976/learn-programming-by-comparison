# 01 Hello World / Output Comparison

このディレクトリでは、各言語で文字を画面に表示する方法を比較します。

プログラミングでは、まず「画面に文字を出す」ことから始めることが多いです。  
言語によって書き方は違いますが、目的は同じです。

## 各言語の出力例

| 言語 | 出力の書き方 |
|---|---|
| Python | `print("Hello, World!")` |
| C | `printf("Hello, World!\n");` |
| C++ | `std::cout << "Hello, World!\n";` |
| Java | `System.out.println("Hello, World!");` |
| Go | `fmt.Println("Hello, World!")` |
| Rust | `println!("Hello, World!");` |
| Bash | `echo "Hello, World!"` |

## 見るポイント

言語ごとに書き方は違います。

しかし、どのコードもやっていることは同じです。

```text
入力：なし
処理：文字列を出力用に渡す
出力：画面に Hello, World! と表示する
```

## 言語ごとの特徴

### Python

```python
print("Hello, World!")
```

Pythonはとてもシンプルです。  
`print()` を使うと、文字を画面に表示できます。

### C

```c
printf("Hello, World!\n");
```

Cでは `printf()` を使います。  
改行したい場合は `\n` を文字列の中に書きます。

### C++

```cpp
std::cout << "Hello, World!\n";
```

C++では `std::cout` を使います。  
`<<` は、右側の文字列を左側の出力先へ送るようなイメージです。

### Java

```java
System.out.println("Hello, World!");
```

Javaでは `System.out.println()` を使います。  
少し長いですが、「標準出力に1行表示する」ための定型的な書き方です。

### Go

```go
fmt.Println("Hello, World!")
```

Goでは `fmt` パッケージの `Println()` を使います。  
使う前に `import "fmt"` が必要です。

### Rust

```rust
println!("Hello, World!");
```

Rustでは `println!()` を使います。  
`!` が付いているので、これは関数ではなくマクロです。

### Bash

```bash
echo "Hello, World!"
```

Bashでは `echo` コマンドを使います。  
シェル上で文字を表示するときによく使います。

## 大事な考え方

この章で大事なのは、すべての書き方を暗記することではありません。

大事なのは、次のように読めることです。

「これは画面に文字を表示しているコードである」

言語が変わっても、まずは「何をしているコードなのか」を読み取ることが重要です。

## 補足

必要なら、リポジトリのルートから次のようにファイルを作成できます。

```bash
touch 01_hello_world/README.md
```