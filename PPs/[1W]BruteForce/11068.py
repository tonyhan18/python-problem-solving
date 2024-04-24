## 11068
import sys
#sys.stdin = open('0.input.txt','r')
input = sys.stdin.readline

t = int(input().strip())
is_ok = True

for _ in range(t):
    d = int(input().strip())
    for div in range(2, 65):
        # To JinBub
        t_d = d
        translated = []
        is_ok = True
        while t_d:
            translated.append(t_d % div)
            t_d //= div
        
        # Check
        for i in range(len(translated) // 2):
            if(translated[i] != translated[-(i+1)]):
                is_ok = False
                break
        if(is_ok):
            print(1)
            break
    if(not is_ok):
        print(0)  
exit()