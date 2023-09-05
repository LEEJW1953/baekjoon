num={'**** ** ** ****':0,
     '  *  *  *  *  *':1,
     '***  *****  ***':2,
     '***  ****  ****':3,
     '* ** ****  *  *':4,
     '****  ***  ****':5,
     '****  **** ****':6,
     '***  *  *  *  *':7,
     '**** ***** ****':8,
     '**** ****  ****':9}

ans=[]
for j in range(5):
    s=input()
    n=(len(s)+1)//4
    if j==0:
        arr=['' for _ in range(n)]
    for i in range(n):
        t=s[4*i:4*i+3]
        arr[i]+=t
for i in range(len(arr)):
    if arr[i] not in num:
        print('BOOM!!')
        exit(0)
    ans.append(num[arr[i]])
if sum(ans)%3==0 and ans[-1]%2==0:
    print('BEER!!')
else:
    print('BOOM!!')