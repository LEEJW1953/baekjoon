import sys
input=sys.stdin.readline

while True:
    arr=list(map(int, input().split()))
    n=arr.pop(0)
    if sum(arr)==0:
        break
    arr.sort()
    num1=''
    num2=''
    i=0
    while arr:
        x=arr.pop(0)
        if i%2==0:
            if x==0 and num1=='':
                arr.insert(0, x)
                for j in range(len(arr)):
                    if arr[j]:
                        num1+=str(arr.pop(j))
                        break
            else:
                num1+=str(x)
        else:
            if x==0 and num2=='':
                arr.insert(0, x)
                for j in range(len(arr)):
                    if arr[j]:
                        num2+=str(arr.pop(j))
                        break
            else:
                num2+=str(x)
        i+=1
    print(int(num1)+int(num2))