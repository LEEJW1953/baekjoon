import sys
input=sys.stdin.readline

def com(x, y):
    count=0
    i=1
    while True:
        a=y**i
        if x//a==0:
            break
        else:
            count+=x//a
            i+=1
    return count

n, m=map(int,input().split())
r=n-m
result1=com(n,5)-com(m,5)-com(r,5)
result2=com(n,2)-com(m,2)-com(r,2)
print(min(result1, result2))