import sys
input = sys.stdin.readline

n = int(input())
ans = 0
res = []
for _ in range(n):
    l = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (l + 1)
    total, start, end, count = -1e11, 0, 0, 0
    for i in range(l):
        dp[i + 1] = dp[i] + arr[i]
    for i in range(l + 1):
        for j in range(i + 1, l + 1):
            tmp = dp[j] - dp[i]
            if tmp > total:
                total = tmp
                start = i + 1
                end = j
                count = end - start
            elif tmp == total:
                count1 = j - i - 1
                if count1 < count:
                    total = tmp
                    start = i + 1
                    end = j
                    count = end - start
    ans += total
    res.append([start, end])
print(ans)
for i in range(n):
    print(*res[i])