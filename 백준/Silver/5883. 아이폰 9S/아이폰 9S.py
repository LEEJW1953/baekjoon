import sys
input=sys.stdin.readline

n=int(input())
arr=[]
d={}
ans=0
for i in range(n):
    x=int(input())
    arr.append(x)
    if x not in d:
        d[x]=1
key=list(d.keys())
for i in range(len(key)):
    tmp, tmp1 =  False, 0
    count=0
    for j in range(n):
        if arr[j]==key[i]:
            continue
        if tmp:
            if cur==arr[j]:
                tmp1+=1
                count=max(count, tmp1)
            else:
                count=max(count, tmp1)
                cur=arr[j]
                tmp1=1
        else:
            cur=arr[j]
            tmp1=1
            count=max(count, tmp1)
            tmp=True
    ans=max(ans, count)
print(ans)