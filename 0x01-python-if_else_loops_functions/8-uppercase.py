#!/usr/bin/python3
def uppercase(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
