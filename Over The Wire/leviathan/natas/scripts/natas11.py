import base64
import json

# === 1. Pega aquí el cookie original (base64) ===
original_cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="

# === 2. JSON original conocido ===
known_plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'

# Decode base64
cipher = base64.b64decode(original_cookie)

# === 3. Obtener keystream completo ===
keystream = bytes([cipher[i] ^ known_plaintext.encode()[i] for i in range(len(known_plaintext))])

print("[+] Keystream completo:")
print(keystream)

# === 4. Detectar clave mínima repetida ===
def find_repeating_key(stream):
    for key_len in range(1, len(stream)):
        key_candidate = stream[:key_len]
        repeated = (key_candidate * (len(stream) // key_len + 1))[:len(stream)]
        if repeated == stream:
            return key_candidate
    return stream

key = find_repeating_key(keystream)

print("\n[+] Clave detectada:")
print(key)

# === 5. Crear nuevo JSON con showpassword = yes ===
new_plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'

# === 6. Cifrar con XOR ===
new_cipher = bytes([
    new_plaintext.encode()[i] ^ key[i % len(key)]
    for i in range(len(new_plaintext))
])

# === 7. Base64 ===
new_cookie = base64.b64encode(new_cipher).decode()

print("\n[+] Nuevo cookie:")
print(new_cookie)
