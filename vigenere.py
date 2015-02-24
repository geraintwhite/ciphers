import sys

args = sys.argv[1:]

if len(args) < 3:
    sys.exit('Usage: {} [-e filename|plaintext] [-d filename|ciphertext] secret'.format(sys.argv[0]))

option = args[0]

try:
    with open(args[1]) as f:
        inputtext = f.read()
except FileNotFoundError:
    inputtext = args[1]

secret = args[2]

outputtext = ''
for i, c in enumerate(inputtext):
    if option == '-e':
        outputtext += chr((ord(c.upper())+ord(secret[i%len(secret)].upper())-130)%26+65)
    elif option == '-d':
        outputtext += chr((ord(c.upper())-ord(secret[i%len(secret)].upper())-130)%26+65)

print(outputtext)
