import sys
input=sys.stdin.readline

def div(arr):
    global answer
    l=len(arr)
    s=0
    for i in range(l):
        for j in arr[i]:
            s+=int(j)
    if s==0:
        answer.append('0')
    elif s==l**2:
        answer.append('1')
    else:
        answer.append('(')
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
        answer.append(')')
    return
    

n=int(input())
arr=[]
for i in range(n):
    arr.append(input().rstrip())
answer=[]
# answer.append('(')
div(arr)
# answer.append(')')
print(''.join(answer))