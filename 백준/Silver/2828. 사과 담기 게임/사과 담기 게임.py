import sys
input=sys.stdin.readline

n, m = map(int, input().split())
box=list(range(1, m+1))
left, right = box[0], box[-1]
j=int(input())
arr=[int(input()) for _ in range(j)]
count=0
for i in range(j):
    if arr[i] in box:
        continue
    elif box[0]>arr[i]:
        tmp=box[0]-arr[i]
        count+=tmp
        for k in range(m):
            box[k]-=tmp
    elif box[-1]<arr[i]:
        tmp=arr[i]-box[-1]
        count+=tmp
        for k in range(m):
            box[k]+=tmp
print(count)