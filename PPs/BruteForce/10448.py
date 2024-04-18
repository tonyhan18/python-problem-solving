# 10448
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

d = [(n * (n+1)//2) for n in range(1,46)]
ans = [0] * 1001

for i in d:
    for j in d:
        for k in d:
            tmp = i + j + k
            if(tmp <= 1000):
                ans[tmp] = 1


k = int(input())
for _ in range(k):
    t = int(input())
    print(ans[t])

