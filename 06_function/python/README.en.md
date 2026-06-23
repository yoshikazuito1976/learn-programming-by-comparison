# 06 Functions

In this chapter, you will learn how to group processing steps into functions.

If you write similar processing many times, your program becomes hard to read.
By using functions, you can name processing and call it whenever you need it.

---

## Goal of This Chapter

The goal of this chapter is to understand the basics of functions.

When writing programs, you may want to write the same kind of processing again and again.

For example, you might print greetings many times like this:

```python
print("Hello, ITO!")
print("Hello, Python!")
print("Hello, Programming!")
```

You can organize this kind of processing by using functions.

With functions, you can name processing and call it when needed.

---

## Keywords

- function
- definition
- call
- argument
- return value
- return
- reuse
- divide processing

---

## What Is a Function?

A function is a named group of processing steps.

In Python, you define a function using `def`.

```python
def greet():
    print("Hello!")
```

In this example, you create a function named `greet`.

However, defining a function alone does not execute it.

To execute a function, write its name and call it.

```python
greet()
```

---

## Basic Function Form

The basic form of a function in Python is as follows:

```python
def function_name():
    processing
```

For example:

```python
def greet():
    print("Hello!")


greet()
```

The output is:

```text
Hello!
```

---

## Calling a Function

You can call a function many times.

```python
def greet():
    print("Hello!")


greet()
greet()
greet()
```

The output is:

```text
Hello!
Hello!
Hello!
```

You do not need to write the same processing repeatedly. Just call the function.

---

## What Is an Argument?

An argument is a value passed to a function.

In the following example, `name` is an argument.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

The output is:

```text
Hello, ITO!
Hello, Python!
```

When you write `greet("ITO")`, `"ITO"` is assigned to `name`.

When you write `greet("Python")`, `"Python"` is assigned to `name`.

---

## Why Use Arguments?

By using arguments, you can pass values from outside into a function.

This allows you to run similar processing with small differences.

```python
def introduce(name, language):
    print(f"{name} is learning {language}.")


introduce("ITO", "Python")
introduce("Tanaka", "Shell")
```

The output is:

```text
ITO is learning Python.
Tanaka is learning Shell.
```

In this example, two arguments are used: `name` and `language`.

---

## What Is a Return Value?

A return value is a value that comes back from a function.

In Python, you return a value using `return`.

```python
def add(a, b):
    return a + b


result = add(3, 5)
print(result)
```

The output is:

```text
8
```

In this example, `add(3, 5)` returns `8`.

That returned value is stored in a variable named `result`.

---

## Difference Between print and return

`print` is used to display something on the screen.

`return` is used to return the result of a function.

Look at the following example.

```python
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


add_print(3, 5)

result = add_return(3, 5)
print(result)
```

`print` displays a value.

`return` returns a value.

Returned values can be stored in variables or used in other calculations.

---

## Using Return Values in Calculations

Return values can be used in later processing.

```python
def add(a, b):
    return a + b


result = add(3, 5)
double_result = result * 2

print(result)
print(double_result)
```

The output is:

```text
8
16
```

By storing function results in variables, you can use them easily later.

---

## Conditionals and Functions

You can also use conditionals inside functions.

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


result = judge(75)
print(result)
```

The output is:

```text
Pass
```

If `score` is 60 or higher, the function returns `"Pass"`.

Otherwise, it returns `"Fail"`.

---

## Input and Functions

You can combine `input` with functions.

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


score = int(input("Enter your score: "))
result = judge(score)
print(result)
```

An execution example is:

```text
Enter your score: 80
Pass
```

The function judges using the value entered by the user.

---

## Loops and Functions

Functions can also be combined with loops.

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

The output is:

```text
92: Pass
85: Pass
74: Pass
66: Pass
39: Fail
```

Each score in the list is taken one by one and judged by the function.

---

## Code Before Refactoring into a Function

The following code judges a score.

```python
score = 75

if score >= 60:
    result = "Pass"
else:
    result = "Fail"

print(result)
```

This works.

However, if you want to judge scores many times, you will repeat similar processing.

---

## Code After Refactoring into a Function

If you put the same processing into a function, it becomes:

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


result = judge(75)
print(result)
```

By turning it into a function, you can give the score-judging process the name `judge`.

---

## Benefits of Refactoring into Functions

Refactoring into functions has these benefits.

- You do not need to write the same processing repeatedly.
- Programs become easier to read.
- You reduce the number of places to modify.
- You can give names to processing.
- You can think about programs in separate parts.

As programs get longer, organizing them with functions becomes more important.

---

## How to Name Functions

Use names that clearly show what the function does.

Good examples:

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"
```

```python
def add(a, b):
    return a + b
```

Less good examples:

```python
def x(a):
    return a + 10
```

```python
def test(data):
    print(data)
```

Names that are too short or too broad become hard to read later.

---

## Notes When Writing Functions

When writing functions, pay attention to indentation.

In Python, processing inside a function must be indented.

```python
def greet():
    print("Hello!")
```

If indentation is missing like below, you get an error.

```python
def greet():
print("Hello!")
```

In Python, indentation is very important.

---

## Practice 1: Greeting Function

Create a function with the following requirements.

- Function name: `greet`
- Argument: `name`
- Display `Hello, name!`

Example:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

---

## Practice 2: Addition Function

Create a function with the following requirements.

- Function name: `add`
- Arguments: `a` and `b`
- Return the result of `a + b`

Example:

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

---

## Practice 3: Score Judgment Function

Create a function with the following requirements.

- Function name: `judge`
- Argument: `score`
- Return `"Pass"` for scores 60 or higher
- Return `"Fail"` for scores below 60

Example:

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


print(judge(80))
print(judge(45))
```

---

## Practice 4: List and Function

You have the following list of scores.

```python
scores = [92, 85, 74, 66, 39]
```

Use the `judge` function to evaluate each score.

Example:

```python
def judge(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

---

## Practice 5: Rank Function

Create a function that returns ranks as follows.

- 90 or above: A
- 80 or above: B
- 70 or above: C
- 60 or above: D
- Below 60: F

Example:

```python
def rank(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = rank(score)
    print(f"{score}: {result}")
```

The output is:

```text
92: A
85: B
74: C
66: D
39: F
```

---

## Chapter Summary

In this chapter, you learned about functions.

A function is a mechanism to name and group processing.

By using functions, you can avoid writing the same processing repeatedly.

You can also organize programs so they are easier to read.

---

## Important Points

- Define functions with `def`
- A function does not run unless you call it
- Arguments let you pass values to functions
- `return` lets you return values from functions
- Refactoring into functions makes programs easier to organize

---

## What to Learn Next

Once you can use functions, you can think of programs as combinations of parts.

Next, you will connect this to topics for writing longer programs, such as file input/output and error handling.
