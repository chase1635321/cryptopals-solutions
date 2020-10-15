#!/usr/bin/python3

import base64
import binascii

# Challenge 2: Fixed XOR

string = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"
solution = "746865206b696420646f6e277420706c6179"
answer = ''

string1 = binascii.unhexlify(string)
string2 = binascii.unhexlify(key)

for i in range(0, len(string2)):
    answer += chr(string1[i] ^ string2[i])

answer = binascii.hexlify(answer.encode()).decode()

if answer == solution:
    print("Correct!")
else:
    print("Failed")
    print(answer)
