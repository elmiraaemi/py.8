n=int(input())
b=0
c=int(n*2)-1
m=n
for j in range(1):
    for i in range(1):
        print(' '*c, end='')
        b+=1
        print('*'*b)
    for k in range(n-1):
        c-=1
        print(' '*c, end='')
        b+=2
        print('*'*b)
    for v in range(c-1):
        c+=1
        print(' '*c, end='')
        b-=2
        print('*'*b)