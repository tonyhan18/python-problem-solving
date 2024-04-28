# 11659 구간 합 구하기 4
import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N,M = map(int, input().strip().split())
data = list(map(int,input().split()))
data = [0] + data
acc = [0 for _ in range(N+1)]

for i in range(1, N+1):
    acc[i] = acc[i-1] + data[i]
    
for i in range(M):
    a,b = map(int, input().split())
    print(acc[b] - acc[a-1])
