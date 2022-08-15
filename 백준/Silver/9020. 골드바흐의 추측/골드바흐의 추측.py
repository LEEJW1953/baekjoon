t=int(input())

arr=[0]*(10002)
arr[0]=arr[1]=1
arr1=[]
for i in range(2, 1001):
    if arr[i]==0:
        k=2*i
        while k<=(10001):
            arr[k]=1
            k+=i
for i in range(len(arr)):
    if arr[i]==0:
        arr1.append(i)

def pnum(n):
    if n in arr1:
        return True
    else:
        return False

for i in range(t):
    n=int(input())
    arr2=[]
    for j in range((n+1)//2,1,-1):
        if pnum(j)==True and pnum(n-j)==True:
            print(j, n-j)
            break