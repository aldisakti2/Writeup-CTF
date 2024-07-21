# Unattached
## Description
504 points - Forensic
Author: nagi

Out of boredom, I accidentally dumped all of my files into this plain-looking PDF. I wonder if I can get them back.

## Solution

1. extract pdf dengan pdfextract
2. lihat pada attachments ada beberapa file yang mencirikan file2 git repo (git index, description, config, HEAD, dan file refs)
3. buat dan pindahkan file itu ke folder .git (untuk refs letak path disesuaikan dengan info di HEAD)
4. lengkapi file maupun folder git yang kurang seperti folder `objects` beserta isinya yaitu folder `info` dan `packs`
5. extract zlib dari attachments pakai extract.sh (pastikan letak extract.sh ada di folder yang sama dengan file2 attachments dan nama file hasil ekstraksi sama juga seperti file - file di attachments)
6. generate hash sha1 dari hasil extract zlib
7. gunakan 2 huruf pertama sebagai nama folder git objects dan sisanya sebagai nama file objek nya.

Contoh:

file attached_attachment283 punya hash sha1
ad18aec1a7aaf65486ee26aa2ad500095d8b7adc

`ad` => nama folder

`18aec1a7aaf65486ee26aa2ad500095d8b7adc` => nama file

jadikan itu untuk format nama file itu di dalam folder objects pada git

`.git/objects/ad/18aec1a7aaf65486ee26aa2ad500095d8b7adc`

8. copy file asli dari attachments ke folder sesuai dengan hasil hash file ekstraksinya.

Contoh:

file attached_attachment283 itu ada dua:
- satu yang ada di attachments
- satu lagi yang hasil ke ekstrak nya (kebetulan ini namanya di setting sama juga namanya)

kita gunakan file hasil ekstrak untuk dapet format nama folder dan file dari hasil sha1sum nya
dan file asli dari attachments merupakan file yang nantinya bakal diubah nama dan letak foldernya mengikuti
format nama file dan folder path yang udah didapetin dari hasil file ekstrak

`cp attachments/attached_attachment283 .git/objects/ad/18aec1a7aaf65486ee26aa2ad500095d8b7adc`

note: ini gunakan script generate.sh

9. kalau sudah, tinggal jalankan `git show --full-diff` untuk melihat perbedaan di setiap commit nya
10. gunakan script get_flag.sh untuk mendapatkan flag nya.


#Voila flag berhasil didapatkan. <br/>
#![](img/img-1.png)

