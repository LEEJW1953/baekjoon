import sys
input=sys.stdin.readline

n=int(input())
arr1=[]
arr2=[]
result=0
for i in range(n):
    num=int(input())
    if num<=0:
        arr1.append(num)
    elif num==1:
        result+=1
    else:
        arr2.append(num)
arr1.sort()
arr2.sort(reverse=True)
l1=len(arr1)
l2=len(arr2)
for i in range(l1//2):
        result+=arr1[2*i]*arr1[2*i+1]
if l1%2==1:
    result+=arr1[-1]
for i in range(l2//2):
        result+=arr2[2*i]*arr2[2*i+1]
if l2%2==1:
    result+=arr2[-1]
print(result)