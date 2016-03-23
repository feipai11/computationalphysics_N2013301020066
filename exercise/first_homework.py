def prlet(st,length):
    g1=(' 000000 ','0       ','0       ','0     0 ',' 000000 ')
    s1=(' 000000 ','0       ',' 00000  ','      0 ','000000  ')
    f1=('0000000 ','0       ','00000   ','0       ','0       ')
    sp=('        ','        ','        ','        ','        ')
    letters={' ':sp,'g':g1,'s':s1,'f':f1}
    raw=[' ']*5
    for i in range(5):
        for j in range(length):
            raw[i]=raw[i] + letters[st[j]][i]
        print raw[i]
    return raw
def gain():
    name=raw_input('please input your names:')
    length=len(name)
    name=name.lower()
    prlet(name,length)

gain()
