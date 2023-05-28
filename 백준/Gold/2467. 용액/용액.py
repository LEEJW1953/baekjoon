import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
s, e = 0, n-1
left=-1
right=-1
total=1e11
while s<e:
    tmp=arr[s]+arr[e]
    if tmp==0:
        left=s
        right=e
        total=tmp
        break
    if abs(tmp)<abs(total):
        left=s
        right=e
        total=tmp
    if tmp<0:
        s+=1
    elif tmp>0:
        e-=1
print(arr[left], arr[right])