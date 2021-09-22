# �˰��� �н� ���� ����
<br>
21�� �Ϲݱ� : Greedy, Simulation, DFS/BFS<br>
22�� ��ݱ� : Sort, Binary Search, DP, Dijkstra, Graph<br>
<br>
<br>

#  === �˰��� ������ ���� ���̽� ���� ===
<br>
<br>

# 1. ����Ʈ(list)
�����͸� �������� ���Ի��� �� �� ������ �׸�ŭ �޸𸮸� ���� ����<br>
<br>
����Ʈ ����<br>
```python
1����
d=[0]*100001 : 100001 ũ���� ����Ʈ ����

3����
d = [[[[False]*436 for k in range(31)] for j in range(31)] for i in range(31)]


# �̶� ���� ���ʿ� �� �� �迭������ ���� ������ �κ�(��,��,����,���� ������ �������� ��)
# 436�� ���� 31�� ���� 31�� �� ���� ������ 31�� ��

```
<br>
<br>
https://shoark7.github.io/category/programming<br>
<br>
offset index<br>
d[�̻�:�̸�:�̵���]<br>
���� �Է��� ���� �ʰų� �ξ� ū ���ڸ� �Է��ϸ� �׳� ��ü�� ��ȯ<br>
<br>
����Ʈ ����<br>
```python
a=[]
b=[]
a+b

c=[0]*2
```
<br>
���� �Լ���<br>
- append(������) : �ڿ� �� �߰�<br>
- extend(����Ʈ) : ���ϱ� ����� ����(�� ����Ʈ�� ����Ʈ�� ���� �� ����)<br>
- insert(��ġ,������) : Ư����ġ�� ������ ����<br>
- remove(������) : Ư�� ���� ���� <br>
- del ����Ʈ[��ȣ] : Ư�� ��ġ�� ���� ����<br>
- sum(����Ʈ) : ����Ʈ�� �ִ� �� ��� ��ġ��<br>
- max(����Ʈ) : �ִ� ã�� ��ȯ<br>
- min(����Ʈ) : �ּڰ� ã�� ��ȯ<br>
<br>

