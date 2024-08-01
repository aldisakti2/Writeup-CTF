# Yowai Kagi
## Description

20 pts - Cryptography

Author: BosToken

Terinspirasi dari Compfest 15 Hackerclass ;)

## Solution

Step by step:
1. Soal ini pada dasarnya terinspirasi dari soal COMPFEST15 Hackerclass bernama `satu-lagi-nih` yang pada intinya me-recover `d` dengan cara invers nilai `e` dengan `phi` karena nilai `n` didapatkan dari `bilangan prima`.

2. Satu hal yang perlu di notice adalah 'bilangan prima hanya bisa dibagi oleh bilangan itu sendiri dan angka 1'.

3. Hal ini pun yang menyebabkan nilai `n` tidak perlu di faktorisasi lebih lanjut. Langsung dipakai untuk decrypt.

4. Pada script `chall.py` terdapat bagian yang menunjukan bahwa hasil `cp` merupakan bilangan sisa dari `n`.

   ```python
   def enc(source):
       a, b, c = source
       if(pow(c, a) > b):
           cp = pow(c, a, b) <== HERE
           cp = long_to_bytes(cp)
           return [cp, b]
   ```

5. Hal itu bisa terjadi karena bilangan yang di modulus oleh bilangan prima dan nilainya lebih besar darinya maka itu akan menghasilkan angka hasil bagi dan bukan angka `0` maupun `1`.

6. Dengan informasi itu kita bisa me-recover `flag` dengan `pow(cp, d, n)` yang mana `d` merupakan hasil `invers(e, n-1)`

7. Voila flag didapatkan.
