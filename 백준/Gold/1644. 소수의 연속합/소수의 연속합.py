import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*(n+1)
count=0
for i in range(2, int(n**0.5)+1):
    if not arr[i]:
        j=2*i
        while j<n+1:
            arr[j]=1
            j+=i
p=[]
for i in range(2, len(arr)):
    if not arr[i]:
        p.append(i)
s, e=0, 0
while e<len(p):
    tmp=sum(p[s:e+1])
    if tmp==n:
        count+=1
        s+=1
    elif tmp<n:
        e+=1
    elif tmp>n:
        s+=1
print(count)