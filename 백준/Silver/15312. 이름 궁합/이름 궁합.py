import sys
input=sys.stdin.readline

arr=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a=input().strip()
b=input().strip()
tmp=[]
for i in range(len(a)):
    tmp.append(arr[ord(a[i])-65])
    tmp.append(arr[ord(b[i])-65])
ans=tmp[:]
while len(ans)>2:
    tmp=ans[:]
    ans=[]
    for i in range(len(tmp)-1):
        ans.append((tmp[i]+tmp[i+1])%10)
print(''.join(list(map(str, ans))))