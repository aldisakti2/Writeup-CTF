# Digital Forensics - GreyHat
* A DFIR enjoyer who love analyze dump memory ask your help for analyze sus file. He says "Aku menemukan ini dari hasil dump memory client ku, client-ku berkata bahwa file dia pada direktori tertentu tiba-tiba menghilang, dan ia terakhir kali menjalankan sebuah executables, dan mungkin ini penyebabnya. Aku mengambil beberapa file yang sus dan sepertinya ini kunci untuk menemukan penyebab hilangnya file-file tersebut. Bisa kah kau menolong ku?"

* Notes : **Jangan di run exe-nya ya, kecuali di sandbox yang emang buat coba-coba**

* Hint :
  - Decompile the exe first maybe? Using some famous decompiler? but you must know, with what the exe was made
  - Parsing PCAP file is fun! maybe you must know how to parse it correctly based on source code from decompiled EXE
  - Maybe you must 'carefully' read the source code from the exe
* File [help.zip](https://github.com/aceptriana/CTF-Gemastik2023/raw/main/Digital%20Forensics/help.zip)

**Proof of Concept**
1. given a zip contain PCAP and EXE
2. analyze the EXE, using strings we can see its a Python-based
3. decompile using pyinstractor, it will give a malware.pyc
4. decompile the pyc using uncompyle6 and pycdc or you can use this <a href="https://www.toolnb.com/tools-lang-en/pyc.html">web</a>, combine the result for more understanding
5. from that we know the EXE encrypt data from Downloads dir to desktop,ini
6. the encryption is only using XOR using value based by time and index encryption file
7. parsing PCAP file using scapy
8. unzip all file (FLAG stored in file [164906.jpg])

   ![](writeup/res/164906.jpg)
