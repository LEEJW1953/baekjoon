a,b,v=map(int,input().split())
if v==a:
    print(1)
elif (v-a)<(a-b):
    print((v-a)//(a-b)+2)
else:
    if (v-a)%(a-b)==0:
        print((v-a)//(a-b)+1)
    else:
        print((v-a)//(a-b)+2)