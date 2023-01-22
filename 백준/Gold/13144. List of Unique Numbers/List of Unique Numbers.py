import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
num=[0]*100001
s, e=0, 0
count=0
while s<n and e<n:
    if not num[arr[e]]:
        num[arr[e]]=1
        e+=1
        count+=e-s
    else:
        while num[arr[e]]:
            num[arr[s]]=0
            s+=1
print(count)