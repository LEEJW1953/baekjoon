n=int(input())
arr=list(map(int, input().split()))
count1, count2, count3 = 0, 0, 0
count=0
tmp=-1
for i in range(n):
    if tmp==-1 and arr[i]==0:
        count+=1
        tmp=0
    elif tmp==0 and arr[i]==1:
        count+=1
        tmp=1
    elif tmp==1 and arr[i]==2:
        count+=1
        tmp=2
    elif tmp==2 and arr[i]==0:
        count+=1
        tmp=0
print(count)