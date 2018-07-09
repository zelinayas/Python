import binascii

data=bytes("ABCD","utf-8")
print(binascii.hexlify (data))


data=bytes("ABCD","utf-32")
print(binascii.hexlify (data))

data=bytes("ABCD","ASCII")
print(binascii.hexlify (data))