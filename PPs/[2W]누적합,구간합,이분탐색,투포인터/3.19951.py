#19951
import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

# 브루트포스 100억
# 주어진 입력에 대해서 값을 바꾼다.
# 아래와 같이하면 O(N + M)이 된다.
N,M = map(int ,input().split())
data = [0] + list(map(int,input().split()))
delta = [0] * (N+2)

for _ in range(M):
    a,b,k = map(int,input().split())
    
    delta[a] += k
    delta[b+1] += k * -1

# 방법 1
accDelta = [0] * (N+2)
for i in range(1, N+1):
    accDelta[i] = accDelta[i-1] + delta[i];
    print(data[i] + accDelta[i], end=' ')
# 방법 2
# accDelta = 0
# for i in range(1, N+1):
#     if(delta[i] != 0): accDelta += delta[i]
#     data[i] += accDelta
#     print(data[i],end=' ')
    
