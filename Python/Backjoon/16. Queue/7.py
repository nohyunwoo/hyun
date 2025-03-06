from collections import deque

qu = deque()

n = int(input())
count = 0

for i in range(1,n+1):
    qu.append(i)

while len(qu) != 1:
    if count == 0:
        qu.popleft()
        count += 1
    else:
        t_qu = qu.popleft()
        qu.append(t_qu)
        count -= 1

print(qu[0])