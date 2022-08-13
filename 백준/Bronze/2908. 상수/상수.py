a,b=map(str,input().split())
aa=100*int(a[2])+10*int(a[1])+int(a[0])
bb=100*int(b[2])+10*int(b[1])+int(b[0])
if aa<=bb:
    print(bb)
else:
    print(aa)