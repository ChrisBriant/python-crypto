#Alice and Bob share a secret key
import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

secret_key = 'Secret key'.encode()

#Alice wants to compute a MAC
m = 'Hay Bob. You are still awesome'.encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print(m, ' ', hmac)

#Eve comes along and modifies the message
m = modify(m)
print(m)

#Bob receives and validates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)
