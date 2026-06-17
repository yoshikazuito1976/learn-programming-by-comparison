# Dasar-Dasar Regular Expression

## Apa Itu Regular Expression?

Regular expression adalah cara untuk menyatakan pola pada teks.

Di Linux, regular expression terutama digunakan dengan perintah seperti `grep`.

Sebagai contoh, perintah berikut mencari baris yang mengandung `a` di dalam `students.txt`.

```bash
grep 'a' students.txt
```

## File Contoh

Pertama, buat file untuk latihan.

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

## Dasar `grep`

### Menampilkan baris yang mengandung `a`

```bash
grep 'a' students.txt
```

Contoh hasil:

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

`AI` menggunakan huruf besar, jadi tidak ditampilkan oleh `grep 'a'`.

## Regular Expression yang Sering Dipakai

| Bentuk | Arti | Contoh |
|---|---|---|
| `a` | mengandung `a` | `grep 'a' students.txt` |
| `^s` | diawali dengan `s` | `grep '^s' students.txt` |
| `o$` | diakhiri dengan `o` | `grep 'o$' students.txt` |
| `.` | sembarang 1 karakter | `grep 'a.o' students.txt` |
| `[abc]` | salah satu dari `a`, `b`, atau `c` | `grep '[abc]' students.txt` |
| `[0-9]` | 1 digit angka | `grep '[0-9]' students.txt` |
| `[a-z]` | 1 huruf kecil | `grep '[a-z]' students.txt` |
| `[A-Z]` | 1 huruf besar | `grep '[A-Z]' students.txt` |
| `[^0-9]` | 1 karakter selain angka | `grep '[^0-9]' students.txt` |
| `*` | karakter sebelumnya muncul 0 kali atau lebih | `grep 'a*' students.txt` |
| `+` | karakter sebelumnya muncul 1 kali atau lebih | `grep -E 'a+' students.txt` |
| `?` | karakter sebelumnya muncul 0 kali atau 1 kali | `grep -E 'a?' students.txt` |
| `a\|b` | `a` atau `b` | `grep -E 'a|b' students.txt` |

## Perbedaan `grep` dan `grep -E`

Pada `grep` biasa, simbol seperti `+`, `?`, dan `|` tidak senyaman itu untuk dipakai langsung, jadi menambahkan `-E` membuat penulisan regular expression yang diperluas menjadi lebih mudah.

```bash
grep -E 'student[0-9]+' students.txt
```

Perintah ini mencari baris dengan `student` yang diikuti satu atau lebih angka.

## Contoh Dasar

### Baris yang diawali `s`

```bash
grep '^s' students.txt
```

### Baris yang diakhiri `o`

```bash
grep 'o$' students.txt
```

### Baris yang mengandung angka

```bash
grep '[0-9]' students.txt
```

### Baris dengan `student` yang diikuti angka

```bash
grep -E '^student[0-9]+$' students.txt
```

### Baris yang hanya berisi huruf kecil

```bash
grep -E '^[a-z]+$' students.txt
```

### Baris yang hanya berisi huruf besar

```bash
grep -E '^[A-Z]+$' students.txt
```

### Baris yang mengandung `_` atau `-`

```bash
grep -E '[_-]' students.txt
```

### Menampilkan hanya baris 4 karakter

```bash
grep -E '^....$' students.txt
```

`.` berarti sembarang 1 karakter.

Jadi `^....$` berarti "tepat 4 karakter dari awal sampai akhir".

### Tidak membedakan huruf besar dan kecil

```bash
grep -i 'ai' students.txt
```

Dalam kasus ini, `AI` dan `ai` keduanya ditampilkan.

### Menampilkan baris yang tidak mengandung `user`

```bash
grep -v 'user' students.txt
```

`-v` adalah opsi untuk menampilkan baris yang tidak cocok dengan kondisi.

## Catatan

Dalam regular expression, beberapa simbol memiliki arti khusus.

Sebagai contoh, `.` di sini bukan titik biasa. Simbol ini berarti "sembarang 1 karakter".

Jika Anda ingin mencari titik yang sebenarnya, tulislah `\.`.

```bash
grep '\.' file.txt
```

## Hal Pertama yang Perlu Diingat

Pada awalnya, cukup ingat lima hal berikut ini.

| Bentuk | Arti |
|---|---|
| `^` | awal baris |
| `$` | akhir baris |
| `.` | sembarang 1 karakter |
| `[0-9]` | angka |
| `[a-z]` | huruf kecil |

## Soal Latihan

Gunakan `grep` untuk menampilkan baris yang sesuai dengan kondisi berikut.

1. Baris yang mengandung `a`
2. Baris yang diawali `s`
3. Baris yang diakhiri `o`
4. Baris yang mengandung angka
5. Baris yang dimulai dengan `student` lalu diikuti angka
6. Baris yang hanya berisi huruf kecil
7. Baris yang hanya berisi huruf besar
8. Baris yang mengandung `_` atau `-`
9. Baris dengan 4 karakter
10. Baris yang mengandung `ai`, tanpa membedakan huruf besar dan kecil
11. Baris yang tidak mengandung `user`
12. Baris dengan `python` yang diikuti angka

## Contoh Jawaban

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

## Melihat `man`

Anda bisa memeriksa detail lebih lanjut dengan perintah berikut.

```bash
man grep
```

Tidak masalah jika Anda belum memahami semua bahasa Inggrisnya.

Belajarlah sedikit demi sedikit, dan tambahkan jumlah kata serta simbol yang Anda kenali.

## Ringkasan

Regular expression bukan sesuatu yang harus dihafal sekaligus.

Gunakan sedikit demi sedikit saat Anda membutuhkannya.

Mulailah dengan mencari string menggunakan `grep`.
