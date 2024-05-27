# Uriel
## Description
50 points - Warmups - 2193 Solves - easy
Author: @JohnHammond

Uriel was browsing the web and he saw this big long blob of text in his address bar! He was telling me about it but I don't remember everything he said... I think he mentioned something like "it happened twice?"

%25%36%36%25%36%63%25%36%31%25%36%37%25%37%62%25%33%38%25%36%35%25%36%36%25%36%35%25%36%32%25%33%36%25%33%36%25%36%31%25%33%37%25%33%31%25%33%39%25%36%32%25%33%37%25%33%35%25%36%31%25%33%34%25%36%32%25%33%37%25%36%33%25%33%36%25%33%33%25%33%34%25%36%34%25%33%38%25%33%38%25%33%35%25%33%37%25%33%38%25%33%38%25%36%34%25%36%36%25%36%33%25%37%64

## Solution
![Screenshot 2024-05-26 195614](https://github.com/aldisakti2/Writeup/assets/106227122/7229e913-a0b5-489a-b9a0-3a2fc3d37b92)


**Terlihat aneh namun kode diatas merupakan kode URL Encode, hal yang menarik disini %25 merupakan representasi dari _%_ sehingga bisa dihapus**


URL encode :
%25%36%36%25%36%63%25%36%31%25%36%37%25%37%62%25%33%38%25%36%35%25%36%36%25%36%35%25%36%32%25%33%36%25%33%36%25%36%31%25%33%37%25%33%31%25%33%39%25%36%32%25%33%37%25%33%35%25%36%31%25%33%34%25%36%32%25%33%37%25%36%33%25%33%36%25%33%33%25%33%34%25%36%34%25%33%38%25%33%38%25%33%35%25%33%37%25%33%38%25%33%38%25%36%34%25%36%36%25%36%33%25%37%64

**Didapat kode hex sebagai berikut** :

 66 6c 61 67 7b 38 65 66 65 62 36 36 61 37 31 39 62 37 35 61 34 62 37 63 36 33 34 64 38 38 35 37 38 38 64 66 63 7d

 **Decode hex**:
 
 ![Screenshot 2024-05-26 200259](https://github.com/aldisakti2/Writeup/assets/106227122/718972af-1417-4a41-8496-d381de7d8641)

 
 
 Flag : flag{8efeb66a719b75a4b7c634d885788dfc}
 
