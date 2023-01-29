import sys
input=sys.stdin.readline

n, k=map(int, input().split())
count=0
arr=[]
for i in range(2, n+1):
    arr.append(i)
while count<k:
    i=arr[0]
    for j in range(i, n+1, i):
        if j in arr:
            count+=1
            arr.remove(j)
            if count==k:
                print(j)
                exit(0)