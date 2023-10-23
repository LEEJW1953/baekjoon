import sys
input=sys.stdin.readline

n=int(input())
arr=[]
ans=0
for i in range(1, 44723):
    arr.append(i*(i-1)//2)
while n:
    for i in range(len(arr)):
        if n<arr[i]:
            ans+=i-1
            n-=arr[i-1]
            break
print(ans)