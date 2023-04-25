import sys
input=sys.stdin.readline

n=int(input())
arr=[]
price, count = 0, 0
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(n):
    if count==2:
        count=0
    else:
        price+=arr[i]
        count+=1
print(price)