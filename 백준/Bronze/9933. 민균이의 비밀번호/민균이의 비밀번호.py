n=int(input())
arr=[]
for i in range(n):
    s=input()
    arr.append(s)
for i in range(n):
    for j in range(n):
        if arr[i]==arr[j][::-1]:
            print(len(arr[i]), arr[i][len(arr[i])//2])
            exit(0)