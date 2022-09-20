def sum():
    r=a+c
    i=d+d
    print(r,'+',i,'i')
def sub():
    r=a-c
    i=b-d
    print(r,'+',i,'i')
def mul():
    r1=a*c
    i1=b*c
    i2=a*d
    r2=b*d
    r=r1-r2
    i=i1+i2
    print(r,'+',i,'i')
while True:
    e = input('(+, -, *, 5 exit ) : ')
    a=int(input('r1 : '))
    b=int(input('i1 : '))
    c=int(input('r2 : '))
    d=int(input('i2 : '))
    if e == '+':sum()
    elif e == '-':sub()
    elif e == '*':mul()
    elif e == 'exit':break
    else: print('Wrong operation')