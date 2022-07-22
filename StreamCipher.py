from curses import keyname
import random

class KeyStream:
    def __init__(self,key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 + self.next*12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256


def encrypt(key,message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))]) 

#Causes distortion in the message
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0,8)
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod = [0]*len(cipher)
    mod[9] =ord(' ') ^ ord('$')
    mod[10] =ord(' ') ^ ord('1')
    mod[11] =ord('$') ^ ord('0')
    mod[12] =ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))]) 

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

def crack(key_stream, cipher):
    length = min(len(key_stream),len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

def brute_force(plain,cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
            else:
                return k
    return False

# keystream = KeyStream()
# for i in range(10):
#     print(keystream.get_key_byte())

key= KeyStream(10)
message = 'Send Bob:  $10'.encode()
print(message)
cipher = encrypt(key,message)
print(cipher)

#distort
#cipher = transmit(cipher,5)
#Bob modifies
cipher = modification(cipher)

key = KeyStream(10)
message = encrypt(key,cipher)
print(message)

#KEY REUSE VULNERABILITY

#EVIL EVE
print('I AM EVE')
eves_message = 'These are the secrets of Castle Greyskull.'.encode()

#Alice
key= KeyStream(10)
message = eves_message
print(message)
cipher = encrypt(key,message)
print(cipher)

#This is Eve alone
eves_key_stream = get_key(eves_message,cipher)

#This is Bob
key = KeyStream(10)
message = encrypt(key,cipher)
print(message)

#Alice again
message = 'Hi, Bob let us meet to discuss our plan of world domination.'.encode()
key = KeyStream(10)
cipher = encrypt(key,message)
print(cipher)

#Bob again
key = KeyStream(10)
message = encrypt(key,cipher)
print(message)

#Eve is evil again
print('This is Eve')
print(crack(eves_key_stream,cipher))


#LOW ENTROPY VULNERABILITY

#This is Alice
#secret_key = 10
secret_key = random.randrange(0, 2**20)
print(secret_key)
key = KeyStream(secret_key)
header = "MESSAGE:"
message = header + "My message to Bob"
message = message.encode()
print(message)
cipher = encrypt(key,message)
print(cipher)

#This is Bob
key = KeyStream(secret_key)
message = encrypt(key,cipher)
print(message)



#This is eve
bf_key = brute_force(header.encode(),cipher)
print("Eve's brute force key:", bf_key)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)