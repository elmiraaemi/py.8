def sum ():
    s=s1+s2
    if s>=60:
        s=s-60
        m=m1+m2+1
        if m>=60:
            m=m-60
            h=h1+h2+1
            print(h,':',m,':',s)
        else:
            h=h1+h2
            print(h,':',m,':',s)
    else:
        m=m1+m2
        h=h1+h2
        print(h,':',m,':',s)
def sub():
    s=s1-s2
    if s<0:
        m=m1-m2-1
        s=(s1+60)-s2
        if m<0:
            h=h1-h2
            m=(m1+60)-m2
        else:
            h=h1-h2
            print(h,':',m,':',s)
    else:      
        m=m1-m2
        h=h1-h2
        print(h,':',m,':',s)
def s2t():
    a = int(input("saconds :"))
    if 60 <= a <3600 :
        b = int( a / 60)
        c = b * 60
        d = a - c
        print(b , ":" , d)
    elif a >= 3600 :
        h = int( a / 3600)
        e = h * 3600
        f = a - e
        if f < 60 :
            print(h , ":" , "00" , ":" , f )
        if f > 60 :
            g = int( f / 60)
            k = g * 60
            y = f - k
            print(h , ":" , g , ":" , y )
    elif a < 60 :
        print("Less than a minute")
def t2s():
    h = int(input( "hour : "))
    m = int(input( "minute : "))
    s = int(input( "Second : "))
    j = h * 3600
    n = m *  60
    x = j + n + s
    print(x)
while True:
    n = input('( + , - , t2s , s2t , exit ) : ')
    if n == '+':
        h1=int(input('h1 : '))
        m1=int(input('m1 : '))
        s1=int(input('s1 : '))
        h2=int(input('h2 : '))
        m2=int(input('m2 : '))
        s2=int(input('s2 : '))
        sum()
    elif n == '-':
        h1=int(input('h1 : '))
        m1=int(input('m1 : '))
        s1=int(input('s1 : '))
        h2=int(input('h2 : '))
        m2=int(input('m2 : '))
        s2=int(input('s2 : '))
        sub()
    elif n == 's2t':s2t()
    elif n == 't2s':t2s()   
    elif n == 'exit':break
    else: print('Wrong operation')