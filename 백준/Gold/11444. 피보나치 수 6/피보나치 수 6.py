import sys
input=sys.stdin.readline

def fib(n):
    if n==1:
        return arr
    else:
        tmp=fib(n//2)
        if n%2==0:
            arr1=[[0, 0],[0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        arr1[i][j]+=(tmp[i][k]*tmp[k][j])%1000000007
            return arr1
        else:
            arr1=[[0, 0],[0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        arr1[i][j]+=(tmp[i][k]*tmp[k][j])%1000000007
            arr2=[[0, 0],[0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        arr2[i][j]+=(arr1[i][k]*arr[k][j])%1000000007
            return arr2
arr=[[1, 1],[1, 0]]
print(fib(int(input()))[1][0]%1000000007)