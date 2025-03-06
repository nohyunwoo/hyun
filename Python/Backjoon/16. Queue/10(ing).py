import sys
from collections import deque

n = int(input())

qu = deque()
qrr = []
for i in range(1, n+1):
    qu.append(i)
qrr = int(sys.stdin.readline().strip())

print(qrr)
# for i in range(1, n+1):
#     if i == 1:
#         q = qu.popleft()
#         print(q)
#         qu.rotate(comm-1)
#         continue
    
#     if comm > 0:
#         p = qu.popleft()
#         print(p)
#         qu.rotate(comm+1)
#         if comm % 2 != 0:
#             qu.rotate(comm)
        
#     elif comm < 0:
#         k = qu.popleft()
#         qu.rotate(comm)
#         print(k)
           
        
        
        
        
