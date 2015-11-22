import sys

args = sys.argv[1:]

if len(args) < 3:
    sys.exit('Usage: python {} [-e filename|plaintext] [-d filename|ciphertext] secret'.format(sys.argv[0]))

option = args[0]

try:
    with open(args[1]) as f:
        inputtext = f.read()
except FileNotFoundError:
    inputtext = args[1]

secret = args[2]

outputtext = ''
for i, c in enumerate(inputtext):
    n, s = ord(c.upper()), ord(secret[i%len(secret)].upper())-130
    d = n-s if option == '-d' else n+s
    outputtext += chr(d%26+65) if c.isalpha() else c

print(outputtext)