## ����Ʈ ���� ��ȯ
[https://wikidocs.net/14](https://wikidocs.net/14)<br>
[![](https://images.velog.io/images/tonyhan18/post/c4fdf96d-bfcd-4167-ba43-4fe8e1467cfb/image.png)](https://wikidocs.net/14)<br>
<br>

## 2���� ����Ʈ ���� ��ȯ �� 2���� ����Ʈ Ž��
<br>
[https://dojang.io/mod/page/view.php?id=2292](https://dojang.io/mod/page/view.php?id=2292)<br>
<br>
[![](https://images.velog.io/images/tonyhan18/post/4dfb1869-637f-4258-bad6-bba84fd6f123/image.png)](https://dojang.io/mod/page/view.php?id=2292)<br>
<br>
<br>

## ����Ʈ, Ʃ�� ��� ���� ����
<br>
![](https://images.velog.io/images/tonyhan18/post/31ba18e5-3cd5-46ec-95cb-881812a5230f/image.png)<br>
[https://dojang.io/mod/page/view.php?id=2300](https://dojang.io/mod/page/view.php?id=2300)<br>
<br>

## 3���� �̻��� �迭 �����ϱ�
[![](https://images.velog.io/images/tonyhan18/post/a8d329a8-be25-43f9-9957-9f72e3519fc2/image.png)](https://dojang.io/mod/page/view.php?id=2297)<br>
<br>
[https://dojang.io/mod/page/view.php?id=2297](https://dojang.io/mod/page/view.php?id=2297)<br>
<br>
```python
d = [[[[False]*436 for k in range(31)]
for j in range(31)] for i in range(31)]
```
�������ڸ� for i in range �ݺ�<br>
�̶� ���� ���ʿ� �� �� �迭������ ���� ������ �κ�(��,��,����,���� ��)<br>
<br>

## ���̽� ����
![](https://images.velog.io/images/tonyhan18/post/094a3ef2-f0a2-41e2-8404-39e9ae76f0a0/image.png)<br>
�� ���� ����<br>
<br>
���� ����ϱ� : ���� ���ظ��� ���� ���� �׷��� ���ٶ�� �ۼ��ϰ� : �Ѵ��� ù��° ���� ������ ���ĵ� �� �� ��° ���� ������ �����Ѵ�.<br>
```python
a=[[1,2],[3,4],[5,6]]
a.sort(key=lambda(x) : (x[1],-x[0]))
sorted(a,key=lambda a : (a[1],-a[0]))
```
<br>

## ���̽� ����Ʈ �� ��ġ��
http://blog.naver.com/PostView.nhn?blogId=ohgnus56&logNo=221517688923&parentCategoryNo=14&categoryNo=&viewDate=&isShowPopularPosts=true&from=search<br>
<br>
![](https://images.velog.io/images/tonyhan18/post/6b894e1e-be1e-4aed-a31a-dde57dae5d24/image.png)<br>
<br>

## ���̽� ����Ʈ�� ���� �����̱�
```python
ans=[]
ans.append("Hello")
```
<br>

## ����Ʈ �� �ʱ�ȭ
```python
list =[]
list.clear()
```
<br>

## ����Ʈ ���� �����ϱ�
```python
a=[0,0,0]
t=a[:]
�� ������� �ϰų�

t=a.copy()
�� ������� �ϰų�
```
<br>

## �ߺ�����(set)
```python
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
my_set = set(my_list) #����set���� ��ȯ
my_list = list(my_set) #list�� ��ȯ
print(new_list)
��µ� ���� ['D', 'B', 'A', 'E', 'C']
```
<br>

# 2. ���
print(a,b,c)<br>
print(a+b+c)<br>
<br>
�齽����, �̽������� ����<br>
![](https://images.velog.io/images/tonyhan18/post/6ff1e5e5-756b-4a5c-8331-d65052db74ce/image.png)<br>
<br>
\t �� Ű������ tab ��ư�� ������ ��ó�� �߰��� ���� �ֱ�<br>
<br>

## format ����ϱ�

```python
# ���� �����ϱ�
s1 = 'name : {0}'.format('BlockDMask')
print(s1)
 
 
# ������ ���� �ϱ�
age = 55
s2 = 'age : {0}'.format(age)
print(s2)
 
# �̸����� �����ϱ�
s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='��')
print(s3)
```
��ó: https://blockdmask.tistory.com/424 [������ ������]<br>
<br>
## % ����ϱ�
![](https://images.velog.io/images/tonyhan18/post/48bb11d0-d158-434f-87ba-7325b3bfdfad/image.png)
```python
# ���� ���
print('���� �̸��� %s�Դϴ�'%('�ѻ��'))
print('���� �̸��� "%s"�Դϴ�. ���̴� %d���̰� ������ %s�Դϴ�.'%('�ѻ��',33,'����'))
print('���̴� %d���̰� ������ %s�Դϴ�. ���� �̸��� "%s"�Դϴ�. '%(33,'����','�ѻ��'))
print('���̴� %03d���̰� ������ %6.2f�Դϴ�. ���� �̸��� "%s"�Դϴ�. '%(33,56.789,'�ѻ��'))
print('-' * 40)
```

# 3. �Է�

## �� ���̻��� ���ڸ� int�� �ޱ�
```python
n,m = map(int,input().split())
```
[������](https://dojang.io/mod/page/view.php?id=2286)
map�� ����Ʈ�� ��Ҹ� ������ �Լ��� ó�����ִ� �Լ�
map(func, list) ���·� ������ 

```python
for i in range(len(a)):
     a[i] = int(a[i])
```
�̷��� ó���ؾ��� �Լ���

```python
map(int,a)
```
�� ���� ¥���� ������ �� �ִ�.

## ���� �� �Է¹޾� ����Ʈ�� �����
```python
a = [0] * 10
for i in range(10):
	a[i] = int(input())
```
�� ���Ÿ��� �ؾ��ϴ� �ݺ�����

```python
a=list(map(int,input()) for _ in range(10))
```

������ �ذ� ����

������ ���� ����� �������� ������ ���� �߻��� a�� map Ÿ���� �ȴٴ��� �ϴ� �׷��� �Ʒ��� ����� ���� �� ������ �� ����

```python
a=[int(input()) for _ in range(9)]
```

�߰������� �� �� �̻��̶��

```python
a=list(list(map(int,input().split())) for _ in range(2))
```

---

�����ϸ� ������ �Է���
a=list(map(int,input()) for _ in range(10))

������ �Է���
a=[int(input()) for _ in range(9)]


## ���� �Է�
```python
import sys
a = int(sys.stdin.readline())
```
�ϸ� ĳ����

�� ���̻��� ���� ��������
```python
import sys
a,b = map(int,sys.stdin.readline().split())
```
���ָ� �� `'\n'` ���� �������� ������ �о��

���� ���� ��ũ
https://www.acmicpc.net/problem/15552

## \n ���๮�� �����ϰ� �Է¹ޱ�
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

```python
t=int(input())
a=list(list(input().split('\n')[0]) for _ in range(t))
```
## ������ ���� ���ڰ� �پ��ִ� 2���� �迭 �ޱ�
![](https://images.velog.io/images/tonyhan18/post/720cdd7a-ef78-4c59-991f-e581666eed39/image.png)
```python
a=[list(map(int,list(input().rstrip()))) for _ in range(m)]
b=[list(map(int,list(input().rstrip()))) for _ in range(m)]
```
���� �� �ϴ� ����Ʈ�� �ٲ۴��� map���� ��� int�� �ٲٰ� �װ� �ٽ� ����Ʈ�� ���´�.

![](https://images.velog.io/images/tonyhan18/post/0fc7b7c3-1d70-45ec-8fc7-c7e349b3c3d4/image.png)
�̰� ���ڿ��� ���������� ���ڸ� ������ ����� �ȴ�.
```python
t=int(input())
a=[list(map(str,list(input().rstrip()))) for _ in range(t)]
```

# 4. ������
����, ����, �Լ�, ��ü, ����Ʈ
���ڴ� �ݵ�� ����ǥ
���̽㿡�� ������ ������ �������� ����
���̽��� ���� ũ�⿡ ������ ���� ������ float Ÿ���� �Ҽ����� ���� �ݺ��Ǹ� ǥ���� �� �ִ� ���� �Ѱ谡 ����

��Ģ����
+ �� ���ϱ�
- �� ����
* �� ���ϱ�
** �� �ŵ�����
/ �� ������
% �� ������ ���ϱ�

����ǥ ���� ��밡�� """ '''�̰� ����ϸ� �߰��� �ֵ���ǥ�� �ܴٿ�ǥ�� ��밡��

## ���̽㿡�� ���� �����ڰ� ����
[![](https://images.velog.io/images/tonyhan18/post/677d879f-5087-494c-96bd-a6993e081444/image.png)](https://ondemand.tistory.com/255)

https://ondemand.tistory.com/255

���� ���̽���...

��ư ���Ÿ� for���� �ַν����

# 5. if ��,���ǹ�
if ����:
	�����ڵ�
elif ����:
	�����ڵ�
else:
	�����ڵ�
    
�񱳿����� <,<=,>,>=,==

# 6. �ݺ���,for��
for i in range(Ƚ�� �ݵ�� ���� �̻�, �̸�,��������):
	�ݺ��� �ڵ�

����Ʈ ��µ� ����
for j in [����1,����2]
	�ݺ��� �ڵ�

�׷��� �Ϲ������δ� �������ڰ� 1�̱� ������
for i in range(0,2): �� ��������� ���� ���ҽ�Ű�� ���� ����
for i in range(2,0,-1): �� �ۼ��Ѵ�. (����,�ʰ�)
Ȥ�� for i in reversed(range(10)) �� �ȴٰ� �Ѵ�.

## ���̽� �ݺ��� �ε��� �� ����
���̽��� 
for i in len(str):
 i =10
 
���� �ٲپ i�� for������ ��� ���� ������ �ʱ�ȭ �ȴ�. �̷��� ������ �ذ��ϱ� ���� ������ ���� �ڵ�� �ٲٴ� ���� ����.

```python
i=0
while i < len(s):
	print(s[i])
	if s[i] == 'a':
		i+=1
	i+=1
```
��ó: https://publivate.tistory.com/207

## �ε����� ���� �Բ� �޾ƿ���
```python
for i,v in enumerate(d)
```

# 7. ����
## ���̽㿡�� �������� ����ϱ�

[![](https://images.velog.io/images/tonyhan18/post/e7c5ef70-e75f-442b-ae65-6b4e69d014d7/image.png)](https://python.bakyeono.net/chapter-3-4.html)
[https://python.bakyeono.net/chapter-3-4.html](https://python.bakyeono.net/chapter-3-4.html)

����� �׳� ������ ���� �̰� �������� �������� �� �� ���� ������ ���������� �Լ� ������ ����Ϸ��� global ������ �ʼ� ��


# 8. �Լ�
```python
def �Լ� �̸�(�Ű�����1, �Ű����� 2=�⺻�� ...):
	return ��ȯ��
```

## Ư�� ���ڿ��� �������� ����Ʈ�� ����� ����ϱ�

[![](https://images.velog.io/images/tonyhan18/post/1e709814-3e2a-469d-bdb9-40be15d403cc/image.png)](https://ourcstory.tistory.com/46)

[https://ourcstory.tistory.com/46](https://ourcstory.tistory.com/46)

����� .join�� ����ϸ� ��


## ���� �ƽ�Ű �� ��ȯ
[![](https://images.velog.io/images/tonyhan18/post/cb1ae31b-a404-4213-9fae-412dde27e086/image.png)](https://wikidocs.net/32#ord)
https://wikidocs.net/32#ord

```python
ord('A') #65 ��ȯ
```

## ���� �� ���ϱ�
[![](https://images.velog.io/images/tonyhan18/post/05e35b38-834f-4d52-b891-6cca80ca8bdb/image.png)](https://codepractice.tistory.com/75)

https://codepractice.tistory.com/75

## min/max �Լ�, �ε���
```python
min(list)
max(list)
```

�ݴ�� max Ȥ�� min ���� �ε����� ã�� ���ؼ��� ������ �Լ��� ����ϸ� �ȴ�.
```python
list.index(max(list))
list.index(min(list))
```

Ư�� �� �Ǵ� ���� ����ϱ�
```python
print(min(d[1][0:2])
```
1�� 0,1�� ���

## math, sqrt
```python
import math
math.sqrt(10)
```

## ����
```python
from itertools import permutations
a=[1,2,3]
permutations(a)
permutations(a,2)
```

���������� ������ C++�� Ǯ��

## �켱���� ť(��)
```python
import heapq
maxheap=[]

# �ּ���
heapq.heappush(maxheap,2)
# �ִ���
heapq.heappush(maxheap,2)

heapq.heappop(maxheap)

��������Ʈ�� heap���� ����
heapq.heapify(maxheap)
```
������ ���̽� heapq�� �ּ������� ������ �ֱ� ������ �츮�� �˾Ƽ� ������ �־�� �Ѵ�. ���� ������ ����.


# 9. ���ڿ�
```python
a="abcde"
a[2]
b="fghij"
a+b
a*2
```

���ڿ� �Լ�
![](https://images.velog.io/images/tonyhan18/post/e90e3bc9-940e-492c-83ce-09e770301738/image.png)
- len(����Ʈ) : ���ڿ��� ���ڰ��� ��ȯ
- .count("Ư������") : Ư�������� ���� ��ȯ
- .upper()
- .lower()
- .split("Ư������") : Ư�����ڰ� ������� �װ� �������� ���ڿ��� ����

# 10. ����
```python
���� ��ü = open(�����̸�, ���� ���� ���)
```
�׳� "a.txt" �ϸ� ���� .py ������ �ִ� ��ġ
���
![](https://images.velog.io/images/tonyhan18/post/79c1c023-0f06-4cd5-91bc-35ff4556cbe5/image.png)

```python
f=open("a.txt","w")

���Ͽ� ����
f.write("2020-03-17 \n")

���� �ݱ�
f.close()

���� �б�
f.read() -> �׳� ��ü �� ����
f.readline() -> �� ���� ���� ����Ʈ�� ��� ����Ʈ ��ȯ
```

# 11. ���(���̺귯��)
����� �ϳ��ϳ� ������ � ������ ���� ���α׷��� ����� ���� ���α׷�
import �� ����ؼ� ��� ��������

```python
import random
num=random.randint(1,1000)
```
����� ���� ���丮�� �ְų� ���̽� ���̺귯���� ����Ǿ� �־�� ��
�� ������ ���̽��� ���� ���� ���� �����ϸ� �ȵ�

## ����Ž��Ʈ��(BST)
��Ÿ���Ե� ����Ž��Ʈ��, ����Ʈ���� �ܺ� ���̺귯���� ���� ��ġ�ؾ� �Ѵ�.

pip install bintrees

## ��ť(heapq)
�������� ���̽㿡�� ���� �����ؼ� ��� �����ϴ�.
```python
import heapq
```

# 12. ����ó��
```python
try:
except ���� Ÿ�� as e:
```
![](https://images.velog.io/images/tonyhan18/post/26bfd03d-699d-4b7c-abf3-777f03893c56/image.png)
![](https://images.velog.io/images/tonyhan18/post/3f703bd1-faf4-4226-a268-1b0946f2b7d5/image.png)
![](https://images.velog.io/images/tonyhan18/post/3727907c-9ce2-4fdd-be1d-3d916cc414cf/image.png)

# 13. Ŭ����
Ŭ������ ���� ����
��ü�� Ŭ������ ���� ������

```python
class Book(��� Ŭ����):
	# ������
	def __init__(self,title,author):
    	self.title=title
        self.author=author
    def outputAuthor(self):
    	print(self.author)

book1=Book(author="Victor",title="Res")
book1.outputAuthor()
```

# 14. �� ũ�Ѹ�
```python
from urllib.request import urlopen
import urllib.request
html=urlopen("�ּ�")
doc=html.read().decode("UTF-8")
```

# 15. ����

## ����Ʈ join ���� TypeError: sequence item 0 �㶧 �ذ���
�̰� �ߴ� ������ join�� �ݵ�� str ���� �Ű������� ����ϱ� ����. �׷��� ������ ����Ʈ�� ���ҵ��� ��� str�� �ٲپ� �ִ� ������ �ʿ��ϴ�.

```python
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline

t = int(input())
d = list(int(input()) for _ in range(t))

d.sort()

print("\n".join(map(str,d)))
```

��ó : https://hyesun03.github.io/2017/04/08/python_int_join/

# PS �ӵ�����
* ��� �� ������ �ڿ� ���°� �� ������.
2133 Ÿ��ä��⸦ �Ʒ��� �������� �͵鰣�� ����
```python
t = int(input())
d=[0]*(t+1)

d[0]=1

for i in range(2,t+1,2):
    d[i]=d[i-2]*3
    for j in range(i-4,-1,-2):
        d[i]+=d[j]*2

print(d[t])
```
```python
t = int(input())
d=[0]*(t+1)

d[0]=1

for i in range(2,t+1,2):
    d[i]=3*d[i-2]
    for j in range(i-4,-1,-2):
        d[i]+=2*d[j]

print(d[t])
```
![](https://images.velog.io/images/tonyhan18/post/7e7c8c75-ec11-4915-8711-9d905f103172/image.png)

���̰� �� ����. ���ʰ� ��������� �������� Ȯ���� �� �־���.

---
�����ڷ�

[��ũ](https://dojang.io/mod/page/view.php?id=1220)


[![](https://images.velog.io/images/tonyhan18/post/4dd675da-21ca-43d1-a65e-db0162168856/image.png)](https://dojang.io/mod/page/view.php?id=1220)