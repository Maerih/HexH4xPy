# import sys
# import crypt

# sg = input("Enter password to Hash with {b74} salt value: ")

# out = crypt.crypt(sg,'b74')
# print(f'Hash: {out}')

import sys
import hashlib

sg = input("Enter password to hash SHA512: ").encode('utf-8')

out = hashlib.sha512(sg).hexdigest()


print(f'Hash: {out}')