# C言語のループ

この章では、C言語における繰り返し処理を学びます。

プログラムでは、同じ処理を何度も実行したい場面があります。
たとえば、次のような処理です。

* 1から5まで順番に表示する
* 配列の中身を1つずつ表示する
* 条件を満たすまで入力を繰り返す
* ファイルの内容を1行ずつ読む

このような処理を行うために、C言語では `for` 文や `while` 文を使います。

---

## このディレクトリで扱う内容

このディレクトリでは、主に次の内容を扱います。

```text
04_loops/
└── c
    ├── for_array.c
    ├── while_count.c
    ├── loop_until_ok.c
    └── sizeof_items.c
```

---

## コンパイルと実行

C言語のプログラムは、そのままでは実行できません。
まず `gcc` でコンパイルして、実行ファイルを作ります。

このリポジトリでは、生成された実行ファイルを `.gitignore` で無視しやすくするため、実行ファイル名を `.out` で終わる名前にします。

例：

```bash
gcc for_array.c -o for_array.out
./for_array.out
```

---

## 1. while文

`while` 文は、条件が成り立つ間、処理を繰り返します。

## 例：1から5まで表示する

```c
#include <stdio.h>

int main(void) {
    int count = 1;

    while (count <= 5) {
        printf("%d\n", count);
        count++;
    }

    return 0;
}
```

実行例：

```bash
gcc while_count.c -o while_count.out
./while_count.out
```

出力例：

```text
1
2
3
4
5
```

## ポイント

```c
while (count <= 5)
```

は、

```text
count が 5 以下の間、繰り返す
```

という意味です。

また、

```c
count++;
```

は、

```text
count を 1 増やす
```

という意味です。

もし `count++` を書き忘れると、条件がずっと変わらず、無限ループになる可能性があります。

---

## 2. for文

`for` 文は、回数が決まっている繰り返しでよく使われます。

## 例：配列の中身を表示する

```c
#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};

    int length = sizeof(items) / sizeof(items[0]);

    for (int i = 0; i < length; i++) {
        printf("items[%d] = %s\n", i, items[i]);
    }

    return 0;
}
```

実行例：

```bash
gcc for_array.c -o for_array.out
./for_array.out
```

出力例：

```text
items[0] = apple
items[1] = banana
items[2] = orange
```

---

## for文の形

```c
for (int i = 0; i < length; i++) {
    printf("%s\n", items[i]);
}
```

この `for` 文は、次のように読みます。

```text
i を 0 から始める
i が length より小さい間、処理を繰り返す
1回処理が終わるたびに i を 1 増やす
```

つまり、

```text
items[0]
items[1]
items[2]
```

のように、配列の中身を順番に取り出しています。

---

## 3. C言語の配列と length

Pythonでは、リストの長さを `len()` で簡単に取得できます。

```python
items = ["apple", "banana", "orange"]

for item in items:
    print(item)
```

しかし、C言語の配列は、Pythonのリストとは違います。

C言語の配列は、基本的には

```text
決まった数のデータがメモリ上に並んでいるもの
```

です。

配列自身が「自分に何個入っているか」を覚えているわけではありません。

そのため、C言語では配列の要素数を自分で管理する必要があります。

---

## 要素数を直接書く方法

最初は、次のように書いても構いません。

```c
#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};
    int length = 3;

    for (int i = 0; i < length; i++) {
        printf("%s\n", items[i]);
    }

    return 0;
}
```

この書き方はわかりやすいです。

しかし、配列の中身を増やしたときに、`length` を直し忘れる危険があります。

例：

```c
const char *items[] = {"apple", "banana", "orange", "grape"};
int length = 3;
```

この場合、配列には4個の要素がありますが、`length` は3のままです。
そのため、最後の `"grape"` が表示されません。

---

## sizeofを使って要素数を求める方法

C言語では、配列そのものが見えている場所であれば、`sizeof` を使って要素数を計算できます。

```c
int length = sizeof(items) / sizeof(items[0]);
```

これは、

```text
配列全体のサイズ ÷ 配列1個分のサイズ = 要素数
```

という意味です。

たとえば、64bit環境で次の配列を考えます。

```c
const char *items[] = {"apple", "banana", "orange"};
```

この場合、`items` の中には文字列そのものではなく、文字列を指すポインタが入っています。

```text
items[0] → "apple"
items[1] → "banana"
items[2] → "orange"
```

64bit環境では、ポインタ1個のサイズは多くの場合8バイトです。

そのため、次のようになります。

```text
sizeof(items[0]) = 8
sizeof(items)    = 24
length           = 3
```

つまり、

```text
24 ÷ 8 = 3
```

となり、要素数が3であることがわかります。

---

## 4. sizeofの確認

`sizeof` の結果を表示するには、`printf` で `%zu` を使います。

```c
#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};

    printf("sizeof(items[0]) = %zu\n", sizeof(items[0]));
    printf("sizeof(items)    = %zu\n", sizeof(items));

    int length = sizeof(items) / sizeof(items[0]);
    printf("length           = %d\n", length);

    return 0;
}
```

実行例：

```bash
gcc sizeof_items.c -o sizeof_items.out
./sizeof_items.out
```

出力例：

```text
sizeof(items[0]) = 8
sizeof(items)    = 24
length           = 3
```

## ポイント

```c
sizeof(items[0])
```

は、`"apple"` の文字数ではありません。

