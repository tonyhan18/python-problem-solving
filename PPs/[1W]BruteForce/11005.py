import sys
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 출력해야 하는 경우에만 이렇게 스트링으로 저장하고
# 그 외의 경우라면 그냥 숫자를 저장하는 것이 진법 변환의 포인트
arr ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n,b = map(int, input().split())
ans = ''
while n:
    ans += arr[n % b]
    n //= b
    
print(ans[::-1])
