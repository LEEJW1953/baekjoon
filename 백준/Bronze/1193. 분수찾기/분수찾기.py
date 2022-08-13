x=int(input())
i=0
j=1
while x>i:
    i+=j
    j+=1
if j%2==0:
    print("%s/%s"%(1+i-x,j-i+x-1))
else:
    print("%s/%s"%(j-i+x-1,1+i-x))