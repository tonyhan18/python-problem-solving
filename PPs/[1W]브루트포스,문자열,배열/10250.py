# 10250
import sys
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    h,w,n = map(int, input().strip().split())
    YY = n % h #층수
    XX = n // h + 1 #라인
    if(YY == 0):
        YY = h
        XX -= 1
    
    print(YY * 100 + XX)