import itertools
import string

def brute_force(pas,max_length = 10):
    char = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for guess in itertools.product(char,repeat = length):
            guess = "".join(guess)
            if guess == pas:
                return f"Password '{pas}' cracked in {length} tries!"
            
            
password = input()
print(brute_force(password))