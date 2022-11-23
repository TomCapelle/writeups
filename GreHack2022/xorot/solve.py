import base64
import string
import random
from itertools import cycle

symbols = string.printable

# Fetched from the sources

def rot(n, s):
    encoded = symbols[n:] + symbols[:n]
    lookup = str.maketrans(symbols, encoded)
    return s.translate(lookup)


# I Think I was hungry when i wrote this plaintext

clear="hello world i love cakes with salad and fruits and love"
crypted = "BDJ1dTE+HRhmFTYyGw80FSIOD0lHGRR+Eg03KiATPEU6MTFURDIhKRNmAgsbEQ8FFgoSLntgJQ=="

# First we prepare the encrypted message for further computing

b64_bytes = base64.b64decode(crypted)
b64_decoded = b64_bytes.decode('utf-8')

all_rot = dict()

possible_keys = dict()

# We compute all possible ROT outputs

for i in range(1,26):
    all_rot[i] = rot(i, clear)

# We do the plaintext attack with all ROT outputs

for i in range(1,26):
    r = all_rot[i]

    k = ''.join(chr(ord(c) ^ ord(k)) for c,k in zip(r, b64_decoded))
    possible_keys[i] = k

# We deduce which key is the flag

flag = ""
for i in range(1,26):
    if "GH22" in possible_keys[i]:
        flag = possible_keys[i]

# We prettify the output and then we print the flag !

flag = flag[:flag.index("}") + 1]

print(flag)