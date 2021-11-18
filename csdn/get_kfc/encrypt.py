#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

KEY = os.urandom(16)

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = cipher.encrypt(plaintext).hex()
    return ciphertext

message = b"Don't be afraid to fail. It's not the end of the world and in many ways it's the first step toward learning something better and getting better at it."
print(encrypt(message))

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
print(encrypt(flag))