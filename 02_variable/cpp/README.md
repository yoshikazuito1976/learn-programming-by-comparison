# 02_variable / C++

## 目的

C++で変数を使い、文字列・整数・小数の扱いを確認する。  
また、Bash、Python、Java、Cと比較しながら、画面への表示方法の違いを理解する。

## ソースコード

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name = "yoshikazu";
    int age = 48;
    double height = 170.5;

    std::cout << name << std::endl;
    std::cout << "name" << std::endl;
    std::cout << "Hello, " << name << std::endl;

    std::cout << age << std::endl;
    std::cout << height << std::endl;

    std::cout << "Age: " << age << std::endl;
    std::cout << "Height: " << height << std::endl;

    return 0;
}
```

## コンパイルと実行
```bash
g++ hello_variable.cpp -o hello_variable
./hello_variable
```

###実行結果
```bash
yoshikazu
name
Hello, yoshikazu
48
170.5
Age: 48
Height: 170.5
```
### 確認ポイント
C++では変数に型を書く
```bash
std::string name = "yoshikazu";
int age = 48;
double height = 170.5;
```
それぞれの意味は次の通り。

```text
std::string name → 文字列
int age          → 整数
double height    → 小数
```

C++では、Pythonのように型を書かずに変数を作るのではなく、変数名の前に型を書く。

```bash
name = "yoshikazu"
age = 48
height = 170.5
```

## 変数と文字列の違い
```bash
std::cout << name << std::endl;
std::cout << "name" << std::endl;
```
この2つは意味が違う。

name   → 変数 name の中身
"name" → name という文字そのもの
画面への表示方法の比較

言語によって、画面に文字を表示する書き方が違う。

```text
Bashでは echo で表示する。
Pythonでは print() で表示する。
Javaでは System.out.println() で表示する。
Cでは printf() で表示する。
C++では std::cout に << で送って表示する。
```

C++では、次のように書く。
```bash
std::cout << "Hello, " << name << std::endl;
```
これは、std::cout に対して、表示したいものを左から順番に送っている。

"Hello, "
name の中身
std::endl

## std::cout の読み方
std::cout

std::cout は、一般に「エスティーディー・シーアウト」と読む。

cout は、標準出力に文字や値を表示するためのもの。
Bashの echo、Pythonの print()、Cの printf() に近い役割を持つ。

## std::endl の読み方と役割
std::endl;

std::endl は、一般に「エスティーディー・エンドル」または「エスティーディー・エンドライン」と読む。

意味としては、行を終える、つまり改行するためのもの。
```bash
std::cout << "Hello" << std::endl;
std::cout << "World" << std::endl;
```

実行結果は次のようになる。
```bash
Hello
World
```

std::endl がないと、出力が同じ行につながって表示されることがある。


## C / C++ / Java / Python の比較
```text
文字列
char name[] = "yoshikazu";
std::string name = "yoshikazu";
String name = "yoshikazu";
name = "yoshikazu"
整数
int age = 48;
int age = 48;
int age = 48;
age = 48
小数
double height = 170.5;
double height = 170.5;
double height = 170.5;
height = 170.5
```

## まとめ
- C++では、変数を使うときに型を書く
- std::string は文字列を扱う型
- int は整数を扱う型
- double は小数を扱う型
- std::cout は「エスティーディー・シーアウト」と読む
- std::cout に << で値を送ると、画面に表示できる
- std::endl は「エスティーディー・エンドル」または「エスティーディー・エンドライン」と読む
- std::endl は改行を表す
- Bash、Python、Java、C、C++では、表示の書き方がそれぞれ違う
