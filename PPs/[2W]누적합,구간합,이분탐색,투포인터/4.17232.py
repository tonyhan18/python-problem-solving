# 17232 - 시뮬레이션 누적합
import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N,M,T = map(int,input().split())
K,A,B = map(int,input().split())

data =[]
for _ in range(N):
    data.append(list(input().strip()))

def getRangeSum(r,c,K):
    sum = 0
    for i in range(max(r-K,0), min(r+K+1, N)):
        for j in  range(max(c-K,0), min(c+K+1, M)):
            if(data[i][j] == '*'): 
                sum+=1
    return sum
        

for _ in range(T):
    for i in range(N):
        for j in range(M):
            nearAlive = getRangeSum(i,j,K)
            #print(nearAlive, end=' ')
            if(data[i][j] == '*'):
                nearAlive -=1
                if(nearAlive < A or B < nearAlive):
                    data[i][j] = '.';
            elif(A < nearAlive and nearAlive <= B):
                data[i][j] = '*'

for i in range(N):
    print(data[i])