import sys
input=sys.stdin.readline

s=input().strip()
arr=[]
minn, maxx = '', ''
n=len(s)
tmp1, tmp2 = 0, 0
for i in range(n):
    if i==(n-1):
        if s[i]=='K':
            maxx+=str(int(5*10**(tmp1)))
            if tmp2:
                minn+=str(int(10**(tmp2-1)))
                minn+='5'
            else:
                minn+='5'
        else:
            maxx+='1'*(tmp1+1)
            minn+=str(int(10**(tmp2)))
    else:
        if s[i]=='K':
            maxx+=str(int(5*10**(tmp1)))
            tmp1=0
            if tmp2:
                minn+=str(int(10**(tmp2-1)))
                minn+='5'
            else:
                minn+='5'
            tmp2=0
        else:
            tmp1+=1
            tmp2+=1
print(maxx)
print(minn)