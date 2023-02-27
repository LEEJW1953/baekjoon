import sys
input=sys.stdin.readline

na, nb = map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort()
b.sort()
tmp={}
arr=[]
arr1=[]
for i in range(na):
    arr.append(a[i])
    tmp[a[i]]=1
for i in range(nb):
    arr.append(b[i])
    tmp[b[i]]=1
arr=list(set(arr))
for i in range(nb):
    tmp[b[i]]=0
for i in range(len(arr)):
    if tmp[arr[i]]:
        arr1.append(arr[i])
arr1.sort()
print(len(arr1))
if len(arr1):
    print(" ".join(map(str, arr1)))