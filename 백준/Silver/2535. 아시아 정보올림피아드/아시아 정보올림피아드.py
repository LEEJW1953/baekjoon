import sys
input=sys.stdin.readline

n=int(input())
arr=[]
d={}
tmp=0
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:-x[2])
for i in range(n):
    if tmp==3:
        exit(0)
    if arr[i][0] not in d:
        d[arr[i][0]]=1
    else:
        if d[arr[i][0]]==2:
            continue
        else:
            d[arr[i][0]]+=1
    tmp+=1
    print(arr[i][0], arr[i][1])
print(arr)