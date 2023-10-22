import sys
input=sys.stdin.readline

n, h, w = map(int, input().split())
s=[list(input().strip()) for _ in range(h)]
ans=''
for i in range(0, len(s[0]), w):
    tmp=[]
    tmp1=False
    for j in range(h):
        for k in range(i, i+w):
            tmp.append(s[j][k])
    for j in tmp:
        if j!='?':
            ans+=j
            tmp1=True
            break
    if not tmp1:
        ans+='?'
print(ans)