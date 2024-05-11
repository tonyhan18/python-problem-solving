# 10816 숫자 카드 2
import sys
import bisect
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
data.sort()
T = int(input())
search = list(map(int,input().split()))

for find in search:
    lower = bisect.bisect_left(data, find)
    upper = bisect.bisect_right(data, find)
    print(upper - lower, end=' ')