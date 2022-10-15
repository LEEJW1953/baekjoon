import sys
input=sys.stdin.readline

def div(arr):
    global count1, count2, count3
    l=len(arr)
    s=arr[0][0]
    a=l//3
    divide=False
    for i in range(l):
        for j in range(l):
            if arr[i][j]!=s:
                divide=True
                break
    if divide==False:
        if s==-1:
            count1+=1
        elif s==0:
            count2+=1
        elif s==1:
            count3+=1
    else:
        arr1=[]
        arr2=[]
        arr3=[]
        arr4=[]
        arr5=[]
        arr6=[]
        arr7=[]
        arr8=[]
        arr9=[]
        for i in range(a):
            arr1.append(arr[i][0:a])
            arr2.append(arr[i][a:2*a])
            arr3.append(arr[i][2*a:l])
            arr4.append(arr[i+a][0:a])
            arr5.append(arr[i+a][a:2*a])
            arr6.append(arr[i+a][2*a:l])
            arr7.append(arr[i+2*a][0:a])
            arr8.append(arr[i+2*a][a:2*a])
            arr9.append(arr[i+2*a][2*a:l])
        div(arr1)
        div(arr2)
        div(arr3)
        div(arr4)
        div(arr5)
        div(arr6)
        div(arr7)
        div(arr8)
        div(arr9)
    return
    

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
count1, count2, count3 = 0, 0, 0
div(arr)
print(count1)
print(count2)
print(count3)