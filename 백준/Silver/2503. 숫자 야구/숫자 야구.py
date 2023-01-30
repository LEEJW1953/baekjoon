import sys
input=sys.stdin.readline

def f(arr):
    count=0
    for i in range(1, 10):
        for j in range(1, 10):
            if j==i:
                continue
            for k in range(1, 10):
                if k==i or k==j:
                    continue
                num=str(i*100+j*10+k)
                tmp=True
                for l in range(len(arr)):
                    guess=arr[l]
                    strike=0
                    ball=0
                    for a in range(3):
                        if num[a]==guess[0][a]:
                            strike+=1
                        elif num[a] in guess[0]:
                            ball+=1
                    if strike!=guess[1] or ball!=guess[2]:
                        tmp=False
                        break
                if tmp:
                    count+=1                    
    print(count)


n=int(input())
arr=[]
for i in range(n):
    arr1=list(map(int, input().split()))
    arr1[0]=str(arr1[0])
    arr.append(arr1)
count=0
f(arr)