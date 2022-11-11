import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
arr1=[0]
for i in range(n):
    arr1.append(arr[i]+i+1)
print(max(arr1)+1)