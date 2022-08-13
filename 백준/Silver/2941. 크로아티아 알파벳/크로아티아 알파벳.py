a=input()
count=len(a)
for i in range(len(a)):
    if a[i]=="=" or a[i]=="-":
        if a[i-1]=="z" and a[i-2]=="d":
            count-=2
        else:
            count-=1
    if a[i]=="j" and (a[i-1]=="l"or a[i-1]=="n"):
        count-=1
print(count)