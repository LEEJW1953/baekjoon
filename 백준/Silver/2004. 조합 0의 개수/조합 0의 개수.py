import sys
input=sys.stdin.readline

n, m=map(int,input().split())
r=n-m
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
i=1
while True:
    a=5**i
    if n//a==0:
        i=1
        break
    else:
        count1+=n//a
        i+=1
while True:
    a=5**i
    if m//a==0:
        i=1
        break
    else:
        count2+=m//a
        i+=1
while True:
    a=5**i
    if r//a==0:
        i=1
        break
    else:
        count3+=r//a
        i+=1
while True:
    a=2**i
    if n//a==0:
        i=1
        break
    else:
        count4+=n//a
        i+=1
while True:
    a=2**i
    if m//a==0:
        i=1
        break
    else:
        count5+=m//a
        i+=1
while True:
    a=2**i
    if r//a==0:
        i=1
        break
    else:
        count6+=r//a
        i+=1
result1=count1-count2-count3
result2=count4-count5-count6
print(min(result1, result2))