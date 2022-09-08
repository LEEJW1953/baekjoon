n=int(input())
arr=list(map(int, input().split()))
arr.sort()
sum=0
result=0
for i in range(n):
    sum+=arr[i]
    result+=sum
print(result)