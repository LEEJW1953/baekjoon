n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str, input().split())))
arr.sort(key=lambda x:(int(x[0])))
for i in range(len(arr)):
    print(arr[i][0],arr[i][1])