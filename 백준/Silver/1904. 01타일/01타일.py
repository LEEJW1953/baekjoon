n=int(input())
arr=[1, 2]

for i in range(2, n):
    arr.append((arr[i-2]+arr[i-1])%15746)

print(arr[n-1]%15746)