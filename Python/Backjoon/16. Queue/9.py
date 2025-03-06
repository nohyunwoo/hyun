import sys
from collections import deque

n = int(input())

qu = deque()

for _ in range(n):
    f_in = sys.stdin.readline().strip()
    conn = f_in.split()
    comm = conn[0]
    if comm == '1':
            qu.appendleft(conn[1])
           
    elif comm == '2':
            qu.append(conn[1])
            
    elif comm == '3':
        if len(qu) != 0:
            q_qu = qu.popleft()
            print(q_qu)
        else:
            print(-1)
    elif comm == '4':
        if len(qu) != 0:
            p_qu = qu.pop()
            print(p_qu)
        else:
            print(-1)
    elif comm == '5':
        print(len(qu))
    elif comm == '6':
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    elif comm == '7':
        if len(qu) != 0:
            print(qu[0])
        else:
            print(-1)
    elif comm == '8':
        if len(qu) != 0:
            print(qu[-1])
        else:
            print(-1)
            