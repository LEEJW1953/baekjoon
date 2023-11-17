import sys
input=sys.stdin.readline

t=0
while True:
    t+=1
    n=int(input())
    if n==0:
        break
    arr=list(map(int, str(n)))
    if arr[0]!=1 or arr[-1]!=2:
        print(f'{t}. NOT')
    else:
        tmp=arr[0]
        valid=True
        for i in range(1, len(arr)):
            if arr[i]==1:
                valid=False
                break
            elif arr[i]==2 or arr[i]==3:
                if arr[i-1]!=4 and arr[i-1]!=6:
                    valid=False
                    break
            elif arr[i]==4 or arr[i]==5:
                if arr[i-1]!=1 and arr[i-1]!=3:
                    valid=False
                    break
            elif arr[i]==6 or arr[i]==7:
                if arr[i-1]!=8:
                    valid=False
                    break
            elif arr[i]==8:
                if arr[i-1]!=5 and arr[i-1]!=7:
                    valid=False
                    break
        if valid:
            print(f'{t}. VALID')
        else:
            print(f'{t}. NOT')