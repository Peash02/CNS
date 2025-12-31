import hashlib

def get_hash(txt):
    sha_signature = hashlib.sha256(txt.encode()).hexdigest()
    return sha_signature

txt = input()
print(f"Text:{txt}")
print(f"SHA-256 Hash: {get_hash(txt)}")