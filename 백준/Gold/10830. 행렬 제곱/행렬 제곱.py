import sys
input=sys.stdin.readline

def mul(arr, x):
    if x==1:
        return aa
    else:
        tmp=mul(arr, x//2)
        if x%2==0:
            arr1=[[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        arr1[i][j]+=(tmp[i][k]*tmp[k][j])%1000
            return arr1
        else:
            arr1=[[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        arr1[i][j]+=(tmp[i][k]*tmp[k][j])%1000
            arr2=[[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        arr2[i][j]+=(arr1[i][k]*aa[k][j])%1000
            return arr2


n, b = map(int,input().split())
aa=[]
for i in range(n):
    aa.append(list(map(int, input().split())))
answer=mul(aa, b)
for i in range(n):
    for j in range(n):
        if j==n-1:
            print(answer[i][j]%1000)
        else:
            print(answer[i][j]%1000, end=' ')