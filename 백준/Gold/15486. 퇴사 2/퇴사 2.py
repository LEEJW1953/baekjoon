import sys
input=sys.stdin.readline

n=int(input())
arr=[]
result=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
    result.append(arr[i][1])
result.append(0)
for i in range(n-1, -1, -1):
    if (arr[i][0]+i)>n:
        result[i]=result[i+1]
    else:
        result[i]=max(result[i+1], arr[i][1]+result[i+arr[i][0]])
print(result[0])