# 2470 두 용액
import sys
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

l = 0
r = N -1
ans = abs(arr[l] + arr[r])
sel = [arr[l], arr[r]]

while( l < r):
    cur = arr[l] + arr[r]
    if(abs(cur) < ans):
        ans = abs(cur)
        sel = [arr[l], arr[r]]
        if(ans == 0):
            break
    elif(cur < 0):
        l +=1
    else:
        r -=1
        
print(sel[0], sel[1])