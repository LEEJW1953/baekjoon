import sys
input=sys.stdin.readline

n=int(input())
count2=0
count5=0
for i in range(1, n+1):
    a=2
    while i!=1:
        if i%a==0:
            i=i//a
            if a==2:
                count2+=1
            elif a==5:
                count5+=1
        else:
            a+=1
print(min(count2, count5))