import sys
input=sys.stdin.readline

n, l = map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
count=0
i=0
while i<n:
    if i==n-1:
        count+=1
        break
    else:
        for j in range(i+1, n):
            if arr[j]>arr[i]+l-1:
                i=j
                break
            if j==n-1:
                i=n
        count+=1
print(count)