`items[0]` は `"apple"` を指すポインタです。
そのため、`sizeof(items[0])` はポインタ1個分のサイズになります。

---

## 5. 要素の中身を表示する

配列の要素の中身を表示するには、`items[i]` を使います。

```c
#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};

    int length = sizeof(items) / sizeof(items[0]);

    for (int i = 0; i < length; i++) {
        printf("items[%d] = %s\n", i, items[i]);
    }

    return 0;
}
```

ここでは、

```c
printf("items[%d] = %s\n", i, items[i]);
```

を使っています。

`%d` は整数を表示します。
`%s` は文字列を表示します。

そのため、

```text
items[0] = apple
items[1] = banana
items[2] = orange
```

のように表示されます。

---

## 6. ポインタの住所も表示してみる

C言語では、文字列配列の中には文字列そのものではなく、文字列の場所を表すポインタが入っています。

その住所を表示するには `%p` を使います。

```c
#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};

    int length = sizeof(items) / sizeof(items[0]);

    for (int i = 0; i < length; i++) {
        printf("items[%d] address = %p\n", i, (void *)items[i]);
        printf("items[%d] value   = %s\n", i, items[i]);
    }

    return 0;
}
```

実行すると、次のような出力になります。

```text
items[0] address = 0x55f8...
items[0] value   = apple
items[1] address = 0x55f8...
items[1] value   = banana
items[2] address = 0x55f8...
items[2] value   = orange
```

住所の値は、実行する環境やタイミングによって変わります。
同じ値になるとは限りません。

---

## 7. 条件を満たすまで繰り返す

`while` 文を使うと、条件を満たすまで入力を繰り返すこともできます。

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char input[100];

    while (1) {
        printf("Type ok: ");
        scanf("%99s", input);

        if (strcmp(input, "ok") == 0) {
            break;
        }

        printf("Try again.\n");
    }

    printf("Finished.\n");

    return 0;
}
```

実行例：

```bash
gcc loop_until_ok.c -o loop_until_ok.out
./loop_until_ok.out
```

出力例：

```text
Type ok: hello
Try again.
Type ok: test
Try again.
Type ok: ok
Finished.
```

---

## while (1) の意味

```c
while (1)
```

は、常に条件が真であるため、無限ループになります。

ただし、次の部分でループを抜けています。

```c
if (strcmp(input, "ok") == 0) {
    break;
}
```

`strcmp` は、文字列を比較する関数です。

```c
strcmp(input, "ok") == 0
```

は、

```text
input の中身が "ok" と同じなら
```

という意味です。

`break` は、ループを途中で抜ける命令です。

---

## 8. C言語のループで大切なこと

C言語のループでは、次の点が大切です。

### 1. 何回繰り返すのかを意識する

`for` 文では、開始値・条件・増加の3つを確認します。

```c
for (int i = 0; i < length; i++)
```

この場合は、

```text
i は 0 から始まる
i が length より小さい間だけ繰り返す
1回ごとに i が 1 増える
```

という流れです。

---

### 2. 配列の添字は0から始まる

C言語の配列は、0番目から始まります。

```text
items[0] → apple
items[1] → banana
items[2] → orange
```

3個の要素がある場合、最後の添字は `2` です。
`items[3]` ではありません。

---

### 3. 配列の範囲外にアクセスしない

次のようなコードは危険です。

```c
const char *items[] = {"apple", "banana", "orange"};

printf("%s\n", items[3]);
```

`items[3]` は存在しません。

C言語では、配列の範囲外にアクセスしても、すぐにわかりやすいエラーが出るとは限りません。
意図しない動作をする可能性があります。

---

### 4. 無限ループに注意する

次のコードは危険です。

```c
int count = 1;

while (count <= 5) {
    printf("%d\n", count);
}
```

`count` が増えていないため、条件がずっと変わりません。
そのため、無限ループになります。

正しくは次のようにします。

```c
int count = 1;

while (count <= 5) {
    printf("%d\n", count);
    count++;
}
```

---

## 9. Pythonとの違い

Pythonでは、リストの中身を直接取り出して繰り返せます。

```python
items = ["apple", "banana", "orange"]

for item in items:
    print(item)
```

C言語では、何番目の要素を見るかを自分で管理することが多いです。

```c
const char *items[] = {"apple", "banana", "orange"};

int length = sizeof(items) / sizeof(items[0]);

for (int i = 0; i < length; i++) {
    printf("%s\n", items[i]);
}
```

Pythonは便利です。
C言語は少し手間がかかります。

しかし、C言語では

```text
配列
添字
メモリ上のサイズ
ポインタ
文字列
```

といった、コンピュータのしくみに近い考え方を学ぶことができます。

---

## 10. まとめ

C言語のループでは、次のことを意識しましょう。

- for文は、回数が決まっている繰り返しでよく使う
- while文は、条件が成り立つ間、繰り返す
- 配列の添字は0から始まる
- C言語の配列は、自分の要素数を覚えていない
- sizeofを使うと、配列の要素数を計算できる場合がある
- 文字列配列の要素は、文字列そのものではなくポインタである

最初からすべてを完全に理解する必要はありません。

まずは、次を意識することが大切です。

- C言語では、何番目の要素を見ているのかを自分で意識する

ループは、配列・ファイル処理・文字列処理・データ処理の基礎になります。
繰り返し処理に慣れることで、より複雑なプログラムも少しずつ読めるようになります。
