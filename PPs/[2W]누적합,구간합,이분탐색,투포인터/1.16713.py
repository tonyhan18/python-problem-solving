import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N, Q = map(int, input().split())
data = [0] + list(map(int, input().split()))
acc = [0 for _ in range(N+1)]

for i in range(1, N+1):
    acc[i] = acc[i-1] ^ data[i]

sum = 0
for _ in range(Q):
    s,e = map(int,input().split())
    sum = sum ^ (acc[e] ^ acc[s-1])
    
print(sum)


