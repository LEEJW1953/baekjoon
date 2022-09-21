import sys
input=sys.stdin.readline

def fun3(num):
    if num%3==0:
        return num//3
    elif num%2==0:
        return num//2
    else:
        return num-1

def fun2(num):
    if num%2==0:
        return num//2
    elif num%3==0:
        return num//3
    else:
        return num-1

n=int(input())
arr=[[n]]
i=0
while n!=1:
    arr1=[]
    for j in range(len(arr[i])):
        arr1.append(fun3(arr[i][j]))
        arr1.append(fun2(arr[i][j]))
        arr1.append(arr[i][j]-1)
    arr1=list(set(arr1))
    arr.append(arr1)
    n=min(arr1)
    i+=1
print(i)