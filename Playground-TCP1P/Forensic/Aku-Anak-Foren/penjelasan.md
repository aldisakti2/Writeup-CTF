Disini saya mendapatkan sebuah file attachment yang berextensi pcap (Packet Capture) yang dimana ini hasil dari capture jaringan
yang di buka menggunakan wireshark

Saya mencoba analyz melihat protocol hierarchy nya, dan melihat ada sebuah protocol HTTP

lalu saya coba follow untuk protocol HTTP/TCP nya, karna saya sudah penasaran dengan protocol tersebut wkwk

disini saya menyadari ada yang janggal pada header dari request nya

yaitu

![gambar](./image.png)

lalu saya kumpulin informasi tersebut dan ternyata hasil dari informasi tersebut adalah flag nya

TCP1P{networking_forensic_is_always_fun_right_hehe}