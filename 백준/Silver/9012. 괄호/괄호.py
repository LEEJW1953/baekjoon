import sys

n=int(input())
for i in range(n):
    ps=sys.stdin.readline().strip()
    result=0
    for i in ps:
        if i=='(':
            result+=1
        elif i==')':
            result-=1
            if result<0:
                break
    if result==0:
        print('YES')
    else:
        print('NO')