import sys
input=sys.stdin.readline

n, k=map(int, input().split())
arr=[]
count=0
a=1
for i in range(n):
    arr.append(int(input()))

while True:
    if k==0:
        break
    elif arr[n-a]<=k:
        count+=(k//arr[n-a])
        k=(k%arr[n-a])
    else:
        a+=1
print(count)