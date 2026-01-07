import itertools
import string
import time

def brute_force(target_pass,max_length):
    start_time = time.time()
    
    charset = string.ascii_letters + string.digits + string.punctuation
    
    for length in range(1,max_length + 1):
        for attempt in itertools.product(charset,repeat = length):
            attempt_pass = "".join(attempt)
            print(f"Trying Password: {attempt_pass}")
            
            if attempt_pass == target_pass:
                end_time = time.time()
                print("\n Password Found!")
                print(f"Password:{attempt_pass}")
                print(f"Time taken:{end_time - start_time:.2f} seconds")
                return attempt_pass
            
    print("\n Password not found within the maximum length.")
    return None

if __name__ == "__main__":
    Pass = input("Enter Target Password:")
    max_length = int(input("Enter max length:"))
    
    brute_force(Pass,max_length)