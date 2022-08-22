n=int(input())
arr=list(map(int, input().split()))
arr1=sorted(list(set(arr)))

arr2={arr1[i]: i for i in range(len(arr1))}

for i in arr:
    print(arr2[i], end=' ')