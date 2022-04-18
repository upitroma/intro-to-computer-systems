;take two bytes of input. add one to the first, output as char. add 5 to the second, output as decimal
br main 
ch: .BLOCK 1 
j: .BLOCK 2
main: ldba charIn,d
stba ch,d 
deci j,d 
ldwa j,d 
adda 5,i
stwa j,d 
ldba  ch,d 
adda 1,i
;stba ch,d 
;ldba ch,d 
stba charOut,d
ldba '\n',i
stba charOut,d
deco j,d
ldba '\n',i
stba charOut,d
stop 
.END
