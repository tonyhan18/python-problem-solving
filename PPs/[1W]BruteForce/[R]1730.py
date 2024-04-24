#1730
# 쌩 노가다 문제 -> 뭔가 더 쉬운 방법이 있는지 알아봐야함

import sys
sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N = int(input())
map = [['.' for i in range(N+1)] for j in range(N+1)] 
cmd = input().strip()

###

def check(x, y):
    if(x < 0 or y < 0 or  N <= x or N <= y): return False
    return True

x = y = 0
for c in cmd:
    if c == 'D' and check(x+1, y):
        if(map[x][y] == '-'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '|'
        x += 1
        if(map[x][y] == '-'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '|'
    elif c == 'R' and check(x,y+1):
        if(map[x][y] == '|'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '-'
        y += 1
        if(map[x][y] == '|'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '-'
    elif c == 'U' and check(x-1,y):
        if(map[x][y] == '-'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '|'
        x -= 1
        if(map[x][y] == '-'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '|'
    elif c == 'L' and check(x,y-1):
        if(map[x][y] == '|'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '-'
        y -= 1
        if(map[x][y] == '|'): map[x][y] = '+'
        elif(map[x][y] == '.'): map[x][y] = '-'
        
for i in range(N):
    for j in range(N):
        print(map[i][j],end='')
    print()