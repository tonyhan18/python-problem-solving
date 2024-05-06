#2295 세 수의 합
# x + y == k - z
import sys
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

N = int(input())
arr1 = list(int(input()) for _ in range(N))
arr1.sort()
arr2 = []
for i in range(N):
    for j in range(i, N):
        arr2.append(arr1[i] + arr1[j])

arr2.sort()
ans = 0
for i in range(N):
    for j in range(i, N):
        a = arr1[j] - arr1[i]
        l = 0
        r = len(arr2) -1
        while (l <= r):
            mid = (r + l) // 2
            b = arr2[mid]
            if (a < b):
                r = mid - 1
            elif (a > b):
                l = mid + 1
            else:
                ans = max(ans, arr1[j])
                break

print(ans)
    