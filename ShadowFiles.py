import hashlib
import base64

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
# SALTED-SHA512-PBKDF2

password = "password".encode()
# Insert code here
value = hashlib.pbkdf2_hmac('sha512',password,salt,iterations,dklen=128)
print(base64.b64encode(value))