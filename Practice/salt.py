import os 
import hashlib

def hash_pass(pwd):
    
    salt = os.urandom(16) #Generate random salt of 16 bytes
    salted_pwd = pwd.encode() + salt
    hash_value = hashlib.sha256(salted_pwd).hexdigest()
    return salt,hash_value

def verify_pwd(input_pwd,stored_salt,stored_hash):
    
    salted_input = input_pwd.encode() + stored_salt
    new_hash = hashlib.sha256(salted_input).hexdigest()
    return new_hash == stored_hash

if __name__ == "__main__":
    pwd = input("Enter Password:")
    
    salt,hashed = hash_pass(pwd)
    
    print("\nStored Salt:",salt)
    print("Stored Hash :",hashed)
    
    print("\nLogin Verification:-")
    login_pass = input("Re-enter Password:")
    
    if verify_pwd(login_pass,salt,hashed):
        print("Password Verified.")
    else:
        print("Wrong Password")
