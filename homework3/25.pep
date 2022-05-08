br main
chConst: .byte 'a'
ch1: .block 1
ch2: .block 1

main: ldba 0xFC15,d
stba ch1,d

ldba 0xFC15,d
stba ch2,d

ldba ch1,d
stba 0xFC16,d

ldba chConst,d
stba 0xFC16,d

ldba ch2,d
stba 0xFC16,d

stop
.end