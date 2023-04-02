import sys
input=sys.stdin.readline

def f(b, c):
    global answer, total
    if c=='P':
        return
    for i in range(len(grade)):
        if c==grade[i]:
            answer+=rating[i]*float(b)
            total+=float(b)
            return


grade=['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
rating=[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
answer=0
total=0
for _ in range(20):
    a, b, c = input().split()
    f(b, c)
print(answer/total)