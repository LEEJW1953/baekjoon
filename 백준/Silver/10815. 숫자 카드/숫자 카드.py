def search(a, array):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==a:
            return 1
        elif array[mid]<a:
            start=mid+1
        else:
            end=mid-1
    return 0

n=int(input())
arr=list(map(int, input().split()))
arr.sort()
m=int(input())
arr1=list(map(int, input().split()))
arr2=[]
for i in range(m):
    arr2.append(search(arr1[i], arr))
for i in range(len(arr2)):
    print(arr2[i], end=' ')