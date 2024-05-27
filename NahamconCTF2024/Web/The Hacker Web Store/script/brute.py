from werkzeug.security import check_password_hash

# Hash target yang ingin di-crack
target_hash = "pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57"

# Baca wordlist dari file pass.txt dengan encoding UTF-8
with open('password.txt', 'r', encoding='utf-8') as file:
    passwords = file.readlines()

# Bersihkan newline characters dari setiap password
passwords = [password.strip() for password in passwords]

# Mulai brute force
for password in passwords:
    a = check_password_hash(target_hash, password)
    print(a,password)
    if check_password_hash(target_hash, password):
        print(f"Password ditemukan: {password}")
        break
else:
   
    print("Password tidak ditemukan dalam wordlist.")
