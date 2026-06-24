# 逆ポーランド記法とエラーハンドリングの考え方

この教材では、Python を使って **逆ポーランド記法** の計算プログラムを作ります。

今回の目的は、完璧な電卓を作ることではありません。

大切なのは、次の流れを体験することです。

1. まず動くコードを書く
2. 動いたコードを関数にまとめる
3. どんなエラーが起きそうか考える
4. エラーを「入口」「処理中」「出口」に分けて考える

`try-except` は今回は必須ではありません。  
まずは `if` を使って、事前に確認できるエラーを考えます。

---

## 1. 逆ポーランド記法とは

通常の式では、演算子を数字の間に書きます。

```text
3 + 4
```

このような書き方を **中置記法** と呼びます。

逆ポーランド記法では、演算子を数字の後ろに書きます。

```text
3 4 +
```

これは、次の式と同じ意味です。

```text
3 + 4
```

もう少し複雑な例です。

```text
3 4 + 5 *
```

これは、次の式と同じ意味です。

```text
(3 + 4) * 5
```

計算結果は `35` です。

---

## 2. 今回の入力ルール

今回のプログラムは、万能電卓ではありません。  
扱う入力のルールを決めます。

### OK

```text
3 4 +
3 4 + 5 *
10 2 /
```

### NG

```text
3+4
3 4+
3 a +
3 4 %
-3 4 +
3.5 2 +
```

今回のルールは次の通りです。

- 数字と演算子は、必ずスペースで区切る
- 数字は 0 以上の整数だけを扱う
- 使える演算子は `+`, `-`, `*`, `/` の4つ
- マイナスの数や小数は発展扱い
- スペースなしの式は発展扱い

---

## 3. スタックを確認する

逆ポーランド記法の計算では、**スタック** を使います。

スタックは、後から入れたものが先に出てくるデータ構造です。  
この考え方を **LIFO** と言います。

Last In, First Out の略です。

Python のリストを使うと、スタックの動きを表現できます。

```python
stack = []

stack.append(3)
stack.append(4)

print(stack)

x = stack.pop()
print(x)
print(stack)
```

実行結果:

```text
[3, 4]
4
[3]
```

`append()` で入れる。  
`pop()` で取り出す。

これが今回の基本です。

---

## 4. まずは関数なしで動かす

最初から `def` を書く必要はありません。

まずは、動くコードを書きます。

```python
stack = []

expression = "3 4 +"
tokens = expression.split()

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    elif token == "+":
        b = stack.pop()
        a = stack.pop()
        result = a + b
        stack.append(result)

print(stack)
```

実行結果:

```text
[7]
```

ここで大事なのは、次の流れです。

```text
数字ならスタックに入れる
演算子なら2つ取り出して計算する
計算結果をスタックに戻す
```

---

## 5. `split()` の確認

文字列をスペースで区切るには、`split()` を使います。

```python
expression = "3 4 +"
tokens = expression.split()

print(tokens)
```

実行結果:

```text
['3', '4', '+']
```

今回のプログラムでは、このように式を1つずつの部品に分けて処理します。

---

## 6. `isdigit()` の確認

文字列が数字かどうかを調べるには、`isdigit()` を使います。

```python
print("3".isdigit())
print("123".isdigit())
print("+".isdigit())
print("a".isdigit())
```

実行結果:

```text
True
True
False
False
```

ただし、注意があります。

```python
print("-3".isdigit())
print("3.5".isdigit())
```

実行結果:

```text
False
False
```

そのため、今回の基本版では **0以上の整数だけ** を扱います。

---

## 7. 四則演算に対応する

`+` だけでなく、`-`, `*`, `/` にも対応します。

```python
stack = []

expression = "3 4 + 5 *"
tokens = expression.split()

for token in tokens:
    if token.isdigit():
        stack.append(int(token))

    elif token == "+":
        b = stack.pop()
        a = stack.pop()
        result = a + b
        stack.append(result)

    elif token == "-":
        b = stack.pop()
        a = stack.pop()
        result = a - b
        stack.append(result)

    elif token == "*":
        b = stack.pop()
        a = stack.pop()
        result = a * b
        stack.append(result)

    elif token == "/":
        b = stack.pop()
        a = stack.pop()
        result = a / b
        stack.append(result)

print(stack)
```

実行結果:

```text
[35]
```

このコードは動きます。

ただし、同じような処理が何度も出てきます。

```python
b = stack.pop()
a = stack.pop()
```

ここから、関数化を考えます。

---

## 8. 計算部分を関数にする

まず、計算だけを担当する関数を作ります。

```python
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
```

動作確認します。

```python
print(calculate(3, 4, "+"))
print(calculate(10, 2, "-"))
print(calculate(3, 4, "*"))
print(calculate(10, 2, "/"))
```

実行結果:

```text
7
8
12
5.0
```

---

## 9. 式全体を計算する関数を作る

次に、逆ポーランド記法の式全体を計算する関数を作ります。

```python
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b


def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        elif token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()

            result = calculate(a, b, token)
            stack.append(result)

    return stack[0]
```

使ってみます。

```python
print(evaluate_rpn("3 4 +"))
print(evaluate_rpn("3 4 + 5 *"))
print(evaluate_rpn("10 2 /"))
```

実行結果:

```text
7
35
5.0
```

---

## 10. エラーについて考える

正しい入力なら、ここまでのプログラムは動きます。

しかし、いつも正しい入力が来るとは限りません。

