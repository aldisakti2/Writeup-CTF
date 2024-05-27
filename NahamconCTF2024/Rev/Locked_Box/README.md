# A Locked Box
## Description
351 points - Reverse Engineering - 174 Solves - medium
Author: @Kkevsterrr#7469

I've got a box, but I think I've misplaced the key.

## Solution
Awalnya saya coba menjalankan `lockedbox` seperti pada challenge sebelumnya (`whats in the box`), namun ternyata terdapat fungsi pencocokan nilai hash pada program yang membuat program ini tidak bisa dijalankan.
![](img/img-1.png)

Lalu saya coba berpikir kalau challenge ini tidak jauh dari challenge sebelumnya berarti ada embedded file di challenge ini. Jadi saya coba cek pakai `binwalk` untuk mengetahui apakah ada file embedded atau tidak.
![](img/img-2.png)

Untuk mendapatkan flag dari challenge ini dengan cara mengekstrak embedded file menggunakan `binwalk` dan flag bisa ditemukan pada baris terakhir salah satu file hasil ekstraksi.
![](img/img-3.png)
![](img/img-4.png)
