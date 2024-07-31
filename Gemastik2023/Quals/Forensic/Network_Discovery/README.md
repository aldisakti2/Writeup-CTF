# Digital Forensics- Network Discovery

Our network was repeatedly bombarded by a port scanner targeting a specific ports. Interestingly, our server seems to provide different responses depending on its current state and the specific request it receives. Although nothing major happened, we believe there was a hidden intention behind the attacks.

* Hint : We discovered that the actor was attempting to determine whether our service was open, closed, or blocked by the firewall.
* File [log.tar.xz](https://github.com/aceptriana/CTF-Gemastik2023/raw/main/Digital%20Forensics/log.tar.xz)

## Solution

1. Ada 3 tipe connection di capture ini (open, closed, dan block)

2. Untuk `open` itu patokannya ada SYN-ACK dan closed itu ada RST-ACK paket data

3. Kalau `block` itu hanya ada TCP Retransmission yang bener - bener tidak berkaitan sama port request di paket data lain.

   misal:

   paket 1 => TCP Retransmission ke port 8080
   
   paket 2 => TCP Port number reused dari port 8080

   nah kl contoh diatas itu contoh untuk TCP Retransmission yang salah untuk blocked

   sementara yang benernya itu cuman ada paket 1 saja dan paket 2 itu ngg berkaitan sama sekali (srcport) dengan dstport si paket 1.

4. Untuk script yang digunakan me-recover data dari `open connection` ada di script pertama, `closed connection` di script kedua, dan `block connection` di script ketiga


