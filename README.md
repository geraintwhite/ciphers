# ciphers

Code implementations of common encryption algorithms

## vigenere.py

A polyalphabetic substitution cipher

`Usage: python vigenere.py [-e filename|plaintext] [-d filename|ciphertext] secret`

```
$ python vigenere.py -e "the quick brown fox jumped over the lazy dog" qwertyuiop
JDI JSCKY RNSNG ZWL ZQQGXB WJTH XYX FINN ZSX
$ python vigenere.py -d "JDI JSCKY RNSNG ZWL ZQQGXB WJTH XYX FINN ZSX" qwertyuiop
THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG

$ python vigenere.py -e vigenere.py secret > ciphertext
$ python vigenere.py -d ciphertext secret
IMPORT SYS

ARGS = SYS.ARGV[1:]

IF LEN(ARGS) < 3:
    SYS.EXIT('USAGE: PYTHON {} [-E FILENAME|PLAINTEXT] [-D FILENAME|CIPHERTEXT] SECRET'.FORMAT(SYS.ARGV[0]))

OPTION = ARGS[0]

TRY:
    WITH OPEN(ARGS[1]) AS F:
        INPUTTEXT = F.READ()
EXCEPT FILENOTFOUNDERROR:
    INPUTTEXT = ARGS[1]

SECRET = ARGS[2]

OUTPUTTEXT = ''
FOR I, C IN ENUMERATE(INPUTTEXT):
    N, S = ORD(C.UPPER()), ORD(SECRET[I%LEN(SECRET)].UPPER())-130
    D = N-S IF OPTION == '-D' ELSE N+S
    OUTPUTTEXT += CHR(D%26+65) IF C.ISALPHA() ELSE C

PRINT(OUTPUTTEXT)
````
