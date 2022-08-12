def han(n):
    if n<100:
        ans=1
    elif 100<=n<1000:
        if (int(str(n)[2])-int(str(n)[1]))==(int(str(n)[1])-int(str(n)[0])):
            ans=1
        else:
            ans=0
    elif 1000<=n<10000:
        if (int(str(n)[3])-int(str(n)[2]))==(int(str(n)[2])-int(str(n)[1]))==(int(str(n)[1])-int(str(n)[0])):
            ans=1
        else:
            ans=0
    return ans
n=int(input())
count=0
for i in range(1,n+1):
    if han(i)==1:
        count+=1
print(count)