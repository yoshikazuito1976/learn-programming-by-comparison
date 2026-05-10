# 02_variable / Java

## 目的

Javaで変数を使い、文字列と変数名の違いを理解する。  
また、Javaのコンパイルと実行、ファイル名とクラス名の関係を確認する。

## ソースコード

```java
public class HelloVariable {
    public static void main(String[] args) {
        String name = "yoshikazu";

        System.out.println(name);
        System.out.println("name");
        System.out.println("Hello, " + name);
    }
}
```

## コンパイルと実行
```bash
javac HelloVariable.java
java HelloVariable
```

## 実行結果
```text
yoshikazu
name
Hello, yoshikazu
```

## 確認ポイント
- String name = "yoshikazu"; は、変数 name に文字列を代入している
- System.out.println(name); は、変数の中身を表示する
- System.out.println("name"); は、name という文字そのものを表示する
- Javaでは、文字列は " で囲む
- javac で .java ファイルをコンパイルすると .class ファイルが生成される
- java HelloVariable では .java や .class を付けない

## よくあるエラー
### ファイル名とクラス名が違う
```bash
javac HelloVriable.java
```

クラス HelloVariableはpublicであり、ファイルHelloVariable.javaで宣言する必要があります

Javaでは、public class HelloVariable と書いた場合、ファイル名は HelloVariable.java にする必要がある。

修正例：
```bash
mv HelloVriable.java HelloVariable.java
javac HelloVariable.java
java HelloVariable
```

## .java と .class
```bash
ls

HelloVariable.class  HelloVariable.java
```

- HelloVariable.java は、人間が書くソースコード
- HelloVariable.class は、コンパイルによって生成されたファイル

```bash
file HelloVariable.class

HelloVariable.class: compiled Java class data, version 65.0
file HelloVariable.java
HelloVariable.java: C source, ASCII text
```

file コマンドは拡張子だけでなく、ファイルの中身を見て種類を推測する。
そのため、Javaのソースコードが C source と判定されることもある。
