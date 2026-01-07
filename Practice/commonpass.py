def is_pass_common(password : str,common_passwords: list) -> bool:
    return password in common_passwords

common_passwords = ['12345678','password','123456','0987654321','qwerty','asdfg','abc123']

pas = 'password'
if is_pass_common(pas,common_passwords):
    print("Password is too common")
else:
    print("Password is not in the common list.")

