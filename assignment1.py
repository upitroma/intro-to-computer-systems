#!/bin/python3
#https://www.geeksforgeeks.org/python-program-to-convert-floating-to-binary/

print("enter a decimal (ex. 5.5)")
input = input()
if input[0] == "-":
    input = input.lstrip("-")
    print("number is negative")
whole, dec = str(input).split(".")
print(whole, dec)