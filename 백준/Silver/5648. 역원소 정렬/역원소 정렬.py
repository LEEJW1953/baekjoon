import sys
input=sys.stdin.readline

arr=[]
n=1e7
while True:
    if len(arr)==n:
        break
    tmp=list(map(str, input().split()))
    if not arr:
        n=int(tmp[0])
        tmp=tmp[1:]
    arr1=[]
    for i in tmp:
        arr.append(int(i[::-1]))
arr.sort()
for i in range(n):
    print(arr[i])