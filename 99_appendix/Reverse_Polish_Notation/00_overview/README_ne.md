# रिभर्स पोलिश नोटेशन बुझ्ने

यस शैक्षिक सामग्रीमा, हामी Python प्रयोग गरेर **रिभर्स पोलिश नोटेशन (RPN)** बुझ्नेछौं।

RPN एउटा त्यस्तो नोटेशन हो जसमा अपरेटरहरू संख्याहरूको पछि लेखिन्छन्।

सामान्य अभिव्यक्ति:

```text
3 + 4
```

रिभर्स पोलिश नोटेशन:

```text
3 4 +
```

सामान्य अभिव्यक्ति:

```text
( 3 + 4 ) * 2
```

रिभर्स पोलिश नोटेशन:

```text
3 4 + 2 *
```

यस सामग्रीमा, हामी Python को list लाई **स्ट्याक** को रूपमा प्रयोग गर्दै RPN अभिव्यक्ति गणना गर्न र सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गर्न सिक्नेछौं।

## उद्देश्य

यस सामग्रीको उद्देश्य केवल क्याल्कुलेटर बनाउनु मात्र होइन।

प्रोग्रामिङ मार्फत निम्न अवधारणाहरू बुझ्नु यसको लक्ष्य हो:

- List
- `append()`
- `pop()`
- सर्त शाखा (Conditional branching)
- पुनरावृत्ति (Loop)
- फंक्शन
- स्ट्रिङ प्रशोधन
- स्ट्याक
- अपरेटर प्राथमिकता
- अभिव्यक्ति रूपान्तरण

## रिभर्स पोलिश नोटेशन भनेको के हो?

सामान्य अभिव्यक्तिमा, अपरेटरहरू संख्याहरूको बीचमा लेखिन्छन्।

```text
3 + 4
```

यस प्रकारको लेखाइलाई **इन्फिक्स नोटेशन** भनिन्छ।

रिभर्स पोलिश नोटेशनमा, अपरेटरहरू संख्याहरूको पछि लेखिन्छन्।

```text
3 4 +
```

यो अभिव्यक्तिको अर्थ हो:

> ३ र ४ जोड्नु।

अलि जटिल उदाहरण:

```text
3 4 + 2 *
```

यसको अर्थ निम्नसँग समान छ:

```text
( 3 + 4 ) * 2
```

परिणाम `14` हो।

## स्ट्याक भनेको के हो?

स्ट्याक एउटा डेटा संरचना हो जसमा पछि राखिएको वस्तु पहिले निकालिन्छ।

अङ्ग्रेजीमा यसलाई **Last In, First Out** भनिन्छ, संक्षेपमा **LIFO**।

Python मा, हामी list प्रयोग गरेर स्ट्याकको व्यवहार देखाउन सक्छौं।

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

आउटपुट:

```text
['A', 'B', 'C']
C
['A', 'B']
```

सबैभन्दा पछि राखिएको `"C"` सबैभन्दा पहिले निकालिन्छ।

## Step 1: स्ट्याकको व्यवहार हेर्ने

पहिले, कुनै गणना नगरी स्ट्याकको काम गर्ने तरिका हेरौं।

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

आउटपुट:

```text
[3, 4]
4
3
[]
```

मान राख्न `append()` र निकाल्न `pop()` प्रयोग गर्नुहोस्।

## Step 2: हातले RPN पढ्ने

निम्न अभिव्यक्ति विचार गर्नुहोस्:

```text
3 4 +
```

पढ्ने तरिका यस प्रकार छ:

| टोकन | स्ट्याक |
|---|---|
| 3 | 3 |
| 4 | 3, 4 |
| + | 7 |

`+` देखिएमा, स्ट्याकबाट दुईवटा संख्या निकाली गणना गर्नुहोस्।

```text
3 + 4 = 7
```

परिणाम `7` लाई फेरि स्ट्याकमा राख्नुहोस्।

## Step 3: RPN अभिव्यक्ति गणना गर्ने

`3 4 +` गणना गर्ने प्रोग्राम लेखौं।

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

आउटपुट:

```text
7
```

## Step 4: चारवटा गणितीय क्रियाहरू समर्थन गर्ने

`+` मात्र होइन, `-`, `*`, र `/` पनि समर्थन गर्नुहोस्।

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

आउटपुट:

```text
14
```

यो अभिव्यक्ति निम्न सामान्य अभिव्यक्तिसँग समान छ:

```text
( 3 + 4 ) * 2
```

## Step 5: फंक्शन बनाउने

एउटै तर्कलाई बारम्बार प्रयोग गर्न सकिने गरी फंक्शनमा रूपान्तरण गर्नुहोस्।

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

