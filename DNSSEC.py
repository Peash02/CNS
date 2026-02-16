import hashlib

def sign_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

original_domain = input("Enter original domain name:")
signature = sign_data(original_domain)
print("\nGenerated DNS Signature:",signature)
received_domain = input("\nEnter received domain name:")
verify_signature = sign_data(received_domain)
if verify_signature == signature:
    print("\n DNSSEC Verificatioon Successful : Data is Authentic.")
else:
    print("\n DNSSEC Verification Failed : Data has been modified.")
    