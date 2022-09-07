import sys
input=sys.stdin.readline

n=int(input())
arr=[]
count=0
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:(x[1], x[0]))
a=0
num=0
while True:
    if a==n:
        break
    if arr[a][0]<num:
        a+=1
    elif arr[a][0]>=num:
        num=arr[a][1]
        count+=1
        a+=1
print(count)