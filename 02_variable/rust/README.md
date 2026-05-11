# 02_variable / Rust

## 目的

Rustで変数を使い、文字列・整数・小数の扱いを確認する。  
また、C、C++、Java、Pythonと比較しながら、Rustでは `let` を使って変数を作ることを理解する。

## ソースコード

```rust
fn main() {
    let name = "yoshikazu";
    let age = 48;
    let height = 170.5;

    println!("{}", name);
    println!("name");
    println!("Hello, {}", name);

    println!("{}", age);
    println!("{}", height);

    println!("Age: {}", age);
    println!("Height: {:.1}", height);

    let first_name = "yoshikazu";
    let last_name = "ito";

    println!("{} {}", last_name, first_name);
}
```

## コンパイルと実行
```bash
rustc hello_variable.rs -o hello_variable.out
./hello_variable.out
```

## 実行結果
```bash
yoshikazu
name
Hello, yoshikazu
48
170.5
Age: 48
Height: 170.5
ito yoshikazu
```

## 確認ポイント
Rustでは let で変数を作る
let name = "yoshikazu";
let age = 48;
let height = 170.5;

Rustでは、変数を作るときに let を使う。

型を書いていないが、Rustが値から型を推論している。

name   → 文字列
age    → 整数
height → 小数
型を明示することもできる

Rustでは、必要に応じて型を書くこともできる。

let age: i32 = 48;
let height: f64 = 170.5;

i32 は整数、f64 は小数を表す型である。

## 変数と文字列の違い
println!("{}", name);
println!("name");

この2つは意味が違う。

name   → 変数 name の中身
"name" → name という文字そのもの
文字列と変数を組み合わせる
println!("Hello, {}", name);

{} の部分に、変数 name の中身が入る。

そのため、実行結果は次のようになる。

Hello, yoshikazu
小数の表示桁数を指定する
println!("Height: {:.1}", height);

{:.1} は、小数第1位まで表示する指定である。

実行結果は次のようになる。

Height: 170.5
画面への表示方法の比較

言語によって、画面に文字を表示する書き方が違う。

Bashでは echo で表示する。
Pythonでは print() で表示する。
Javaでは System.out.println() で表示する。
Cでは printf() で表示する。
C++では std::cout に << で送って表示する。
Rustでは println!() で表示する。

Rustでは、次のように書く。

println!("Hello, {}", name);

println! は「プリントライン」と読む。

最後に ! が付いているのは、Rustの println! がマクロだからである。
初めのうちは、画面に表示するときは println!() を使う、と理解すればよい。

---
## C / C++ / Java / Python / Rust の比較
### 文字列
```text
char name[] = "yoshikazu";
std::string name = "yoshikazu";
String name = "yoshikazu";
name = "yoshikazu"
let name = "yoshikazu";
```

### 整数
```text
int age = 48;
int age = 48;
int age = 48;
age = 48
let age = 48;
```

### 小数
```text
double height = 170.5;
double height = 170.5;
double height = 170.5;
height = 170.5
let height = 170.5;
```

---
## まとめ
- Rustでは let を使って変数を作る
- Rustは型を推論できる
- 必要なら let age: i32 = 48; のように型を明示できる
- println!() を使うと画面に表示できる
- println!("{}", name); は変数の中身を表示する
- println!("name"); は文字列 name を表示する
- {} の部分に変数の値を埋め込める
- println! は「プリントライン」と読む
