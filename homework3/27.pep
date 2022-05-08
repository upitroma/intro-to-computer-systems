br main 

width: .block 2
length: .block 2
perim: .block 2

nl: .ascii "\n\x00"
msg1: .ascii "length = \x00"
msg2: .ascii "width = \x00"
msg3: .ascii "perim = \x00"

main: deci length,d
deci width,d

ldwa length,d
adda width,d

asla

stwa perim,d

stro msg1,d
deco length,d
stro nl,d
stro msg2,d
deco width,d
stro nl,d
stro nl,d
stro msg3,d
deco perim,d
stro nl,d

stop
.end
