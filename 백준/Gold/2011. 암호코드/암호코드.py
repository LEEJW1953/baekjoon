import sys
input=sys.stdin.readline

def f1(n):
    if n=="0":
        return 0
    else:
        return 1

def f2(n):
    if n[0]=='0':
        return 4
    elif n=="10" or n=="20":
        return 1
    elif 0<int(n)<=26:
        return 2
    elif int(n)%10==0:
        return 0
    else:
        return 3

n=input().strip()
dp=[0]
if n[0]==0: # 맨 앞에 0이 있으면 잘못됨
    dp.append(0)
elif len(n)==1:
    dp.append(f1(n))
elif len(n)==2:
    if f2(n)==3:
        dp.append(1)
    elif f2(n)==4:
        dp.append(0)
    else:
        dp.append(f2(n))
else:
    dp.append(f1(n[0:1]))
    if f2(n[0:2])==3:
        dp.append(1)
    elif f2(n[0:2])==4:
        dp.append(0)
    else:
        dp.append(f2(n[0:2]))
    for i in range(len(n)-2):
        s=n[0:i+3]
        s1=n[i+2:i+3]
        s2=n[i+1:i+3]
        if f1(s1)==1:
            if f2(s2)==1:
                dp.append(dp[i+1]%1000000)
            elif f2(s2)==2:
                dp.append((dp[i+1]+dp[i+2])%1000000)
            elif f2(s2)==3:
                dp.append(dp[i+2]%1000000)
            elif f2(s2)==4:
                dp.append(dp[i+2]%1000000)
        else:
            if f2(s2)==1:
                dp.append(dp[i+1]%1000000)
            else:
                dp.append(0)
                break
print(dp[-1])