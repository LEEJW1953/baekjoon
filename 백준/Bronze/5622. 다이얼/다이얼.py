a=list(input())
alp=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0
for i in a:
    for j in alp:
        for k in j:
            if i==k:
                time+=3+alp.index(j)
print(time)