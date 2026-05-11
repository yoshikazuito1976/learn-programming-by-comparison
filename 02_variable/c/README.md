# 02_variable / C

## 目的

C言語で変数を使い、文字列・整数・小数の扱いを確認する。  
また、JavaやPythonと比較しながら、Cでは変数に「型」を明示する必要があることを理解する。

## ソースコード

```c
#include <stdio.h>

int main(void) {
    char name[] = "yoshikazu";
    int age = 48;
    double height = 170.5;

    printf("%s\n", name);
    printf("name\n");
    printf("Hello, %s\n", name);

    printf("%d\n", age);
    printf("%f\n", height);

    printf("Age: %d\n", age);
    printf("Height: %.1f\n", height);

    return 0;
}
```

## コンパイルと実行
```bash
gcc hello_variable.c -o hello_variable
./hello_variable
```

## 実行結果
```bash
yoshikazu
name
Hello, yoshikazu
48
170.500000
Age: 48
Height: 170.5
```

## 確認ポイント
- Cでは変数に型を書く

- C言語では、変数を使うときに「どの種類の値を入れるのか」を先に書く。
```bash
char name[] = "yoshikazu";
int age = 48;
double height = 170.5;
```

それぞれの意味は次の通り。
```text
char name[]     → 文字列
int age         → 整数
double height   → 小数
```

Cでは、Pythonのように次のようには書けない。
```bash
name = "yoshikazu"
age = 48
height = 170.5
```

Cでは、変数名の前に型を書く必要がある。

## 文字列の表示
```c
printf("%s\n", name);
```
%s は、文字列を表示するための指定である。
この場合、変数 name の中身である yoshikazu が表示される。
```c
printf("name\n");
```
これは、変数 name の中身ではなく、name という文字そのものを表示している。

つまり、次の2つは意味が違う。

```bash
printf("%s\n", name);
printf("name\n");
```

name   → 変数
"name" → 文字列

## 文字列と変数を組み合わせる
```bash
printf("Hello, %s\n", name);
```

%s の部分に、変数 name の中身が入る。

そのため、実行結果は次のようになる。
```bash
Hello, yoshikazu
```

Pythonのf文字列と比べると、次のような対応になる。

```python
print(f"Hello, {name}")
```

Cでは {name} のようには書かず、%s という場所を用意して、あとから name を渡す。
```c
printf("Hello, %s\n", name);
```

## 数字の表示

Cでは、整数と小数で表示の指定が変わる。
```c
int age = 48;
double height = 170.5;
```

整数を表示する場合は %d を使う。
```c
printf("%d\n", age);
```

小数を表示する場合は %f を使う。
```c
printf("%f\n", height);
```
実行結果は次のようになる。
``` bash
48
170.500000
```
%f では、標準では小数点以下が6桁表示される。

小数の表示桁数を指定する
printf("Height: %.1f\n", height);

%.1f は、小数第1位まで表示する指定である。

実行結果は次のようになる。

```bash
Height: 170.5
printfの指定
```
Cの printf では、値の種類に応じて指定を変える。

%s → 文字列
%d → 整数
%f → 小数

今回のコードでは、次のように使っている。

```c
printf("%s\n", name);
printf("%d\n", age);
printf("%f\n", height);
```

## Javaとの比較

Javaでは、文字列・整数・小数を次のように扱う。
```java
String name = "yoshikazu";
int age = 48;
double height = 170.5;

System.out.println(name);
System.out.println("name");
System.out.println("Hello, " + name);
System.out.println(age);
System.out.println(height);
```

## CとJavaは、どちらも変数に型を書く。
```c
C:
char name[] = "yoshikazu";
int age = 48;
double height = 170.5;
```
```java
Java:
String name = "yoshikazu";
int age = 48;
double height = 170.5;
```
ただし、文字列の扱いは違う。

```bash
C      → char name[]
Java   → String name
```

Javaには String という文字列用の型がある。
Cでは、文字列は char の配列として扱う。

## Pythonとの比較

Pythonでは、変数に型を書かない。
```python
name = "yoshikazu"
age = 48
height = 170.5

print(name)
print("name")
print(f"Hello, {name}")
print(age)
print(height)
```
Cと比べると、Pythonはかなり短く書ける。

```c
C:
char name[] = "yoshikazu";
int age = 48;
double height = 170.5;
```
```python
Python:
name = "yoshikazu"
age = 48
height = 170.5
```

Pythonでは型を書かないが、値の種類がなくなるわけではない。
"yoshikazu" は文字列、48 は整数、170.5 は小数として扱われる。


## C / Java / Python の比較

### 文字列
char name[] = "yoshikazu";
String name = "yoshikazu";
name = "yoshikazu"
### 整数
int age = 48;
int age = 48;
age = 48
### 小数
double height = 170.5;
double height = 170.5;
height = 170.5

## まとめ
Cでは、変数を使うときに型を書く
char name[] は文字列を扱うための変数
int は整数を扱う型
double は小数を扱う型
printf では、表示する値の種類に応じて %s、%d、%f を使い分ける
Javaも型を書くが、文字列は String を使う
Pythonは型を書かずに変数を使える
どの言語でも、変数名と文字列は区別する必要がある
