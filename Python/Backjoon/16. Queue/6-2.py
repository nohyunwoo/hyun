import sys
from collections import deque

queue = deque()
f_comm = []
n = int(sys.stdin.readline())

for i in range(n):
    f_in = sys.stdin.readline().strip()
    comm = f_in.split()
    f_comm = comm[0]
    
    if f_comm == 'push':
        queue.append(comm[1])
        print(queue)
    elif f_comm == 'pop':
        if len(queue) != 0:
            delt = queue.popleft()
            print(delt)
        else:
            print(-1)
    elif f_comm == 'size':
        print(len(queue))
    elif f_comm == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif f_comm == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif f_comm == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
            