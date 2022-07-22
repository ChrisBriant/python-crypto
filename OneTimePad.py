import random

def generate_key_stream(n):
    return bytes([random.randrange(0,256) for i in range(n)])

def xor_bytes(key_stream,message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

message = "You are awesome do de lalla spghetti cheese burger please, me."
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream,message)
print(key_stream)
print(cipher)
print(xor_bytes(key_stream,cipher))