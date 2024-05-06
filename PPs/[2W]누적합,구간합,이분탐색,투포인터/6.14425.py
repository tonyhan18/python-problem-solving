# 14425 문자열 집합
import sys
import bisect
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N,M = map(int, input().split())
data = []
for _ in range(N):
    tmp = input().strip()
    data.append(tmp)
    
data.sort()

ans = 0
for _ in range(M):
    target = input().rstrip()
    l = 0
    r = N-1
    while ( l <= r):
        m = (l + r) // 2
        if(data[m] == target):
            ans+=1
            break
        elif( data[m] > target):
            r = m - 1
        else:
            l = m + 1
    
print(ans)