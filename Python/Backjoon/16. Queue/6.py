import sys

n = int(sys.stdin.readline())

qu = []

for i in range(n):
    c_a = sys.stdin.readline().strip()
    e = c_a.split()
    a = e[0]
    if a == 'push':
        qu.append(e[1])
        if len(qu) == 1:
            f = qu.index(e[1])
        ba = qu.index(e[1])
    elif a == 'pop':
        if len(qu) > 0:
            qq = qu.pop(f)
            print(qq)
        else:
            print(-1)
    elif a == 'size':
        print(len(qu))
    elif a == "empty":
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    elif a == "front":
        if len(qu) > 0:
            print(qu[f])
        else:
            print(qu[f])
            print(-1)
    elif a == "back":
        if len(qu) > 0:
            print(qu[ba])
        else:
            print(-1)