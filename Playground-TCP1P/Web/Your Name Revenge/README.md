

1. Kalau kita baca source code, kita bisa tau kalau ada path /report yang akan mengunjungi setiap web tanpa mempedulikan web itu berasal dari lokal ataupun external jaringan server.

2. Kebetulan juga tidak ada proteksi tambahan terkait request keluar (outbound) dari server ke web attacker.

3. Kita bisa memanfaatkan ini untuk CSRF Attack, yang mana kita buat web dimana setiap pengunjungnya nanti akan mentrigger code yang akan membuat si pengunjung melakukan http request ke lokal dan mentrigger code script html xss.

4. Untuk kode nya ada di index.html pada folder solver.

5. Buka akses hosting di sisi attacker.

   cd solver/

   pyton3 -m http.server 8080


   ngrok http 8080

6. Salin url ngrok dan kirim ke server, voila flag didapatkan.

Note: jangan lupa mengganti link webhook.
