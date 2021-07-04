import hashlib


val = input("Enter the string to be hashed : ")

crypt1 = hashlib.md5(val.encode())
crypt2 = hashlib.sha1(val.encode())
crypt3 = hashlib.sha256(val.encode())
print("the md5 encrypt of the string is:")
print(crypt1.hexdigest())
print("the sha1 encrypt of the string is:")
print(crypt2.hexdigest())
print("the sha256 encrypt of the string is:")
print(crypt3.hexdigest())