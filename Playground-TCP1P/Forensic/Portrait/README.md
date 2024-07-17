# Portrait
## Description
703 points - Forensic
Author: nagi

A man had typed a bunch of characters to create a peculiar portrait. Legend said that this portrait may hide a secret beneath it. Can you unveil the secret of the portrait?

## Solution

1. Jika kita lihat isi dari file pcapng maka kita dapat tau kalau data yang ter capture adalah data - data bluetooth yang bisa ditandai dengan adanya protocol "btl2cap".

2. Lalu ketika kita coba check payload data dari paket data pcapng didapati susunan seperti "a1:01:00:00:19:00:00:00:00:00".

3. Menurut informasi dari "https://github.com/benizi/hidclient/blob/master/hidclient.c", diperoleh informasi untuk 2 bytes pertama mengindikasikan sebagai mouse atau keyboard. Lalu untuk bytes ke 3 adalah bytes yang munjukan apakah menggunakan tombol SHIFT atau tidak.

4. Bila bytes ke-3 berupa "20" atau "02" maka itu artinya sedang menggunakan tombol SHIFT.

5. Bytes data sisanya adalah keycode. Di pcapng tidak menunjukan tipe dari bluetooth devicenya, tapi kita bisa menganalisisnya dari data keycode yang tersedia.

6. Diketahui hanya bytes ke-5 saja yang ada data keycode nya hal ini menandakan kalau devicenya adalah keyboard. Hal ini karena, bila mouse harus ada setidaknya 3 bytes data keycode sementara keyboard itu hanya perlu mengisi bytes data sisa saja untuk keycodenya (untuk panjangnya tidak tentu).

7. Lalu untuk berikutnya dapat menggunakan script "parsing.py" untuk restore text yang dikirimkan lewat bluetooth device nya.

8. Setelah itu kita bisa tau kalau aktifitas yang dilakukan adalah menggenerate kode QR.

9. Agar kita dapat memperoleh kode QR berdasarkan hasil dari "parsing.py" kita dapat menggunakan script "automate.py"
