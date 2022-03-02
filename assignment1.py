#!/bin/python3

#get user input
print("enter a decimal (ex. 5.5)")
input = input()

#check if negative
negative="0"
if input[0] == "-":
    input = input[1:]
    negative = "1"

#seporate decimal and integer
whole, dec = str(input).split(".")

#convert whole portion to binary
whole=int(whole)
wholeBin=bin(whole)[2:]

#convert decimal portion to binary
dec=float("0."+dec)
decBin=""
for i in range(4):
    dec*=2
    if dec >= 1:
        dec-=1
        decBin+="1"
    else:
        decBin+="0"

#print binary decimal form
decimalString=str(wholeBin)+"."+str(decBin)
print("binary decimal form (positive): "+decimalString)

binaryFloatExcess3Form=""

#if exponent is negative
if(decimalString.index(".")==1 and decimalString[0]=="0"):
    newDecimalIndex=decimalString.index("1")+1 #move the decimal point to the right of the first 1

    decimalString=decimalString[newDecimalIndex:] #get everything after the decimal point

    exp=bin(-(newDecimalIndex-2)+3)[2:] #get the exponent in excess 3

    exp = str(exp).rjust(3, '0') #pad the exponent with zeros

    decimalString=decimalString[0:4] #get the first 4 decimal places
    decimalString=decimalString.ljust(4, '0') #pad the remaining decimal places with zeros

    binaryFloatExcess3Form=negative+exp+decimalString

#if exponent is zero
elif decimalString.index(".")==1 and decimalString[0]=="1":
    binaryFloatExcess3Form=negative+"011"+decimalString[2:]

#if exponent is positive
else:
    newDecimalIndex=decimalString.index("1")+1 #move the decimal point to the right of the first 1

    exp=bin(decimalString.index(".")+2)[2:] #get the exponent in excess 3
    exp = str(exp).rjust(3, '0') #pad the exponent with zeros
    
    decimalString=decimalString[newDecimalIndex:] #get everything after the decimal point
    decimalString=decimalString.replace(".", "") #remove the decimal point since it's still in the decimal portion
    decimalString=decimalString[0:4] #get the first 4 decimal places
    decimalString=decimalString.ljust(4, '0') #pad the remaining decimal places with zeros

    binaryFloatExcess3Form=negative+exp+decimalString

print("binary float excess 3 form: "+binaryFloatExcess3Form)