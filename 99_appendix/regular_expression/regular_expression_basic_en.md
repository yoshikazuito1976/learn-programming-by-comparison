# Basic Regular Expressions

## What Is a Regular Expression?

A regular expression is a way to describe a pattern in text.

In Linux, it is mainly used with commands such as `grep`.

For example, the following command searches for lines containing `a` in `students.txt`.

```bash
grep 'a' students.txt
```

## Example File

First, create a file for practice.

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

## Basic `grep`

### Show lines containing `a`

```bash
grep 'a' students.txt
```

Example output:

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

`AI` is uppercase, so it is not shown by `grep 'a'`.

## Common Regular Expressions

| Pattern | Meaning | Example |
|---|---|---|
| `a` | contains `a` | `grep 'a' students.txt` |
| `^s` | starts with `s` | `grep '^s' students.txt` |
| `o$` | ends with `o` | `grep 'o$' students.txt` |
| `.` | any one character | `grep 'a.o' students.txt` |
| `[abc]` | one of `a`, `b`, or `c` | `grep '[abc]' students.txt` |
| `[0-9]` | one digit | `grep '[0-9]' students.txt` |
| `[a-z]` | one lowercase letter | `grep '[a-z]' students.txt` |
| `[A-Z]` | one uppercase letter | `grep '[A-Z]' students.txt` |
| `[^0-9]` | one non-digit character | `grep '[^0-9]' students.txt` |
| `*` | the previous character appears 0 or more times | `grep 'a*' students.txt` |
| `+` | the previous character appears 1 or more times | `grep -E 'a+' students.txt` |
| `?` | the previous character appears 0 or 1 time | `grep -E 'a?' students.txt` |
| `a\|b` | `a` or `b` | `grep -E 'a|b' students.txt` |

## Difference Between `grep` and `grep -E`

With plain `grep`, symbols such as `+`, `?`, and `|` are less convenient to use directly, so adding `-E` makes extended regular expressions easier to write.

```bash
grep -E 'student[0-9]+' students.txt
```

This searches for lines where `student` is followed by one or more digits.

## Basic Examples

### Lines starting with `s`

```bash
grep '^s' students.txt
```

### Lines ending with `o`

```bash
grep 'o$' students.txt
```

### Lines containing digits

```bash
grep '[0-9]' students.txt
```

### Lines where `student` is followed by digits

```bash
grep -E '^student[0-9]+$' students.txt
```

### Lines containing only lowercase letters

```bash
grep -E '^[a-z]+$' students.txt
```

### Lines containing only uppercase letters

```bash
grep -E '^[A-Z]+$' students.txt
```

### Lines containing `_` or `-`

```bash
grep -E '[_-]' students.txt
```

### Show only 4-character lines

```bash
grep -E '^....$' students.txt
```

`.` means any one character.

So `^....$` means "exactly 4 characters from beginning to end".

### Ignore uppercase and lowercase differences

```bash
grep -i 'ai' students.txt
```

In this case, both `AI` and `ai` are shown.

### Show lines that do not contain `user`

```bash
grep -v 'user' students.txt
```

`-v` is an option that shows lines that do not match the condition.

## Notes

In regular expressions, some symbols have special meanings.

For example, `.` does not mean a normal period here. It means "any one character".

If you want to search for an actual period, write `\.`.

```bash
grep '\.' file.txt
```

## First Things to Remember

At first, it is enough to remember these five:

| Pattern | Meaning |
|---|---|
| `^` | start of line |
| `$` | end of line |
| `.` | any one character |
| `[0-9]` | digit |
| `[a-z]` | lowercase letter |

## Practice Questions

Use `grep` to display lines that match the following conditions.

1. Lines containing `a`
2. Lines starting with `s`
3. Lines ending with `o`
4. Lines containing digits
5. Lines starting with `student` followed by digits
6. Lines containing only lowercase letters
7. Lines containing only uppercase letters
8. Lines containing `_` or `-`
9. Lines with 4 characters
10. Lines containing `ai`, ignoring uppercase and lowercase differences
11. Lines not containing `user`
12. Lines where `python` is followed by digits

## Sample Answers

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

## See `man`

You can check more details with the following command.

```bash
man grep
```

It is okay if you do not understand all the English at first.

Learn little by little, and increase the number of words and symbols you recognize.

## Summary

Regular expressions are not something you must memorize all at once.

Use them little by little whenever you need them.

Start by searching for strings with `grep`.
