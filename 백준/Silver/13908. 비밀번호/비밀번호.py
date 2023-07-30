import sys
input=sys.stdin.readline

n, m = map(int, input().split())
count=0
if m:
    arr=list(map(str, input().split()))
else:
    arr=[]
for i in range(10**n):
    tmp=True
    target=str(i).zfill(n)
    for j in arr:
        if j not in target:
            tmp=False
            break
    if tmp:
        count+=1
print(count)