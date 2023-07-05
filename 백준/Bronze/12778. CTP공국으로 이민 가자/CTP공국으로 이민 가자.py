import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    m, s = map(str, input().split())
    m=int(m)
    arr=list(input().split())
    tmp=[]
    if s=='C':
        for j in range(m):
            tmp.append(str(ord(arr[j])-64))
    else:
        for j in range(m):
            tmp.append(chr(int(arr[j])+64))
    print(' '.join(tmp))