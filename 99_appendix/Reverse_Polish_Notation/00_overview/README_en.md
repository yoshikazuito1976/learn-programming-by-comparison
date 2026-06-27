# Understanding Reverse Polish Notation

In this material, we use Python to understand **Reverse Polish Notation (RPN)**.

RPN is a notation in which operators are written after the numbers.

Standard notation:

```text
3 + 4
```

Reverse Polish Notation:

```text
3 4 +
```

Standard notation:

```text
( 3 + 4 ) * 2
```

Reverse Polish Notation:

```text
3 4 + 2 *
```

In this material, we use Python lists as a **stack** to learn how to evaluate RPN expressions and convert standard expressions into RPN.

## Goals

The goal of this material is not simply to build a calculator.

The aim is to understand the following concepts through programming:

- Lists
- `append()`
- `pop()`
- Conditional branching
- Loops
- Functions
- String processing
- Stack
- Operator precedence
- Expression conversion

## What is Reverse Polish Notation?

In standard notation, operators are written between numbers.

```text
3 + 4
```

This is called **infix notation**.

In Reverse Polish Notation, operators are written after the numbers.

```text
3 4 +
```

This expression is read as:

> Add 3 and 4.

A slightly more complex example:

```text
3 4 + 2 *
```

This has the same meaning as:

```text
( 3 + 4 ) * 2
```

The result is `14`.

## What is a Stack?

A stack is a data structure where the last item added is the first item removed.

In English, this is called **Last In, First Out**, or **LIFO** for short.

In Python, we can represent stack behavior using a list.

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

x = stack.pop()
print(x)
print(stack)
```

Output:

```text
['A', 'B', 'C']
C
['A', 'B']
```

`"C"`, the last item added, is the first one removed.

## Step 1: Observe the Stack

First, let's observe how the stack works without any calculation.

```python
stack = []

stack.append(3)
stack.append(4)

print(stack)

x = stack.pop()
print(x)

y = stack.pop()
print(y)

print(stack)
```

Output:

```text
[3, 4]
4
3
[]
```

Use `append()` to push values and `pop()` to retrieve them.

## Step 2: Read RPN by Hand

Consider the following expression:

```text
3 4 +
```

Here is how to read it:

| Token | Stack |
|---|---|
| 3 | 3 |
| 4 | 3, 4 |
| + | 7 |

When `+` appears, pop two numbers from the stack and calculate.

```text
3 + 4 = 7
```

Push the result `7` back onto the stack.

## Step 3: Evaluate an RPN Expression

Let's write a program to calculate `3 4 +`.

```python
tokens = ["3", "4", "+"]

stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b

        stack.append(result)

print(stack[0])
```

Output:

```text
7
```

## Step 4: Support All Four Operations

Add support for `-`, `*`, and `/` in addition to `+`.

```python
tokens = ["3", "4", "+", "2", "*"]

stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b
        elif token == "-":
            result = a - b
        elif token == "*":
            result = a * b
        elif token == "/":
            result = a / b

        stack.append(result)

print(stack[0])
```

Output:

```text
14
```

This expression has the same meaning as:

```text
( 3 + 4 ) * 2
```

## Step 5: Convert to a Function

Turn the logic into a function so it can be reused.

```python
def calc_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)

    return stack[0]


print(calc_rpn("3 4 +"))
print(calc_rpn("3 4 + 2 *"))
print(calc_rpn("10 3 -"))
```

Output:

```text
7
14
7
```

## Step 6: Convert a Standard Expression to RPN

Next, let's convert a standard expression to RPN.

Standard notation:

```text
3 + 4 * 2
```

Reverse Polish Notation:

```text
3 4 2 * +
```

We use two lists:

```python
output = []  # Holds the converted expression
stack = []   # Temporarily holds operators
```

Operators have precedence:

```python
priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
```

`*` and `/` are calculated before `+` and `-`.

## Step 7: Convert Without Parentheses

First, let's convert expressions without parentheses.

```python
def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while stack and priority[stack[-1]] >= priority[token]:
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


print(infix_to_rpn("3 + 4"))
print(infix_to_rpn("3 + 4 * 2"))
print(infix_to_rpn("3 * 4 + 2"))
```

Output:

```text
3 4 +
3 4 2 * +
3 4 * 2 +
```

## Step 8: Support Parentheses

Now add support for parentheses.

```python
def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while (
                stack
                and stack[-1] != "("
                and priority[stack[-1]] >= priority[token]
            ):
                output.append(stack.pop())

            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

    while stack:
        output.append(stack.pop())

    return " ".join(output)


print(infix_to_rpn("( 3 + 4 ) * 2"))
print(infix_to_rpn("3 * ( 4 + 2 )"))
```

Output:

```text
3 4 + 2 *
3 4 2 + *
```

## Step 9: Convert and Evaluate

Finally, convert a standard expression to RPN and evaluate it.

```python
def calc_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)

    return stack[0]


def infix_to_rpn(expression):
    tokens = expression.split()

    output = []
    stack = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in priority:
            while (
                stack
                and stack[-1] != "("
                and priority[stack[-1]] >= priority[token]
            ):
                output.append(stack.pop())

            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

    while stack:
        output.append(stack.pop())

    return " ".join(output)


normal_expression = "( 3 + 4 ) * 2"

rpn_expression = infix_to_rpn(normal_expression)
answer = calc_rpn(rpn_expression)

print("Standard:", normal_expression)
print("RPN:", rpn_expression)
print("Result:", answer)
```

Output:

```text
Standard: ( 3 + 4 ) * 2
RPN: 3 4 + 2 *
Result: 14
```

## Input Rules

In this material, expressions must be written with spaces between each token.

OK:

```text
3 + 4
3 + 4 * 2
( 3 + 4 ) * 2
```

NG:

```text
3+4
3+4*2
(3+4)*2
```

Handling expressions without spaces is left as an advanced exercise.

## Exercises

### Required

Write a function `calc_rpn()` that evaluates an RPN expression.

Make sure it can handle the following:

```text
3 4 +
3 4 + 2 *
10 3 -
10 2 /
```

### Standard

Write a function `infix_to_rpn()` that converts a standard expression to RPN.

Make sure it can handle the following:

```text
3 + 4
3 + 4 * 2
3 * 4 + 2
```

### Advanced

Add support for parentheses.

Make sure it can handle the following:

```text
( 3 + 4 ) * 2
3 * ( 4 + 2 )
( 10 - 3 ) * ( 2 + 1 )
```

## Submission

Submit the following:

- Stack behavior demonstration
- `calc_rpn()` program
- `infix_to_rpn()` program
- Output using at least 3 expressions of your own
- Explanation of the program

## Review

Explain each of the following in your own words:

- What is a stack?
- What does `append()` do?
- What does `pop()` do?
- Why do we use a stack for RPN?
- Why is operator precedence needed when converting to RPN?

## Further Challenges

If you want to go further, try the following:

- Support decimal numbers
- Support negative numbers
- Support expressions without spaces
- Add error handling
- Support `**` (exponentiation)
- Implement the same logic in another programming language
