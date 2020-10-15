#!/usr/bin/python3

s1 = b"this is a test"
s2 = b"wokka wokka!!!"

def hamming_distance(a, b):
    distance = 0
    for i in range(0, len(a)):
        for mask in [0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000, 0b1000000, 0b10000000]:
            if a[i]&mask != b[i]&mask:
                distance += 1

    return distance

assert(hamming_distance(s1, s2) == 37)


for KEYSIZE in range(2, 40):

