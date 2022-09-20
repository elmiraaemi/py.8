def mul():
    s=a*c
    m=b*d
    print()
    print('',s)
    print('____')
    print()
    print('',m)
def sum():
    for i in range(1 , (b*d)+1):
        if i % b == 0 and i % d == 0:
            break
    bb=i/b
    dd=i/d
    if i==d:
        aa=a*bb
        s=aa+c
    elif i==b:
        cc=c*dd
        s=a+cc
    else:
        aa=a*dd
        cc=c*bb
        s=aa+cc
    m=i
    print()
    print('',s)
    print('____')
    print()
    print('',m)
def sub():
    for i in range(1 , (b*d)+1):
        if i % b == 0 and i % d == 0:
            break
    bb=i/b
    dd=i/d
    if i==d:
        aa=a*bb
        s=aa-c
    elif i==b:
        cc=c*dd
        s=a-cc
    else:
        aa=a*dd
        cc=c*bb
        s=aa-cc
    m=i
    print()
    print('',s)
    print('____')
    print()
    print('',m)
def div():
    s=a*d
    m=b*c
    print()
    print('',s)
    print('____')
    print()
    print('',m)
while True:
    e = input('(+, -, *, /, exit ) : ')
    a=int(input('s1 : '))
    b=int(input('m1 : '))
    c=int(input('s2 : '))
    d=int(input('m2 : '))
    if e=='+':sum()
    if e=='-':sub()
    if e=='*':mul()
    if e=='/':div()
    elif e=='exit': break
    else: print('Wrong operation')