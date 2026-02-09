#!/usr/bin/python3
def islower(c):
    return ord(c) >= 97 and ord(c) <= 122

c = input("Enter a character: ")
if islower(c):
    print("{} is lower".format(c))
else:
    print("{} is upper".format(c))
