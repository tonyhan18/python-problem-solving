# 1920
import sys
import bisect
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
T = int(input())
find = list(map(int, input().split()))

# 이렇게 하면 기존 배열이 바뀜
#data.sort()

# 이렇게하면 기존 배열을 새로 만들어서 바뀜
data = sorted(data)

def binary_search(target):
    l = 0
    r = len(data) - 1
    while( l <= r):
        m = (l + r) // 2
        if(data[m] == target):
            return 1
        elif( target < data[m]):
            r = m - 1
        else:
            l = m + 1
    return 0

def bisect_search(target):
    i = bisect.bisect_left(data,target)
    #print(f"data {i}")
    if i < len(data) and data[i] == target:
        return 1
    else:
        return 0

for f in find:
    # 248ms
    #print(binary_search(f))
    # 264ms
    print(bisect_search(f))
    # 4920ms 정렬 안되어 있으면 시간초과
    #print(1 if f in data else 0)