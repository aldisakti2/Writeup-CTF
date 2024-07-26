# Pemanasan
## Description
703 points - Forensic
Author: fire

I just create handmade pdf. Well i also made flag checker inside pdf file. Cool right? ���

## Solution

Step by step:
1. Cek kalau file memang benar - benar terproteksi
   ```bash
   pdfid -e <nama_file>
   ```
   Jika muncul ```/Encrypt 1```` itu artinya file terproteksi.

2. Untuk mengetahui panjang dari password proteksinya gunakan perintah ini

   ```bash
   pdfparser -s /Encrypt <nama_file>
   ```
   Nanti informasi panjang passwordnya ada di bagian (Size ...)

3. Brute force dengan pdfcrack dan pakai ketentuan minimal panjang password tadi

   ```bash
   pdfcrack --wordlist=/usr/share/wordlists/rockyou.txt --minpw=11 flag_protected.pdf
   ```

4. Di soal ada informasi kalau soal ini juga ada flag checker program juga dan ini dirasa akan menampilkan flag asli, karena jika hanya buka file pdf nya saja itu tidak menampilkan Flag yang valid.

5. Extract pdf dengan pdfextract dan masukan password hasil brute force tadi
   ```bash
   pdfextract <nama_file>
   ```
6. Jika sudah, kita tinggal eksplorasi file saja hingga menemukan file script FuckJS

7. Kita decompile lalu minta bantuan AI untuk membuatnya mudah dibaca. Selesai.
