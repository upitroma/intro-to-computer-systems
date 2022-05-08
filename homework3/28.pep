br main 
ch: .block 1

main: ldba 0xFC15,d
suba 1,i
stba 0xFC16,d

ldba "\n",i 
stba 0xFC16,d

stop
.end