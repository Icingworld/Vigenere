from code import *

choice = input("加密（1）？解密（2）：")
if choice == "1":
    word = input("明文：")
    key = input("密钥：")
    print(code(word, key))
elif choice == "2":
    word = input("密文：")
    key = input("密钥：")
    print(decode(word, key))
