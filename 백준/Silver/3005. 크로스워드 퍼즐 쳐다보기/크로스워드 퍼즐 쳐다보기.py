import sys
input=sys.stdin.readline

r, c = map(int, input().split())
arr=[list(input().strip()) for _ in range(r)]
ans=[]
for i in range(r):
    s=''.join(arr[i])
    tmp=s.split('#')
    for j in tmp:
        if len(j)>1:
            ans.append(j)
for i in range(c):
    s=''
    for j in range(r):
        s+=arr[j][i]
    tmp=s.split('#')
    for j in tmp:
        if len(j)>1:
            ans.append(j)
ans.sort()
print(ans[0])