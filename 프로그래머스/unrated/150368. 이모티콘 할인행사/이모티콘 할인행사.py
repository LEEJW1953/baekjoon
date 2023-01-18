def solution(users, emoticons):
    sale = []
    s = []
    def f():
        if len(s)==len(emoticons):
            sale.append(s[:])
            return
        for i in range(40, 0, -10):
            s.append(i)
            f()
            s.pop()
    f()

    n = len(users)
    m = len(emoticons)
    answer = []
    for i in range(len(sale)):
        plus=0
        result=0
        for j in range(n):
            result1=0
            for k in range(m):
                if sale[i][k]>=users[j][0]:
                    result1+=int(emoticons[k]*(100-sale[i][k])/100)
            if result1>=users[j][1]:
                plus+=1
            else:
                result+=result1
        answer.append([plus, result])
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]