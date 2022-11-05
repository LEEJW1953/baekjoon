e, s, m = map(int, input().split())
if e==15:
    e=0
if s==28:
    s=0
if m==19:
    m=0
answer=1
while True:
    if (answer%15)==e and (answer%28)==s and (answer%19)==m:
        print(answer)
        break
    answer+=1