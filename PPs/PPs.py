import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def flip(a, x, y, n, m):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if(i >= n or j >= m):
                continue
            if(a[i][j] == '0'):
                a[i][j] = '1'
            else:
                a[i][j] = '0'

n,m = map(int,input().split())

a = list(list(input().strip()) for _ in range(n))
b = list(list(input().strip()) for _ in range(n))

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if(a[i][j] != b[i][j]):
            ans+=1
            flip(a,i,j,n,m)

for i in range(n):
    for j in range(m):
        if(a[i][j] != b[i][j]):
            print('-1')
            sys.exit(0)
print(ans)