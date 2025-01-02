n = int(input())

for _ in range(n):
    arr = []
    count= 0
    back = 0
    arr = list(input())
    
    for i in range(len(arr)):
        if (arr[i] == '('):
            count += 1
        else:
            count -= 1
        if (count < 0):
            back += 1
            break
    if (back == 1):
        print("NO")
        continue
    if (count == 0):
        print("YES")
    else:
        print("NO")
   
