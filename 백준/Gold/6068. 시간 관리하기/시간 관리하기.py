import sys
input=sys.stdin.readline

n=int(input())
arr=[]
ans=1e8
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:-x[1])
for i in range(n):
    ans=min(ans-arr[i][0], arr[i][1]-arr[i][0])
    if ans<0:
        print(-1)
        exit(0)
print(ans)