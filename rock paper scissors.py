import random
a=['rock','paper','scissors']
cs=0
us=0
while True:
    c=random.choice(a)
    u=input('rock,paper,scissors ? (e for exit) : ')
    if c=='rock' and u=='scissors' or  c=='paper' and u=='rock' or  c=='scissors' and u=='paper' :
        print(c)
        cs+=1
        print(cs,us)
    if c=='rock' and u=='rock' or  c=='paper' and u=='paper' or  c=='scissors' and u=='scissors' :
        print(c)
        print(cs,us)
    if u=='e':
        if cs>us:
            print('computer scores : ',cs)
            print('your scores : ',us)
            print('computer is win')
            break
        else:
            print('computer scores : ',cs)
            print('your scores : ',us)
            print('you win')
    else:
        print(c)
        us+=1
        print(cs,us)
    