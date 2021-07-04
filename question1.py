import hashlib


val = input("Enter the string to be hashed : ")

crypt1 = hashlib.md5(val.encode())
print("the md5 encrypt of the string is:")
print(crypt1.hexdigest())
