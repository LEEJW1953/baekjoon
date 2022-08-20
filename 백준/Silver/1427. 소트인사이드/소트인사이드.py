n=input()
arr=[]
for i in n:
    arr.append(int(i))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i],end='')