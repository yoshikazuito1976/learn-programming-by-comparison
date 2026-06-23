# 06 Fungsi

Di bab ini, Anda akan mempelajari cara merangkum proses ke dalam fungsi.

Jika proses yang mirip ditulis berulang-ulang, program menjadi sulit dibaca.
Dengan fungsi, Anda bisa memberi nama pada proses dan memanggilnya saat diperlukan.

---

## Tujuan Bab Ini

Tujuan bab ini adalah memahami dasar-dasar fungsi.

Saat menulis program, sering kali kita ingin menulis proses yang sama berkali-kali.

Contohnya, menampilkan salam berulang seperti berikut:

```python
print("Hello, ITO!")
print("Hello, Python!")
print("Hello, Programming!")
```

Proses seperti ini bisa dirapikan dengan fungsi.

Dengan fungsi, proses dapat diberi nama lalu dipanggil saat dibutuhkan.

---

## Kata Kunci

- fungsi
- definisi
- pemanggilan
- argumen
- nilai balik
- return
- penggunaan ulang
- pembagian proses

---

## Apa Itu Fungsi?

Fungsi adalah kumpulan proses yang diberi nama.

Di Python, fungsi didefinisikan menggunakan `def`.

```python
def greet():
    print("Hello!")
```

Pada contoh ini, Anda membuat fungsi bernama `greet`.

Namun, hanya mendefinisikan fungsi tidak otomatis menjalankannya.

Untuk menjalankan fungsi, tulis nama fungsi lalu panggil.

```python
greet()
```

---

## Bentuk Dasar Fungsi

Bentuk dasar fungsi Python adalah sebagai berikut.

```python
def nama_fungsi():
    proses
```

Contoh:

```python
def greet():
    print("Hello!")


greet()
```

Hasil eksekusi:

```text
Hello!
```

---

## Memanggil Fungsi

Fungsi dapat dipanggil berkali-kali.

```python
def greet():
    print("Hello!")


greet()
greet()
greet()
```

Hasil eksekusi:

```text
Hello!
Hello!
Hello!
```

Anda tidak perlu menulis proses yang sama berulang kali. Cukup panggil fungsinya.

---

## Apa Itu Argumen?

Argumen adalah nilai yang dikirim ke fungsi.

Pada contoh berikut, `name` adalah argumen.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

Hasil eksekusi:

```text
Hello, ITO!
Hello, Python!
```

Saat menulis `greet("ITO")`, nilai `"ITO"` masuk ke `name`.

Saat menulis `greet("Python")`, nilai `"Python"` masuk ke `name`.

---

## Mengapa Menggunakan Argumen?

Dengan argumen, nilai yang dipakai di dalam fungsi bisa dikirim dari luar.

Dengan begitu, proses serupa dapat dijalankan dengan sedikit perbedaan.

```python
def introduce(name, language):
    print(f"{name} is learning {language}.")


introduce("ITO", "Python")
introduce("Tanaka", "Shell")
```

Hasil eksekusi:

```text
ITO is learning Python.
Tanaka is learning Shell.
```

Pada contoh ini digunakan dua argumen: `name` dan `language`.

---

## Apa Itu Nilai Balik?

Nilai balik adalah nilai yang dikembalikan dari fungsi.

Di Python, gunakan `return` untuk mengembalikan nilai.

```python
def add(a, b):
    return a + b


result = add(3, 5)
print(result)
```

Hasil eksekusi:

```text
8
```

Pada contoh ini, `add(3, 5)` mengembalikan `8`.

Nilai tersebut disimpan ke variabel `result`.

---

## Perbedaan print dan return

`print` digunakan untuk menampilkan ke layar.

`return` digunakan untuk mengembalikan hasil fungsi.

Perhatikan contoh berikut.

```python
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


add_print(3, 5)

result = add_return(3, 5)
print(result)
```

`print` menampilkan nilai.

`return` mengembalikan nilai.

Nilai yang dikembalikan bisa disimpan di variabel atau dipakai untuk perhitungan lain.

---

## Menggunakan Nilai Balik dalam Perhitungan

Nilai balik dapat dipakai lagi pada proses berikutnya.

```python
def add(a, b):
    return a + b


result = add(3, 5)
double_result = result * 2

print(result)
print(double_result)
```

Hasil eksekusi:

```text
8
16
```

Dengan menyimpan hasil fungsi ke variabel, hasilnya lebih mudah dipakai selanjutnya.

---

## Percabangan dan Fungsi

Percabangan juga bisa digunakan di dalam fungsi.

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


result = judge(75)
print(result)
```

Hasil eksekusi:

```text
Lulus
```

Jika `score` 60 atau lebih, fungsi mengembalikan `"Lulus"`.

Jika tidak, fungsi mengembalikan `"Tidak Lulus"`.

---

## Input dan Fungsi

`input` juga bisa digabungkan dengan fungsi.

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


score = int(input("Masukkan nilai: "))
result = judge(score)
print(result)
```

