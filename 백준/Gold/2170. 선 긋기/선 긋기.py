import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
s=arr[0][0]
e=arr[0][1]
result=0
for i in range(1, n):
    if arr[i][0]<=e:
        if arr[i][1]<=e:
            continue
        else:
            e=arr[i][1]
    else:
        result+=(e-s)
        s=arr[i][0]
        e=arr[i][1]
result+=(e-s)
print(result)