たとえば、次のような入力はどうでしょうか。

```text
3 +
3 4 5 +
3 a +
3 4 %
3+4
10 0 /
```

プログラムを作るときは、  
「正しいときに動くか」だけでなく、  
「どんなときに壊れそうか」も考える必要があります。

---

## 11. エラーを3つに分けて考える

今回、エラーを次の3つに分けて考えます。

| 分類 | 意味 | 例 |
|---|---|---|
| 入口で防ぐ | 入力がルールに合っているか見る | 数字でも演算子でもない |
| 処理中に防ぐ | 計算しようとした瞬間に問題がないか見る | 数字が足りない |
| 出口で確認する | 処理後の結果が正しい形か見る | 最後に答えが1つだけ残っているか |

エラーハンドリングは、`try-except` だけではありません。  
`if` で確認できることもたくさんあります。

---

## 12. 入口で防ぐエラー

入口では、入力されたものがルールに合っているかを見ます。

今回なら、1つずつ取り出した `token` が、

- 数字か
- 使える演算子か
- それ以外か

を確認します。

```python
if token.isdigit():
    stack.append(int(token))

elif token in ["+", "-", "*", "/"]:
    # 計算する
    pass

else:
    return "エラー: 数字または演算子を入力してください"
```

たとえば、次の入力は入口で止められます。

```text
3 a +
```

`a` は数字でも演算子でもないからです。

---

## 13. 処理中に防ぐエラー

演算子が出てきたら、スタックから数字を2つ取り出します。

しかし、スタックに数字が2つない場合があります。

```text
3 +
```

この式では、`+` が来たときに数字が1つしかありません。

そのため、`pop()` する前に確認します。

```python
if len(stack) < 2:
    return "エラー: 数字が足りません"
```

これは、処理中に防ぐエラーです。

---

## 14. 出口で確認するエラー

正しい逆ポーランド記法なら、計算が終わったあと、スタックには答えが1つだけ残ります。

OK:

```text
3 4 +
```

最後のスタック:

```text
[7]
```

NG:

```text
3 4 5 +
```

最後のスタック:

```text
[3, 9]
```

途中まで計算できていますが、答えが1つにまとまっていません。

そのため、最後に確認します。

```python
if len(stack) != 1:
    return "エラー: 式が正しくありません"
```

---

## 15. 最低限のエラー処理を入れた完成形

次のコードは、基本的なエラーを確認する版です。

```python
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b


def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()

    if expression == "":
        return "エラー: 入力が空です"

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        elif token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                return "エラー: 数字が足りません"

            b = stack.pop()
            a = stack.pop()

            result = calculate(a, b, token)
            stack.append(result)

        else:
            return "エラー: 数字または演算子を入力してください"

    if len(stack) != 1:
        return "エラー: 式が正しくありません"

    return stack[0]


expression = input("逆ポーランド記法の式を入力してください: ")
result = evaluate_rpn(expression)
print(result)
```

---

## 16. 動作確認

次の入力で試してみましょう。

### 正常に計算できる例

```text
3 4 +
```

結果:

```text
7
```

```text
3 4 + 5 *
```

結果:

```text
35
```

```text
10 2 /
```

結果:

```text
5.0
```

### エラーになる例

```text
3 +
```

結果:

```text
エラー: 数字が足りません
```

```text
3 4 5 +
```

結果:

```text
エラー: 式が正しくありません
```

```text
3 a +
```

結果:

```text
エラー: 数字または演算子を入力してください
```

---

## 17. 練習問題

次の入力について、結果を予想してください。

また、エラーになる場合は、  
入口・処理中・出口のどこで気づけるか考えてください。

| 入力 | 結果 | 分類 |
|---|---|---|
| `3 4 +` |  |  |
| `3 4 + 5 *` |  |  |
| `10 2 /` |  |  |
| `3 +` |  |  |
| `3 4 5 +` |  |  |
| `3 a +` |  |  |
| `3 4 %` |  |  |
| 空文字 |  |  |

---

## 18. 発展問題

余裕がある人は、次に挑戦してみましょう。

### 発展1: 0で割るエラーを防ぐ

```text
10 0 /
```

この入力をエラーにしましょう。

ヒント:

```python
if token == "/" and b == 0:
    return "エラー: 0で割ることはできません"
```

### 発展2: 小数を扱う

```text
3.5 2 *
```

`isdigit()` では小数を数字として判定できません。

発展では、`float()` や `try-except` を使う方法があります。

### 発展3: マイナスの数を扱う

```text
-3 4 +
```

`isdigit()` では `-3` を数字として判定できません。

これも発展扱いです。

### 発展4: ファイルから入力する

`input.txt` に式を書いて、Pythonで読み込みます。

```python
with open("input.txt", "r", encoding="utf-8") as file:
    expression = file.read().strip()

result = evaluate_rpn(expression)
print(result)
```

### 発展5: 結果をファイルに書き出す

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(str(result))
```

---

## 19. まとめ

今回のポイントです。

- まず動かす
- 動いたコードを関数化する
- 関数は、処理に名前をつけて整理するために使える
- 正しい入力だけでなく、壊れる入力も考える
- エラーは、入口・処理中・出口に分けて考える
- `try-except` を知らなくても、`if` で防げるエラーはある
- 最初から完璧なコードを書かなくてよい

プログラムがエラーになることは、失敗ではありません。

どんな入力で壊れるかを考えられるようになることが、  
プログラミングの成長です。
