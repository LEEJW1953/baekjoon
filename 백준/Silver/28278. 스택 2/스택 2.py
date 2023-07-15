import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for i in range(n):
    c=list(map(int, input().split()))
    com=c[0]
    if com==1:
        stack.append(c[1])
    elif com==2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com==3:
        print(len(stack))
    elif com==4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)