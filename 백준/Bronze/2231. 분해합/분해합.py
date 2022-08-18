n=int(input())
arr=[]
for i in str(n):
    arr.append(int(i))
num=[]
for i in range(len(arr), 9*len(arr)+1):
    m=n-i
    arr1=[]
    if m<=0:
        continue
    for j in str(m):
        arr1.append(int(j))
    if (m+sum(arr1))==n:
        num.append(m)

if len(num)==0:
    print(0)
else:
    print(min(num))