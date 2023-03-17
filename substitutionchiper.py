import random

huruf = 'abcdefghijklmnopqrstuvwxyz.! '
key = 'napdshtdwcgh.pmsgbbtdnmnjk!'
plaintext = "Acnan Dini Niken Putri Darmasari"


def makeKey(huruf):
   huruf = list(huruf)
   random.shuffle(huruf)
   return ''.join(huruf)

def encrypt(plaintext, key, huruf):
    keyMap = dict(zip(huruf, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, huruf):
    keyMap = dict(zip(key, huruf))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, huruf)

print("Plain text :", plaintext)
print("key :", key)
print("Chiper :", cipher)
print("Decrypted :", decrypt(cipher, key, huruf))
