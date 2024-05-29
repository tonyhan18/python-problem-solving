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

def lower_bound(find):
    lowerAns = len(data)
    l,r = 0, len(data) - 1
    while( l <= r):
        m = (l + r) // 2
        if( data[m] < find): l = m + 1
        else:
            lowerAns = m
            r = m - 1
    return lowerAns

def upper_bound(find):
    upperAns = len(data)
    l,r = 0, len(data) - 1
    while(l <= r):
        m = (l + r) // 2
        if(data[m] <= find): l = m + 1
        else:
            upperAns = m
            r = m - 1
    return upperAns


for find in search:
    lower = lower_bound(find)
    upper = upper_bound(find)
    print(upper - lower, end=' ')