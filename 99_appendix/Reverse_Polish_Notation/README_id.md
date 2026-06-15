# Memahami Notasi Polandia Terbalik

Dalam materi ini, kita menggunakan Python untuk memahami **Notasi Polandia Terbalik (RPN)**.

RPN adalah notasi di mana operator ditulis setelah angka.

Ekspresi biasa:

```text
3 + 4
```

Notasi Polandia Terbalik:

```text
3 4 +
```

Ekspresi biasa:

```text
( 3 + 4 ) * 2
```

Notasi Polandia Terbalik:

```text
3 4 + 2 *
```

Dalam materi ini, kita menggunakan list Python sebagai **stack** untuk mempelajari cara mengevaluasi ekspresi RPN dan mengubah ekspresi biasa menjadi RPN.

## Tujuan

Tujuan materi ini bukan sekadar membuat kalkulator.

Tujuannya adalah memahami konsep berikut melalui pemrograman:

- List
- `append()`
- `pop()`
- Percabangan kondisi
- Perulangan
- Fungsi
- Pemrosesan string
- Stack
- Prioritas operator
- Konversi ekspresi

## Apa itu Notasi Polandia Terbalik?

Dalam ekspresi biasa, operator ditulis di antara angka.

```text
3 + 4
```

Cara penulisan ini disebut **notasi infiks**.

Dalam Notasi Polandia Terbalik, operator ditulis setelah angka.

```text
3 4 +
```

Ekspresi ini dibaca sebagai:

> Tambahkan 3 dan 4.

Contoh yang sedikit lebih kompleks:

```text
3 4 + 2 *
```

Ini memiliki arti yang sama dengan:

```text
( 3 + 4 ) * 2
```

Hasilnya adalah `14`.

## Apa itu Stack?

Stack adalah struktur data di mana item yang terakhir dimasukkan adalah yang pertama dikeluarkan.

Dalam bahasa Inggris disebut **Last In, First Out**, disingkat **LIFO**.

Di Python, kita dapat merepresentasikan perilaku stack menggunakan list.

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

`"C"`, item yang terakhir dimasukkan, adalah yang pertama dikeluarkan.

## Step 1: Amati Stack

Pertama, mari kita amati cara kerja stack tanpa melakukan perhitungan.

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

Gunakan `append()` untuk memasukkan nilai dan `pop()` untuk mengambilnya.

## Step 2: Membaca RPN Secara Manual

Perhatikan ekspresi berikut:

```text
3 4 +
```

Cara membacanya adalah sebagai berikut:

| Token | Stack |
|---|---|
| 3 | 3 |
| 4 | 3, 4 |
| + | 7 |

Ketika `+` muncul, ambil dua angka dari stack dan hitung.

```text
3 + 4 = 7
```

Masukkan kembali hasil `7` ke dalam stack.

## Step 3: Mengevaluasi Ekspresi RPN

Mari tulis program untuk menghitung `3 4 +`.

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

## Step 4: Mendukung Empat Operasi Dasar

Tambahkan dukungan untuk `-`, `*`, dan `/` selain `+`.

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

Ekspresi ini memiliki arti yang sama dengan:

```text
( 3 + 4 ) * 2
```

## Step 5: Buat Fungsi

Jadikan logika ini sebagai fungsi agar dapat digunakan kembali.

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

## Step 6: Mengubah Ekspresi Biasa ke RPN

Selanjutnya, ubah ekspresi biasa menjadi RPN.

Ekspresi biasa:

```text
3 + 4 * 2
```

Notasi Polandia Terbalik:

```text
3 4 2 * +
```

Kita menggunakan dua list:

```python
output = []  # Menyimpan ekspresi hasil konversi
stack = []   # Menyimpan operator sementara
```

Operator memiliki prioritas:

```python
priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
```

`*` dan `/` dihitung sebelum `+` dan `-`.

## Step 7: Konversi Tanpa Tanda Kurung

Pertama, ubah ekspresi tanpa tanda kurung.

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

## Step 8: Mendukung Tanda Kurung

Sekarang tambahkan dukungan untuk tanda kurung.

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

## Step 9: Konversi Lalu Hitung

Terakhir, ubah ekspresi biasa ke RPN lalu hitung hasilnya.

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

print("Ekspresi biasa:", normal_expression)
print("RPN:", rpn_expression)
print("Hasil:", answer)
```

Output:

```text
Ekspresi biasa: ( 3 + 4 ) * 2
RPN: 3 4 + 2 *
Hasil: 14
```

## Aturan Input

Dalam materi ini, ekspresi harus ditulis dengan spasi di antara setiap token.

Benar:

```text
3 + 4
3 + 4 * 2
( 3 + 4 ) * 2
```

Salah:

```text
3+4
3+4*2
(3+4)*2
```

Penanganan ekspresi tanpa spasi merupakan tantangan lanjutan.

## Latihan

### Wajib

Tulis fungsi `calc_rpn()` yang mengevaluasi ekspresi RPN.

Pastikan dapat menangani ekspresi berikut:

```text
3 4 +
3 4 + 2 *
10 3 -
10 2 /
```

### Standar

Tulis fungsi `infix_to_rpn()` yang mengubah ekspresi biasa menjadi RPN.

Pastikan dapat menangani ekspresi berikut:

```text
3 + 4
3 + 4 * 2
3 * 4 + 2
```

### Lanjutan

Tambahkan dukungan untuk tanda kurung.

Pastikan dapat menangani ekspresi berikut:

```text
( 3 + 4 ) * 2
3 * ( 4 + 2 )
( 10 - 3 ) * ( 2 + 1 )
```

## Pengumpulan Tugas

Kumpulkan hal-hal berikut:

- Demonstrasi perilaku stack
- Program `calc_rpn()`
- Program `infix_to_rpn()`
- Output menggunakan minimal 3 ekspresi buatan sendiri
- Penjelasan program

## Refleksi

Jelaskan hal-hal berikut dengan kata-kata sendiri:

- Apa itu stack?
- Apa yang dilakukan `append()`?
- Apa yang dilakukan `pop()`?
- Mengapa RPN menggunakan stack?
- Mengapa prioritas operator diperlukan saat mengonversi ke RPN?

## Tantangan Lanjutan

Jika ingin lebih maju, coba hal-hal berikut:

- Dukung bilangan desimal
- Dukung bilangan negatif
- Dukung ekspresi tanpa spasi
- Tambahkan penanganan error
- Dukung `**` (pemangkatan)
- Implementasikan logika yang sama dalam bahasa pemrograman lain
