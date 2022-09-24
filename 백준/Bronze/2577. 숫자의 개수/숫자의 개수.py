a=int(input())
b=int(input())
c=int(input())
num=str(a*b*c)
arr=[0]*10
for i in num:
    i=int(i)
    arr[i]+=1
for i in range(10):
    print(arr[i])