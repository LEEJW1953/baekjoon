import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    total, maxx, count, tmp = 0, 0, 0, -1
    for i in range(n):
        s=int(input())
        if s>maxx:
            maxx=s
            count=1
            tmp=i+1
        elif s==maxx:
            count+=1
        total+=s
    if count==1:
        if maxx>(total//2):
            print(f'majority winner {tmp}')
        else:
            print(f'minority winner {tmp}')
    else:
        print('no winner')