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


ciphertext = ""
with open("file.txt", "rb") as f:
    ciphertext = f.read()


possible_keys = []
for KEYSIZE in range(2, 40):
    possible_keys.append((KEYSIZE, hamming_distance(ciphertext[0:KEYSIZE], ciphertext[KEYSIZE:KEYSIZE*2])/KEYSIZE))

for KEYSIZE, distance in possible_keys:
    print("Possible keysize " + str(KEYSIZE) + " of distance " + str(distance))


