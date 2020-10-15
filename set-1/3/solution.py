#!/usr/bin/python3

import base64
import binascii

# Challenge 2: Fixed XOR

string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
string1 = binascii.unhexlify(string)

for byte in range(1, 0xff):
    answer = ''
    printable = True
    for i in range(0, len(string1)):
        answer += chr(string1[i] ^ byte)
    if " " in answer:
        print(answer)

# Solution: Cooking MC's like a pound of bacon
