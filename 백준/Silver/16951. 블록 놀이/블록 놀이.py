import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr=list(map(int, input().split()))
ans=10000
for i in range(1, 1000):
    count=0
    for j in range(n):
        if arr[j]!=(k*j+i):
            count+=1
            if ans<count:
                break
    ans=min(ans, count)
print(ans)