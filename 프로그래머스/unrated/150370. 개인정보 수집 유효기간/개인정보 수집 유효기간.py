def solution(today, terms, privacies):
    answer = []
    termd={}
    yy, mm, dd = map(int, today.split("."))
    day = yy*10000 + mm*100 + dd
    for i in range(len(terms)):
        aa, bb = terms[i].split()
        bb=int(bb)
        termd[aa] = bb
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        yy1, mm1, dd1 = map(int, date.split("."))
        num=termd[term]
        num1=num//12
        num2=num%12
        yy1+=num1
        mm1+=num2
        if mm1>12:
            yy1+=1
            mm1=mm1-12
        if dd1==1:
            dd1=28
            mm1-=1
            if mm1<=0:
                yy1-=1
                mm1=mm1+12
        elif dd1!=1:
            dd1-=1
        day1 = yy1*10000 + mm1*100 + dd1
        if day1<day:
            answer.append(i+1)
        print(day1, day)
    return answer