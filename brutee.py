def brute_force_attack(password_list,target_password):
    for password in password_list:
        print(f"Trying Password:{password}")
        
        if password == target_password:
            print(f"Password Found:{password}")
            return True
        
    print("Password not found!")
    return False

if __name__ == "__main__":
    password_list = [
        '123456','password','123456789','12345678','qwerty','abc123','monkey','letmein','dragon','1111','baseball'
    ]
    
target_password = input("Enter the Target Password:")
print("Starting Brute force attack....")
result = brute_force_attack(password_list,target_password)

if result:
    print("Brute Force Attack Successful")
else:
    print("Brute Force Attack Failed.")
    
    