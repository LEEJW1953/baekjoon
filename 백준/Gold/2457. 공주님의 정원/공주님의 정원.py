import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr.append([100*a+b, 100*c+d])
arr.sort(key=lambda x:(-x[1], -x[0]))
count=0
end=0
j=0
if arr[0][1]>1130:
    while end<=1130:
        j+=1
        if count==0:
            for i in range(len(arr)):
                if arr[i][0]<=301:
                    count+=1
                    start=arr[i][0]
                    end=arr[i][1]
                    break
        else:
            for i in range(len(arr)):
                if arr[i][0]<=end:
                    count+=1
                    start=arr[i][0]
                    end=arr[i][1]
                    break
        if j>=1000000:
            count=0
            break
    print(count)
else:
    print(0)