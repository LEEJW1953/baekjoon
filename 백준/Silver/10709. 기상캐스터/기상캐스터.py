import sys
input=sys.stdin.readline

h,w=map(int, input().split())
arr=[list(input().strip()) for _ in range(h)]
for i in range(h):
    res=[-1]*w
    for j in range(w-1, -1, -1):
        tmp=-1
        for k in range(j, -1, -1):
            if arr[i][k]=='c':
                tmp=j-k
                break
        res[j]=tmp
    print(*res)