आउटपुट:

```text
7
14
7
```

## Step 6: सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गर्ने

अब सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गरौं।

सामान्य अभिव्यक्ति:

```text
3 + 4 * 2
```

रिभर्स पोलिश नोटेशन:

```text
3 4 2 * +
```

हामी दुईवटा list प्रयोग गर्छौं:

```python
output = []  # रूपान्तरित अभिव्यक्ति राख्ने
stack = []   # अपरेटर अस्थायी रूपमा राख्ने
```

अपरेटरहरूको प्राथमिकता हुन्छ:

```python
priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
```

`*` र `/` लाई `+` र `-` भन्दा पहिले गणना गरिन्छ।

## Step 7: कोष्ठक बिनाको रूपान्तरण

पहिले, कोष्ठक नभएका अभिव्यक्तिहरू रूपान्तरण गरौं।

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

आउटपुट:

```text
3 4 +
3 4 2 * +
3 4 * 2 +
```

## Step 8: कोष्ठक समर्थन गर्ने

अब कोष्ठक भएका अभिव्यक्तिहरूको लागि समर्थन थप्नुहोस्।

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

आउटपुट:

```text
3 4 + 2 *
3 4 2 + *
```

## Step 9: रूपान्तरण गरेर गणना गर्ने

अन्तमा, सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गरेर गणना गरौं।

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

print("सामान्य अभिव्यक्ति:", normal_expression)
print("RPN:", rpn_expression)
print("परिणाम:", answer)
```

आउटपुट:

```text
सामान्य अभिव्यक्ति: ( 3 + 4 ) * 2
RPN: 3 4 + 2 *
परिणाम: 14
```

## इनपुट नियमहरू

यस सामग्रीमा, अभिव्यक्तिहरू प्रत्येक टोकनको बीचमा खाली ठाउँ राखेर लेख्नु पर्छ।

सही:

```text
3 + 4
3 + 4 * 2
( 3 + 4 ) * 2
```

गलत:

```text
3+4
3+4*2
(3+4)*2
```

खाली ठाउँ नभएका अभिव्यक्तिहरूको प्रशोधन उन्नत अभ्यासको रूपमा छोडिएको छ।

## अभ्यासहरू

### अनिवार्य

`calc_rpn()` फंक्शन लेख्नुहोस् जसले RPN अभिव्यक्ति गणना गर्छ।

निम्न अभिव्यक्तिहरू गणना गर्न सक्ने बनाउनुहोस्:

```text
3 4 +
3 4 + 2 *
10 3 -
10 2 /
```

### मानक

`infix_to_rpn()` फंक्शन लेख्नुहोस् जसले सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गर्छ।

निम्न अभिव्यक्तिहरू रूपान्तरण गर्न सक्ने बनाउनुहोस्:

```text
3 + 4
3 + 4 * 2
3 * 4 + 2
```

### उन्नत

कोष्ठक भएका अभिव्यक्तिहरूको लागि पनि समर्थन थप्नुहोस्।

निम्न अभिव्यक्तिहरू रूपान्तरण गर्न सक्ने बनाउनुहोस्:

```text
( 3 + 4 ) * 2
3 * ( 4 + 2 )
( 10 - 3 ) * ( 2 + 1 )
```

## पेश गर्ने सामग्री

निम्न सामग्रीहरू पेश गर्नुहोस्:

- स्ट्याकको व्यवहार प्रदर्शन
- `calc_rpn()` प्रोग्राम
- `infix_to_rpn()` प्रोग्राम
- आफैंले बनाएका कम्तीमा ३ वटा अभिव्यक्तिहरूको आउटपुट
- प्रोग्रामको व्याख्या

## समीक्षा

निम्न विषयहरू आफ्नै शब्दमा व्याख्या गर्नुहोस्:

- स्ट्याक भनेको के हो?
- `append()` ले के गर्छ?
- `pop()` ले के गर्छ?
- RPN मा स्ट्याक किन प्रयोग गरिन्छ?
- सामान्य अभिव्यक्तिलाई RPN मा रूपान्तरण गर्दा अपरेटर प्राथमिकता किन आवश्यक छ?

## उन्नत चुनौतीहरू

थप अगाडि जान चाहनेहरूका लागि:

- दशमलव संख्या समर्थन गर्नुहोस्
- ऋणात्मक संख्या समर्थन गर्नुहोस्
- खाली ठाउँ नभएका अभिव्यक्तिहरू समर्थन गर्नुहोस्
- त्रुटि प्रशोधन थप्नुहोस्
- `**` (घातांक) समर्थन गर्नुहोस्
- अर्को प्रोग्रामिङ भाषामा पनि उही तर्क लागू गर्नुहोस्
