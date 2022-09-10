eq=input().split('-')
num=0
for i in range(len(eq)):
    n=eq[i].split('+')
    m=0
    for j in n:
        m+=int(j)

    if i==0:
        num+=m
    else:
        num-=m
print(num)