# 正则表达式基础

## 什么是正则表达式？

正则表达式是一种用来表示字符串模式的写法。

在 Linux 中，它主要和 `grep` 之类的命令一起使用。

例如，下面的命令会在 `students.txt` 中查找包含 `a` 的行。

```bash
grep 'a' students.txt
```

## 示例文件

首先，创建一个练习用文件。

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

## `grep` 的基础用法

### 显示包含 `a` 的行

```bash
grep 'a' students.txt
```

输出示例：

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

`AI` 是大写，所以 `grep 'a'` 不会显示它。

## 常用正则表达式

| 写法 | 含义 | 示例 |
|---|---|---|
| `a` | 包含 `a` | `grep 'a' students.txt` |
| `^s` | 以 `s` 开头 | `grep '^s' students.txt` |
| `o$` | 以 `o` 结尾 | `grep 'o$' students.txt` |
| `.` | 任意 1 个字符 | `grep 'a.o' students.txt` |
| `[abc]` | `a`、`b`、`c` 中的任意 1 个字符 | `grep '[abc]' students.txt` |
| `[0-9]` | 1 个数字 | `grep '[0-9]' students.txt` |
| `[a-z]` | 1 个小写英文字母 | `grep '[a-z]' students.txt` |
| `[A-Z]` | 1 个大写英文字母 | `grep '[A-Z]' students.txt` |
| `[^0-9]` | 1 个非数字字符 | `grep '[^0-9]' students.txt` |
| `*` | 前一个字符重复 0 次或多次 | `grep 'a*' students.txt` |
| `+` | 前一个字符重复 1 次或多次 | `grep -E 'a+' students.txt` |
| `?` | 前一个字符重复 0 次或 1 次 | `grep -E 'a?' students.txt` |
| `a\|b` | `a` 或 `b` | `grep -E 'a|b' students.txt` |

## `grep` 和 `grep -E` 的区别

在普通的 `grep` 中，像 `+`、`?`、`|` 这样的符号不太方便直接使用，所以加上 `-E` 后，书写扩展正则表达式会更容易。

```bash
grep -E 'student[0-9]+' students.txt
```

这会查找 `student` 后面跟着一个或多个数字的行。

## 基本示例

### 以 `s` 开头的行

```bash
grep '^s' students.txt
```

### 以 `o` 结尾的行

```bash
grep 'o$' students.txt
```

### 包含数字的行

```bash
grep '[0-9]' students.txt
```

### `student` 后面跟数字的行

```bash
grep -E '^student[0-9]+$' students.txt
```

### 只包含小写字母的行

```bash
grep -E '^[a-z]+$' students.txt
```

### 只包含大写字母的行

```bash
grep -E '^[A-Z]+$' students.txt
```

### 包含 `_` 或 `-` 的行

```bash
grep -E '[_-]' students.txt
```

### 只显示 4 个字符的行

```bash
grep -E '^....$' students.txt
```

`.` 表示任意 1 个字符。

所以 `^....$` 的意思是“从开头到结尾正好 4 个字符”。

### 不区分大小写

```bash
grep -i 'ai' students.txt
```

这种情况下，`AI` 和 `ai` 都会显示。

### 显示不包含 `user` 的行

```bash
grep -v 'user' students.txt
```

`-v` 是一个显示“不符合条件的行”的选项。

## 注意事项

在正则表达式中，一些符号有特殊含义。

例如，`.` 在这里不是普通的句点，而是表示“任意 1 个字符”。

如果你想查找真正的句点，需要写成 `\.`。

```bash
grep '\.' file.txt
```

## 先记住这些

刚开始时，只要先记住下面这五个就够了。

| 写法 | 含义 |
|---|---|
| `^` | 行首 |
| `$` | 行尾 |
| `.` | 任意 1 个字符 |
| `[0-9]` | 数字 |
| `[a-z]` | 小写英文字母 |

## 练习题

请使用 `grep` 显示符合下列条件的行。

1. 包含 `a` 的行
2. 以 `s` 开头的行
3. 以 `o` 结尾的行
4. 包含数字的行
5. 以 `student` 开头，后面跟数字的行
6. 只包含小写字母的行
7. 只包含大写字母的行
8. 包含 `_` 或 `-` 的行
9. 4 个字符的行
10. 包含 `ai` 的行，但不区分大小写
11. 不包含 `user` 的行
12. `python` 后面跟数字的行

## 参考答案

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

## 查看 `man`

你可以用下面的命令查看更多细节。

```bash
man grep
```

即使一开始看不懂全部英文也没关系。

可以一点一点学习，逐步增加你认识的单词和符号。

## 总结

正则表达式并不是需要一次性全部背下来的东西。

在需要的时候一点一点查、一点一点用就可以。

先从用 `grep` 查找字符串开始吧。
