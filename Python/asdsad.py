p, q = map(int, input().split())

m=min(p,q)

sum=0

for i in range(1,m+1):
    num_square = (p-i+1) * (q-i+1)
    sum += num_square

print("전체 정사각형 개수:", sum)