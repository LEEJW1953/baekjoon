n=int(input())
x=[]
y=[]
for i in range(n):
    xx, yy=map(int, input().split())
    x.append(xx)
    y.append(yy)
arr=[]
for i in range(n):
    count=1
    for j in range(n):
        if x[i]<x[j] and y[i]<y[j]:
            count+=1
    arr.append(str(count))
result=" ".join(arr)
print(result)