n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    if x==0:
        arr.pop()
    else:
        arr.append(x)
print(sum(arr))