import sys
input=sys.stdin.readline

n, c = map(int, input().split())
m=int(input())
arr=[list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x:(x[1], x[0]))
answer=0
arr1=[c]*(n+1)
for i in range(m):
    tmp=c
    for j in range(arr[i][0], arr[i][1]):
        tmp=min(tmp, arr1[j])
    tmp=min(tmp, arr[i][2])
    for j in range(arr[i][0], arr[i][1]):
        arr1[j]-=tmp
    answer+=tmp
print(answer)