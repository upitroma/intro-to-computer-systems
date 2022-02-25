#!/bin/python3
#https://www.geeksforgeeks.org/python-program-to-convert-floating-to-binary/

import struct
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))


print("enter a decimal (ex. 5.5)")
input = float(input())
# if input[0] == "-":
#     input = input[1:]
#     print("number is negative")
# whole, dec = str(input).split(".")

# whole=float(whole)
# dec=int(dec)

# print(whole, dec)
# print(binary(whole))

print(binary(input))