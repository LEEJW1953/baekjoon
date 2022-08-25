n, m=map(int, input().split())
arr=[]
arr1=[]
for i in range(n):
    arr.append(input())
for i in range(m):
    arr1.append(input())
set=list(set(arr)&set(arr1))
set.sort()
print(len(set))
for i in range(len(set)):
    print(set[i])