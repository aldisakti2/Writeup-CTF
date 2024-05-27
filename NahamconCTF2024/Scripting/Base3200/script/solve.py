import base64

def decode_base32(file_path, iterations=50):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    for i in range(iterations):
        data = base64.b64decode(data)
    print(data)
    

# Ganti 'encoded_file_path' dengan path ke file yang ingin kamu dekode
decode_base32('theflag')