Contoh eksekusi:

```text
Masukkan nilai: 80
Lulus
```

Nilai yang dimasukkan dipakai oleh fungsi untuk menentukan hasil.

---

## Perulangan dan Fungsi

Fungsi juga bisa digabungkan dengan perulangan.

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

Hasil eksekusi:

```text
92: Lulus
85: Lulus
74: Lulus
66: Lulus
39: Tidak Lulus
```

Setiap nilai pada daftar diambil satu per satu lalu dinilai oleh fungsi.

---

## Kode Sebelum Dijadikan Fungsi

Kode berikut menilai skor.

```python
score = 75

if score >= 60:
    result = "Lulus"
else:
    result = "Tidak Lulus"

print(result)
```

Kode ini tetap berjalan.

Namun, jika penilaian skor dilakukan berkali-kali, proses serupa akan terus berulang.

---

## Kode Setelah Dijadikan Fungsi

Jika proses yang sama diringkas menjadi fungsi, hasilnya seperti ini.

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


result = judge(75)
print(result)
```

Dengan fungsi, proses penilaian skor bisa diberi nama `judge`.

---

## Kelebihan Memfungsikan Kode

Mengubah proses menjadi fungsi memberi beberapa kelebihan.

- Tidak perlu menulis proses yang sama berulang kali
- Program menjadi lebih mudah dibaca
- Lokasi yang perlu diubah lebih sedikit
- Proses bisa diberi nama
- Program bisa dipikirkan per bagian

Semakin panjang program, semakin penting merapikannya dengan fungsi.

---

## Cara Memberi Nama Fungsi

Nama fungsi sebaiknya menunjukkan apa yang dilakukan fungsi tersebut.

Contoh yang baik:

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"
```

```python
def add(a, b):
    return a + b
```

Contoh yang kurang baik:

```python
def x(a):
    return a + 10
```

```python
def test(data):
    print(data)
```

Nama yang terlalu pendek atau terlalu umum akan sulit dibaca nantinya.

---

## Hal yang Perlu Diperhatikan Saat Menulis Fungsi

Saat menulis fungsi, perhatikan indentasi.

Di Python, proses di dalam fungsi harus ditulis dengan indentasi.

```python
def greet():
    print("Hello!")
```

Jika tidak diindentasi seperti di bawah ini, akan terjadi error.

```python
def greet():
print("Hello!")
```

Dalam Python, indentasi sangat penting.

---

## Latihan 1: Fungsi Salam

Buat fungsi dengan syarat berikut.

- Nama fungsi: `greet`
- Argumen: `name`
- Menampilkan `Hello, nama!`

Contoh:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("ITO")
greet("Python")
```

---

## Latihan 2: Fungsi Penjumlahan

Buat fungsi dengan syarat berikut.

- Nama fungsi: `add`
- Argumen: `a` dan `b`
- Mengembalikan hasil `a + b`

Contoh:

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

---

## Latihan 3: Fungsi Penilaian Skor

Buat fungsi dengan syarat berikut.

- Nama fungsi: `judge`
- Argumen: `score`
- Jika skor 60 atau lebih, kembalikan `"Lulus"`
- Jika skor kurang dari 60, kembalikan `"Tidak Lulus"`

Contoh:

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


print(judge(80))
print(judge(45))
```

---

## Latihan 4: Daftar dan Fungsi

Berikut daftar skor.

```python
scores = [92, 85, 74, 66, 39]
```

Gunakan fungsi `judge` untuk menilai setiap skor.

Contoh:

```python
def judge(score):
    if score >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


scores = [92, 85, 74, 66, 39]

for score in scores:
    result = judge(score)
    print(f"{score}: {result}")
```

---

## Latihan 5: Fungsi Penentuan Peringkat

Buat fungsi yang mengembalikan peringkat berdasarkan skor.

- 90 ke atas: A
- 80 ke atas: B
- 70 ke atas: C
- 60 ke atas: D
- Di bawah 60: F

Contoh:

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

Hasil eksekusi:

```text
92: A
85: B
74: C
66: D
39: F
```

---

## Ringkasan Bab

Di bab ini, Anda mempelajari fungsi.

Fungsi adalah mekanisme untuk memberi nama dan merangkum proses.

Dengan fungsi, Anda tidak perlu menulis proses yang sama berulang-ulang.

Selain itu, program bisa disusun agar lebih rapi dan mudah dibaca.

---

## Poin Penting

- Fungsi didefinisikan dengan `def`
- Fungsi tidak dijalankan jika tidak dipanggil
- Argumen memungkinkan pengiriman nilai ke fungsi
- `return` memungkinkan fungsi mengembalikan nilai
- Fungsi membantu merapikan struktur program

---

## Apa yang Dipelajari Berikutnya

Setelah bisa menggunakan fungsi, Anda dapat memikirkan program sebagai gabungan komponen.

Berikutnya, Anda akan lanjut ke topik untuk menulis program yang lebih panjang, seperti input/output file dan penanganan error.
