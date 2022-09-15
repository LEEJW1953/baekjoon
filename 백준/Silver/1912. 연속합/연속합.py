import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
if n==1:
    print(arr[0])
elif n==2:
    print(max(arr[0], arr[1], arr[0]+arr[1]))
else:
    for i in range(n):
        if i==0:
            num=arr[0]
            arr1=[num]
            # print(arr1)
            continue
        else:
            if num<0:
                if arr[i]>=0:
                    num=arr[i]
                    arr1.append(num)
                elif arr[i]>=num:
                    num=arr[i]
                    arr1.append(num)
                # print(arr1)
            else:
                num+=arr[i]
                arr1.append(num)
                # print(arr1)
    print(max(arr1))