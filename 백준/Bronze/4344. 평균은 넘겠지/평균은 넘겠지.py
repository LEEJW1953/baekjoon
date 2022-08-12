c=int(input())
for i in range(c):
    count=0
    testcase=list(map(int, input().split()))
    for j in range(testcase[0]):
        if testcase[j+1] > (sum(testcase[1:len(testcase)])/testcase[0]):
            count+=1
    print("{:.3f}%" .format(count/testcase[0]*100))