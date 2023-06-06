import sys
input=sys.stdin.readline

a, b = map(int, input().split())
arr=['4', '7']
for i in range(1, 10):
    tmp=[]
    for j in range(len(arr)):
        if len(arr[j])==i:
            tmp.append(arr[j]+'4')
            tmp.append(arr[j]+'7')
    for j in range(len(tmp)):
        arr.append(tmp[j])
arr.sort(key=lambda x:int(x))
start, end = -1, -1
for i in range(len(arr)):
    n=int(arr[i])
    if a<=n and start==-1:
        start=i
    if b<n and end==-1:
        end=i
print(end-start)