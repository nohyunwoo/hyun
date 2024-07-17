result = 0
n = int(input())
i = 1
while(True):
    result += i
    if result < n:
       i += 1
       continue
    if result >= n:
        print(i)
        break

