# 3085.py
import sys
#sys.stdin=open("input.txt","r")
input = sys.stdin.readline

t=int(input())
a=list(list(input().split('\n')[0]) for _ in range(t))


def check(a):
    n = len(a)
    c =1
    ans = 1
    for i in range(n):
        # 행검사
        c=1
        for j in range(1,n):
            if(a[i][j]==a[i][j-1]): c+=1
            else: c=1
            if(ans<c): ans=c

        c=1
        for j in range(1,n):
            if(a[j][i]==a[j-1][i]): c+=1
            else: c=1
            if(ans<c): ans=c
    return ans

ans=0
for i in range(0,t):
    for j in range(0,t):
        if(j+1<t):
            a[i][j],a[i][j+1]=a[i][j+1],a[i][j]
            ans=max(check(a),ans)
            a[i][j],a[i][j+1]=a[i][j+1],a[i][j]
        if(i+1<t):
            a[i][j],a[i+1][j]=a[i+1][j],a[i][j]
            ans=max(check(a),ans)
            a[i][j],a[i+1][j]=a[i+1][j],a[i][j]

print(ans)