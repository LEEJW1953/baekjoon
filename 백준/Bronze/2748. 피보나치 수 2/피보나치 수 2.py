import sys
input = sys.stdin.readline

arr=[0, 1]
for i in range(90):
    arr.append(arr[i]+arr[i+1])
print(arr[int(input())])