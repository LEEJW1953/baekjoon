import sys
input=sys.stdin.readline

n, x = map(int, input().split())
arr=list(map(int, input().split()))
d={}
total=sum(arr[0:x])
maxx=sum(arr[0:x])
d[total]=1
for i in range(1, n-x+1):
    total+=(arr[i+x-1]-arr[i-1])
    maxx=max(total, maxx)
    if total in d:
        d[total]+=1
    else:
        d[total]=1
if maxx:
    print(maxx)
    print(d[maxx])
else:
    print('SAD')