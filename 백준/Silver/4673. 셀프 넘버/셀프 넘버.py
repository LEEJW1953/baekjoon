def d(num):
    ans=num
    for i in str(num):
        ans+=int(i)
    return ans
arr=[]
for i in range(1,10001):
    arr.append(i)
arr1=set(arr)
arr=[]
for i in range(1,10001):
    arr.append(d(i))
arr2=set(arr)
arr=list(arr1-arr2)
arr.sort()
for i in range(len(arr)):
    print(arr[i])