n=int(input())
for i in range(n):
    ox=list(input())
    sum=0
    sum1=0
    for j in range(len(ox)):
        if ox[j]=='O':
            sum1+=1
            sum+=sum1
        else:
            sum1=0
    print(sum)