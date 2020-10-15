#!/usr/bin/python3

import binascii

data = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

data = bytes(data)

key = b"ICE"

result = []

i = 0
for c in data:
    result.append(c ^ key[i%3])
    i += 1

encodedY = binascii.hexlify(bytes(result)).decode("ascii")
print(encodedY)

