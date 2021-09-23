import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

ans = []

def search(a, b, i, j, n,m):
	max = m if n < m else n
	for s in range(1,max+1):
		if(i-s < 0 or i+s >= n or j-s < 0 or j+s >= m):
			break
		if(a[i-s][j] == a[i+s][j] == '*' and a[i][j-s] == a[i][j+s] == '*'):
			ans.append([i+1,j+1,s])
			b[i-s][j] = b[i+s][j] = b[i][j-s] = b[i][j+s] = b[i][j] = 0

n,m = map(int,input().split())
a = list(input().strip() for _ in range(n))
b = []*n
for i in range(n):
	c= []
	for j in range(m):
		if(a[i][j] == "."):
			c.append(0)
		elif(a[i][j] == "*"):
			c.append(1)
	b.append(c)

for i in range(n):
	for j in range(m):
		if(a[i][j] == '*'):
			search(a,b,i,j,n,m)

for i in range(n):
	for j in range(m):
		if(b[i][j] == 1):
			print("-1")
			sys.exit()
print(len(ans))
for x,y,s in ans:
	print(x,y,s)