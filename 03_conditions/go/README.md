# Go: 条件分岐

このディレクトリでは、Go言語の条件分岐を学びます。

条件分岐は、プログラムの中で「もし〜ならば」という判断を行い、条件によって処理を分けるための仕組みです。

Pythonで学んだ `if` 文と同じ考え方ですが、Goでは `{}` を使って処理のまとまりを表します。

---

## ファイル一覧

| ファイル名 | 内容 |
|---|---|
| `conditions_basic.go` | 基本的な `if / else` |
| `age_check.go` | 年齢による判定 |
| `grade.go` | 点数による成績判定 |
| `login_check.go` | ユーザー名とパスワードによる判定 |

---

## ビルドと実行

Goでは、ソースコードをビルドして実行ファイルを作成できます。

この教材では、実行ファイル名を `*.out` に統一します。

例：

```bash
go build -o conditions_basic.out conditions_basic.go
./conditions_basic.out
各ファイルの実行方法
conditions_basic.go
go build -o conditions_basic.out conditions_basic.go
./conditions_basic.out
age_check.go
go build -o age_check.out age_check.go
./age_check.out
grade.go
go build -o grade.out grade.go
./grade.out
login_check.go
go build -o login_check.out login_check.go
./login_check.out
まとめてビルド・実行
go build -o conditions_basic.out conditions_basic.go && ./conditions_basic.out
go build -o age_check.out age_check.go && ./age_check.out
go build -o grade.out grade.go && ./grade.out
go build -o login_check.out login_check.go && ./login_check.out
Goの条件分岐の基本形
if 条件 {
    条件が正しいときの処理
} else {
    条件が正しくないときの処理
}

Goでは、条件式を () で囲む必要はありません。

if score >= 60 {
    fmt.Println("合格")
} else {
    fmt.Println("不合格")
}
else if

条件を複数に分けたい場合は、else if を使います。

if score >= 90 {
    fmt.Println("S")
} else if score >= 80 {
    fmt.Println("A")
} else if score >= 70 {
    fmt.Println("B")
} else if score >= 60 {
    fmt.Println("C")
} else {
    fmt.Println("D")
}

上から順番に条件を確認し、最初に当てはまった処理だけが実行されます。

Pythonとの比較

Pythonでは、インデントで処理のまとまりを表します。

if score >= 60:
    print("合格")
else:
    print("不合格")

Goでは、{} で処理のまとまりを表します。

if score >= 60 {
    fmt.Println("合格")
} else {
    fmt.Println("不合格")
}
比較演算子
演算子	意味
==	等しい
!=	等しくない
>	より大きい
<	より小さい
>=	以上
<=	以下

注意点として、「等しい」を判定するときは = ではなく == を使います。

if username == "student" {
    fmt.Println("ユーザー名が一致しました")
}
論理演算子
演算子	意味
&&	かつ
`	
!	ではない

例：

if username == "student" && password == "linux" {
    fmt.Println("ログイン成功")
} else {
    fmt.Println("ログイン失敗")
}

この場合、ユーザー名とパスワードの両方が正しいときだけ、ログイン成功になります。

学習ポイント

このディレクトリでは、次の点を確認します。

Goでも if を使って条件分岐ができる
Goでは処理のまとまりを {} で表す
else は直前の } と同じ行に書く
条件式に () は不要
等しいかどうかの判定には == を使う
複数条件には && や || を使う
.go はソースコード
.out はビルド後の実行ファイル
実行ファイルを実行するときは ./ファイル名 と書く
Git管理について

.out ファイルはビルドによって生成される実行ファイルです。

そのため、Gitでは管理しません。

リポジトリルートの .gitignore に以下が入っていることを確認します。

*.out

Gitに追加するのは、基本的に以下のようなファイルです。

git add conditions_basic.go age_check.go grade.go login_check.go README.md

.out ファイルは追加しません。

この教材のねらい

この教材では、Pythonで学んだ条件分岐をGoでも書いてみることで、言語ごとの共通点と違いを確認します。

条件分岐の考え方そのものは、多くのプログラミング言語で共通しています。

一方で、書き方には違いがあります。

Pythonではインデントを使い、Goでは {} を使います。

この違いを比較することで、特定の言語だけではなく、プログラミングの考え方そのものを理解することを目指します。
