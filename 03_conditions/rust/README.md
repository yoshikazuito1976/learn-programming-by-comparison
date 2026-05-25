# Rust: 条件分岐の基本

このディレクトリでは、Rustで条件分岐を書く練習をします。

Pythonでは、条件分岐を次のように書きました。

```python
score = 75

if score >= 60:
    print("合格です")
else:
    print("不合格です")

```

Rustでは、次のように書きます。

```rust
// conditions_basic.rs
// Rust: 条件分岐の基本

fn main() {
    let score = 75;

    if score >= 60 {
        println!("合格です");
    } else {
        println!("不合格です");
    }
}
```

実行方法

## 実行方法

Rustでは、`rustc` コマンドで `.rs` ファイルをコンパイルします。

```bash
rustc age_check.rs -o age_check.out
./age_check.out
```

-o age_check.out は、作成される実行ファイル名を指定するオプションです。

このリポジトリでは *.out を .gitignore に登録しているため、コンパイル後の実行ファイルはGitの管理対象になりません。

## Pythonとの違い
|内容|	Python|	Rust|
|---|---|---|
|変数|	score = 75|	let score = 75;|
|条件分岐|	if score >= 60:|	if score >= 60 {|
|ブロック|	インデント|	{ }|
|出力|	print()|	println!()|

## ポイント

Pythonでは、インデントによって処理のまとまりを表します。

Rustでは、{ } を使って処理のまとまりを表します。

また、Rustでは文の終わりに ; を書くことが多いです。

```rust
let score = 75;
```

## ただし、if の条件式のあとには ; は書きません。

```rust
if score >= 60 {
    println!("合格です");
}
```
## 学習のねらい

この例では、次のことを確認します。

Rustで変数を作る方法
Rustで条件分岐を書く方法
PythonのインデントとRustの { } の違い
println!() を使った出力