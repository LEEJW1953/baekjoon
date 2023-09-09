import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for i in range(n):
    arr=list(map(int, input().split()))
    if arr[0]==0:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        for j in arr[1:]:
            stack.append(j)
        stack.sort()