import sys
from collections import deque

qu = deque()

f_in = sys.stdin.readline().strip()
n, k = f_in.split()
k = int(k)
arr = []

n = int(n)
for i in range(1,n+1):
    qu.append(i)

for i in range(k, n+k):
    qu.rotate(n-i)
    arr.append(qu.pop())
  
print(arr)  
# print(f"<{', '.join(map(str, arr))}>")