import sys
input=sys.stdin.readline

n=int(input())
st, en = 1, 2
ans=0
while st<=n:
    tmp=0
    for i in range(st, en):
        tmp+=i
    if tmp==n:
        ans+=1
        st+=1
    elif tmp<n:
        en+=1
    else:
        st+=1
print(ans)