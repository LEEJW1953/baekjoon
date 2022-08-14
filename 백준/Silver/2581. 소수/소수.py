m=int(input())
n=int(input())
arr=[]
sum=0
for i in range(m, n+1):
    count=0
    for j in range(1, i+1):
        if i%(j)==0:
            count+=1
    if count==2:
        arr.append(i)
        sum+=i
if len(arr)==0:
    print(-1)
else:
    print(sum)
    print(arr[0])