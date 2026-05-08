# 02_variable

この章では、複数のプログラミング言語で「変数」の書き方を比較する。

## 学習すること

- 変数とは何か
- 文字列・整数・小数の扱い
- 型を書く言語と書かない言語の違い
- 変数を使った出力
- シェルスクリプトにおける変数の扱い

## 比較する言語

- Python
- Java
- C
- C++
- Rust
- Shell Script

## 共通の題材

各言語で、次の情報を変数に入れて出力する。

```text
name = "Taro"
age = 20
height = 170.5
is_student = true
```

出力例：
```text
Name: Taro
Age: 20
Height: 170.5
is_student = true
```

## 比較のポイント
| 観点   | Python | Java               | C      | C++         | Rust          | Shell  |
| ---- | ------ | ------------------ | ------ | ----------- | ------------- | ------ |
| 変数宣言 | 型を書かない | 型を書く               | 型を書く   | 型を書く        | letを使う        | そのまま代入 |
| 文字列  | str    | String             | char配列 | std::string | &str / String | 基本文字列  |
| 整数   | int    | int                | int    | int         | i32など         | 基本文字列  |
| 小数   | float  | double             | double | double      | f64など         | 基本文字列  |
| 真偽値 | `bool` | `boolean` | `bool` ※`stdbool.h`が必要 | `bool` | `bool` | 厳密な真偽値型はない |
| 出力   | print  | System.out.println | printf | std::cout   | println!      | echo   |


## 注意点

シェルスクリプトでは、変数代入の = の前後にスペースを入れない。

```bash
name="Taro"
```

これは正しい。

```bash
name = "Taro"
```

これはエラーになる。

Shell Scriptでは、`is_student=true` のように書けるが、これは他の言語のような厳密な真偽値型ではない。
文字列として扱ったり、コマンドの終了ステータスで条件判定したりする。
