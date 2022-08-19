n, m=map(int, input().split())
arr=[[0]*m for i in range(n)]
for i in range(n):
    chess=input()
    for j in range(m):
        arr[i][j]=chess[j]
arr1=[]
for i in range(n-7):
    for j in range(m-7):
        arr2=[row[j:j+8] for row in arr[i:i+8]]
        countW=0
        countB=0
        for k in range(8):
            for l in range(8):
                if (k+l)%2==0:
                    if arr2[k][l]!='B':
                        countB+=1
                    if arr2[k][l]!='W':
                        countW+=1
                if (k+l)%2==1:
                    if arr2[k][l]!='W':
                        countB+=1
                    if arr2[k][l]!='B':
                        countW+=1
        arr1.append(countW)
        arr1.append(countB)
if (min(arr1))>32:
    result=64-int((min(arr1)))
else:
    result=min(arr1)
print(result)