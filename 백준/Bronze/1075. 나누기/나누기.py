n=input()
f=int(input())
num=int(n[0:-2])*100
for i in range(100):
    if (num+i)%f==0:
        if i<10:
            print(f'0{i}')
            break
        else:
            print(i)
            break