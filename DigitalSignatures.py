
#These are Alice's RSA keys
#Public key (e,n) 5 164119
#Secret key (d) 21773

import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


n = 164119
e = 5
d = 21773

#This is the message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

#Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, 'big') % n
print('Hash value',h)

#Step 2: decrypt the hash value, use secret exponent
signature = (h**d) % n

#Step 3: send message with signature to Bob
print(message,signature)

#This is Eve being evil and modifies the message
message = modify(message)
print(message)

#Bob verifying the signature
#Step 1: calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, 'big') % n
print('Hash value',h)

#Step 2: Verify the signature
verification = signature % n
print('Verification value: ',verification)


