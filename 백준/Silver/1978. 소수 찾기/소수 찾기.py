n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    count1=0
    for j in range(arr[i]):
        if arr[i]%(j+1)==0:
            count1+=1
    if count1==2:
        count+=1
print(count)