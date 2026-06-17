# 正規表現の基本

## 正規表現とは

正規表現とは、文字列のパターンを表すための書き方です。

Linux では、主に `grep` コマンドなどで使います。

たとえば、次のコマンドは `students.txt` の中から `a` を含む行を探します。

```bash
grep 'a' students.txt
```

## 例題用ファイル

まず、練習用のファイルを作成します。

```bash
cat > students.txt << 'DATA'
sato
suzuki
tanaka
ito
kato
saito
sasaki
yamada
yamamoto
john
alice
bob
student01
student02
test_user
user-test
linux2026
python3
AI
ai
DATA
```

## `grep` の基本

### `a` を含む行を表示する

```bash
grep 'a' students.txt
```

実行結果の例:

```text
sato
tanaka
kato
saito
sasaki
yamada
yamamoto
alice
ai
```

`AI` は大文字なので、`grep 'a'` では表示されません。

## よく使う正規表現

| 書き方 | 意味 | 例 |
|---|---|---|
| `a` | `a` を含む | `grep 'a' students.txt` |
| `^s` | `s` で始まる | `grep '^s' students.txt` |
| `o$` | `o` で終わる | `grep 'o$' students.txt` |
| `.` | 任意の 1 文字 | `grep 'a.o' students.txt` |
| `[abc]` | `a`, `b`, `c` のどれか 1 文字 | `grep '[abc]' students.txt` |
| `[0-9]` | 数字 1 文字 | `grep '[0-9]' students.txt` |
| `[a-z]` | 小文字の英字 1 文字 | `grep '[a-z]' students.txt` |
| `[A-Z]` | 大文字の英字 1 文字 | `grep '[A-Z]' students.txt` |
| `[^0-9]` | 数字以外の 1 文字 | `grep '[^0-9]' students.txt` |
| `*` | 直前の文字が 0 回以上 | `grep 'a*' students.txt` |
| `+` | 直前の文字が 1 回以上 | `grep -E 'a+' students.txt` |
| `?` | 直前の文字が 0 回または 1 回 | `grep -E 'a?' students.txt` |
| `a\|b` | `a` または `b` | `grep -E 'a|b' students.txt` |

## `grep` と `grep -E` の違い

`grep` では、`+`、`?`、`|` などをそのまま使いにくいため、拡張正規表現を使うときは `-E` を付けると書きやすくなります。

```bash
grep -E 'student[0-9]+' students.txt
```

これは、`student` の後ろに数字が 1 文字以上続く行を探します。

## 基本例

### `s` で始まる行

```bash
grep '^s' students.txt
```

### `o` で終わる行

```bash
grep 'o$' students.txt
```

### 数字を含む行

```bash
grep '[0-9]' students.txt
```

### `student` の後ろに数字がある行

```bash
grep -E '^student[0-9]+$' students.txt
```

### 小文字だけの行

```bash
grep -E '^[a-z]+$' students.txt
```

### 大文字だけの行

```bash
grep -E '^[A-Z]+$' students.txt
```

### `_` または `-` を含む行

```bash
grep -E '[_-]' students.txt
```

### 4 文字の行だけを表示する

```bash
grep -E '^....$' students.txt
```

`.` は任意の 1 文字を表します。

そのため、`^....$` は「最初から最後まで 4 文字」という意味になります。

### 大文字小文字を区別しない

```bash
grep -i 'ai' students.txt
```

この場合、`AI` と `ai` の両方が表示されます。

### `user` を含まない行を表示する

```bash
grep -v 'user' students.txt
```

`-v` は、条件に合わない行を表示するオプションです。

## 注意点

正規表現では、記号に特別な意味があります。

たとえば、`.` は普通のピリオドではなく、「任意の 1 文字」という意味になります。

普通のピリオドとして探したい場合は、`\.` のように書きます。

```bash
grep '\.' file.txt
```

## まず覚えるもの

最初は、次の 5 つだけ覚えれば十分です。

| 書き方 | 意味 |
|---|---|
| `^` | 行の先頭 |
| `$` | 行の最後 |
| `.` | 任意の 1 文字 |
| `[0-9]` | 数字 |
| `[a-z]` | 小文字の英字 |

## 練習問題

次の条件に合う行を `grep` で表示しなさい。

1. `a` を含む行
2. `s` で始まる行
3. `o` で終わる行
4. 数字を含む行
5. `student` で始まり、その後ろに数字がある行
6. 小文字だけの行
7. 大文字だけの行
8. `_` または `-` を含む行
9. 4 文字の行
10. `ai` を含む行。ただし、大文字小文字は区別しない
11. `user` を含まない行
12. `python` の後ろに数字がある行

## 練習問題の解答例

```bash
grep 'a' students.txt
grep '^s' students.txt
grep 'o$' students.txt
grep '[0-9]' students.txt
grep -E '^student[0-9]+$' students.txt
grep -E '^[a-z]+$' students.txt
grep -E '^[A-Z]+$' students.txt
grep -E '[_-]' students.txt
grep -E '^....$' students.txt
grep -i 'ai' students.txt
grep -v 'user' students.txt
grep -E '^python[0-9]+$' students.txt
```

## `man` を見る

詳しい使い方は、次のコマンドで確認できます。

```bash
man grep
```

英語が全部わからなくても大丈夫です。

少しずつ、知っている単語や記号を増やしていきましょう。

## まとめ

正規表現は、全部を暗記するものではありません。

必要になったときに、少しずつ調べながら使います。

まずは、`grep` で文字列を探すところから始めましょう。
