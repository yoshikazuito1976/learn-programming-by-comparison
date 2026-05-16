# Go: 条件分岐

このディレクトリでは、Go言語の条件分岐を学びます。

Pythonの `if` 文と同じように、Goでも条件によって処理を分けることができます。

## ファイル一覧

| ファイル名 | 内容 |
|---|---|
| `conditions_basic.go` | 基本的な if / else |
| `age_check.go` | 年齢による判定 |
| `grade.go` | 点数による成績判定 |
| `login_check.go` | ユーザー名とパスワードの判定 |

## ビルドと実行

Goでは、ソースコードを実行ファイルに変換してから実行できます。

この教材では、実行ファイル名を `*.out` に統一します。

```bash
go build -o conditions_basic.out conditions_basic.go
./conditions_basic.out
