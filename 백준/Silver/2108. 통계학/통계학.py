import sys
n=int(input())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
#산술평균
print(round(sum(num)/n))
#중앙값
print(num[(n-1)//2])
#최빈값
nmax=max(num)
nmin=min(num)
count=[0]*(nmax-nmin+1)
for i in range(n):
    count[num[i]-nmin]+=1
cmax=max(count)
cmin=min(count)
arr=[]
cnt=0
for i in range(len(count)):
    if count[i]==cmax:
        arr.append(i+nmin)
        cnt+=1
    if cnt==2:
        break
if len(arr)==1:
    print(arr[0])
elif len(arr)!=1:
    print(arr[1])
#범위
print(num[-1]-num[0])