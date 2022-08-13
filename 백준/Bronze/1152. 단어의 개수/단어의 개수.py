a=input()
count=1
for i in a:
    if i==" ":
        count+=1
if a[0]==" ":
    count-=1
if a[len(a)-1]==" ":
    count-=1
print(count)