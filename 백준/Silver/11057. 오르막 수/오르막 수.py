import sys
input=sys.stdin.readline

n=int(input())
dp=[0]
arr=[1]*10
# if n>=3:
for i in range(1, n+1):
    arr1=[]
    for j in range(10):
        arr1.append(arr[j])
    dp.append(sum(arr))
    for j in range(10):
        arr[j]=sum(arr1[0:j+1])
print(dp[-1]%10007)