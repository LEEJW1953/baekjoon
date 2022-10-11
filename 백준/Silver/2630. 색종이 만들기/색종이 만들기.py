import sys
input=sys.stdin.readline

def div(arr):
    global blue, white
    l=len(arr)
    ll=len(arr)**2
    s=0
    for i in range(l):
        s+=sum(arr[i])
    if s==ll:
        blue+=1
        return
    elif s==0:
        white+=1
        return
    else:
        arr1=[]
        arr2=[]
        arr3=[]
        arr4=[]
        for i in range(l//2):
            arr1.append(arr[i][0:l//2])
            arr2.append(arr[i][l//2:l])
            arr3.append(arr[i+l//2][0:l//2])
            arr4.append(arr[i+l//2][l//2:l])
        div(arr1)
        div(arr2)
        div(arr3)
        div(arr4)

n=int(input())
arr=[]
white=0
blue=0
for i in range(n):
    arr.append(list(map(int, input().split())))
div(arr)
print(white)
print(blue)