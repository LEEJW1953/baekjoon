n=int(input())
count=0
num=666
while count!=n:
    for i in range(len(str(num))-2):
        if str(num)[i]=='6' and str(num)[i+1]=='6' and str(num)[i+2]=='6':
            count+=1
            break
    num+=1
print(num-1)