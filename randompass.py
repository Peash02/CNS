import secrets
import string

def gen_pass(length : int) -> str :
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for i in range(length))
    return password

password_length = 12
password =  gen_pass(password_length)
print(f"Generated password : {password}")