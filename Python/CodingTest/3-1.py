import time

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0
count = 0
while m >= 1:
    m += -1
    if(count ==  3):
        result += second
        count = 0
        print(2)
    else:
        result += first
        count += 1
        print(1)

print(result)