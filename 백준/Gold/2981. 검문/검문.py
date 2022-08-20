import sys
n=int(sys.stdin.readline())

def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

def LCM(x,y):
    return (x*y)/GCD(x,y)

num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))
num=sorted(num)

sub=[]
for i in range(n-1):
    sub.append(num[i+1]-num[i])

if n==2:
    result=sub[0]
else:
    for i in range(len(sub)-1):
        if i==0:
            result=GCD(sub[i],sub[i+1])
        else:
            result=GCD(result,sub[i+1])

a=1
res=[]
while a*a<=result:
    if result%a==0:
        res.append(a)
    a+=1

if (result**0.5)%1!=0:
    for i in range((len(res)-1),-1,-1):
        res.append(result//res[i])
elif(result**0.5)%1==0:
    for i in range((len(res)-2),-1,-1):
        res.append(result//res[i])

for i in range(len(res)-1):
    print(res[i+1],end=' ')