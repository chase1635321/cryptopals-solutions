#!/usr/bin/python3

import base64
import binascii

# Challenge 1: Convert hex to base64

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

decoded = binascii.unhexlify(string)
answer = base64.b64encode(decoded).decode()

if answer == solution:
    print("Correct!")
else:
    print("Failed")
