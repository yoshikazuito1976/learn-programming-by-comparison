# 03_conditions - C

このフォルダでは、C言語で条件分岐を学びます。

## 学ぶこと

- `if`
- `else`
- 比較演算子
- 変数と型
- `{}` による処理のまとまり

## 基本の形

```c
if (条件式) {
    条件が正しいときの処理
} else {
    条件が正しくないときの処理
}
```

## 実行方法
```bash
gcc conditions_basic.c -o conditions_basic
./conditions_basic
```

## Pythonとの違い

Pythonではインデントで処理のまとまりを表します。
```python
if score >= 60:
    print("合格です")
else:
    print("不合格です")
```

C言語では {} で処理のまとまりを表します。
```c
if (score >= 60) {
    printf("合格です\n");
} else {
    printf("不合格です\n");
}
```

## Rustとの違い

Rustも {} を使いますが、C言語では printf を使って表示します。

```c
printf("合格です\n");
```

また、C言語では main 関数の最後に return 0; を書くことがあります。
```c
return 0;
```