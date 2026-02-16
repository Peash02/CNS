from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad

def encrypt_AES(key,txt):
    cipher = AES.new(key,AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(txt.encode(),AES.block_size))
    return ciphertext,cipher.iv

def decrypt_AES(key,ciphertxt,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv = iv)
    txt = unpad(cipher.decrypt(ciphertxt),AES.block_size)
    return txt.decode()

key = get_random_bytes(16)

txt = "Hello,World!"
ciphertxt,iv = encrypt_AES(key,txt)
decrypted_txt = decrypt_AES(key,ciphertxt,iv)

print("Plaintext:",txt)
print("Ciphertext:",ciphertxt)
print("Decrypted Text:",decrypted_txt)


