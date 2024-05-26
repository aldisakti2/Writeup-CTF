**INDEX**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/b512e58b-c916-4a86-80f0-368a0fab98f9)

http://<host>:<port>/code


![image](https://github.com/aldisakti2/Writeup/assets/106227122/7739a19b-b6fa-4697-8297-e36415f2aaf3)


**Hmmm menarik, disini kita diizinkan untuk menggunakan request PROPFIND (https://stackoverflow.com/questions/71142211/what-is-propfind-request) sehingga kita dapat tahu apa yang ada didalam folder tertentu, ini cukup membantu untuk menemukan flag**
![image](https://github.com/aldisakti2/Writeup/assets/106227122/7495b2d7-7b64-4154-8a18-279bc6606953)

**Disini kita bisa mengakses app.py.backup melalui /static/app.py.backup**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/30862538-9cb5-4e3e-af55-9819800f70a5)


**Setelah didownload app.py.backup saya menemukan hal menarik, dimana kita diizinkan untuk merequest menggunakan MOVE dengan menambahkan header _Destination_**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/cf26e0c3-4820-4c26-90c5-5f1bb74d2cdb)

**EXPLOIT**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/e4dfe3f8-9444-4541-a002-e2cc93398d93)

**FLAG**

![image](https://github.com/aldisakti2/Writeup/assets/106227122/7b60f5bb-a3e8-4c08-9370-e8d391f8abaf)

flag : flag{2bc76964262b3a1bbd5bc610c6918438}
