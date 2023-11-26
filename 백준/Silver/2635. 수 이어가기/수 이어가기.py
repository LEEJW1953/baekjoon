import sys
input=sys.stdin.readline

n=int(input())
ans=0
arr=[]
for i in range(1, n+1):
    tmp=[n, i]
    while True:
        a=tmp[-2]-tmp[-1]
        if a<0:
            break
        tmp.append(a)
    if ans<len(tmp):
        ans=len(tmp)
        arr=tmp[:]
print(ans)
print(*arr)