n, m=map(int, input().split())
arr=[]
arr1=[]
for i in range(n):
    arr.append(input())
for i in range(m):
    arr1.append(input())
dict={}
for i in range(n):
    dict[i+1]=arr[i]
    dict[arr[i]]=i+1
for i in arr1:
    if i.isdigit():
        print(dict[int(i)])
    else:
        print(dict[i])