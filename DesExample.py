from lib.pyDes import *

def modify(cipher):
    mod = [0] * len(cipher)
    mod[8] = 1
    # mod[10] = ord(' ') ^ ord('1')
    # mod[11] = ord(' ') ^ ord('0')
    # mod[12] = ord(' ') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

#message = "0123456701234567"
message = 'Give Bob:    $10 and send them to me.'
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key,ECB,iv,pad=None, padmode=PAD_PKCS5)
# create the cipher here


# Alice sending the encrypted message
# encrypt the message to cipher
print("Length of plain text:", len(message))
cipher = k.encrypt(message)
print("Length of cipher text:", len(cipher))

cipher = modify(cipher)

print('Encrypted: ',cipher[0:8])
print('Encrypted: ',cipher[8:16])
print('Encrypted: ',cipher[16:])

# Bob decrypting the cipher text
# decrypt the cipher to message
message = k.decrypt(cipher)
print("Decrypted:", message)