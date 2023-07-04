import sys
input=sys.stdin.readline

arr=[0]
ans=0
for i in range(10):
    n=int(input())
    arr.append(arr[-1]+n)
for i in range(1, 11):
    tmp=abs(100-arr[i])
    if tmp<=abs(100-ans):
        ans=arr[i]
print(ans)