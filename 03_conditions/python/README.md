# Python: 条件分岐

このディレクトリでは、Python の条件分岐を学びます。

条件分岐は、プログラムに「判断」をさせるための仕組みです。

たとえば、次のような処理を行うときに使います。

- 点数が60点以上なら合格
- 年齢が20歳以上なら成人
- ユーザー名とパスワードが正しければログイン成功
- 条件に応じて表示するメッセージを変える

---

## ファイル一覧

```text
python/
├── README.md
├── conditions_basic.py
├── grade.py
├── age_check.py
└── login_check.py
```

---

## 1. conditions_basic.py

条件分岐の基本を確認するプログラムです。

```python
# conditions_basic.py
# Python: 条件分岐の基本

score = 75

if score >= 60:
    print("合格です")
else:
    print("不合格です")
```

### 実行方法

```bash
python3 conditions_basic.py
```

### ポイント

Pythonでは、条件式のあとに `:` を書きます。

```python
if score >= 60:
```

また、条件に当てはまるときに実行する処理は、インデントを下げて書きます。

```python
if score >= 60:
    print("合格です")
```

このインデントが、Pythonではとても重要です。

---

## 2. grade.py

点数に応じて評価を分けるプログラムです。

```python
# grade.py
# Python: if / elif / else

score = 82

if score >= 90:
    print("評価: S")
elif score >= 80:
    print("評価: A")
elif score >= 70:
    print("評価: B")
elif score >= 60:
    print("評価: C")
else:
    print("評価: D")
```

### 実行方法

```bash
python3 grade.py
```

### ポイント

複数の条件を順番に確認したいときは、`elif` を使います。

`elif` は、他の言語でいう `else if` に近い書き方です。

Pythonでは、条件は上から順番に判定されます。

たとえば `score = 82` の場合、まず次の条件が確認されます。

```python
if score >= 90:
```

これは成り立ちません。

次に、次の条件が確認されます。

```python
elif score >= 80:
```

これは成り立つので、`評価: A` が表示されます。

---

## 3. age_check.py

キーボードから年齢を入力し、成人か未成年かを判定するプログラムです。

```python
# age_check.py
# Python: input() と条件分岐

age = int(input("年齢を入力してください: "))

if age >= 20:
    print("成人です")
else:
    print("未成年です")
```

### 実行方法

```bash
python3 age_check.py
```

### ポイント

`input()` は、キーボードから入力を受け取る関数です。

ただし、`input()` で受け取った値は文字列になります。

そのため、数値として比較したい場合は `int()` を使って整数に変換します。

```python
age = int(input("年齢を入力してください: "))
```

---

## 4. login_check.py

ユーザー名とパスワードを入力し、両方が正しい場合だけログイン成功と表示するプログラムです。

```python
# login_check.py
# Python: and を使った条件分岐

username = input("ユーザー名: ")
password = input("パスワード: ")

if username == "admin" and password == "python":
    print("ログイン成功")
else:
    print("ログイン失敗")
```

### 実行方法

```bash
python3 login_check.py
```

### ポイント

2つの条件が両方とも成り立つか確認したいときは、`and` を使います。

```python
username == "admin" and password == "python"
```

この場合、次の2つの条件が両方とも成り立つときだけ、ログイン成功になります。

- ユーザー名が `"admin"`
- パスワードが `"python"`

---

## 比較演算子

条件分岐では、比較演算子をよく使います。

| 演算子 | 意味 | 例 |
|---|---|---|
| `==` | 等しい | `score == 80` |
| `!=` | 等しくない | `score != 80` |
| `>` | より大きい | `score > 80` |
| `<` | より小さい | `score < 80` |
| `>=` | 以上 | `score >= 80` |
| `<=` | 以下 | `score <= 80` |

注意点として、`=` と `==` は意味が違います。

```python
score = 80
```

これは、変数 `score` に `80` を代入しています。

```python
score == 80
```

これは、`score` が `80` と等しいかどうかを比較しています。

---

## 論理演算子

複数の条件を組み合わせるときは、論理演算子を使います。

| 演算子 | 意味 | 例 |
|---|---|---|
| `and` | かつ | `age >= 18 and age < 65` |
| `or` | または | `answer == "yes" or answer == "y"` |
| `not` | ではない | `not is_logged_in` |

---

## Pythonの条件分岐で大事なこと

Pythonの条件分岐では、次の点に注意します。

1. 条件式の最後に `:` を書く
2. 条件に当てはまる処理はインデントして書く
3. 複数条件は `elif` を使う
4. どれにも当てはまらない場合は `else` を使う
5. 数値入力は必要に応じて `int()` で変換する

---

## 実行例

`03_conditions/python/` に移動している場合は、次のように実行できます。

```bash
python3 conditions_basic.py
python3 grade.py
python3 age_check.py
python3 login_check.py
```

`03_conditions/` にいる場合は、次のように実行できます。

```bash
python3 python/conditions_basic.py
python3 python/grade.py
python3 python/age_check.py
python3 python/login_check.py
```

この4つのプログラムを通して、Pythonにおける条件分岐の基本を確認します。

