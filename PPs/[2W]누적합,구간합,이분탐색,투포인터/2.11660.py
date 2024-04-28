import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N,M = map(int,input().split())
data = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)

acc = [ [0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + data[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(acc[x2][y2] - acc[x1-1][y2] - acc[x2][y1-1] + acc[x1-1][y1-1])
