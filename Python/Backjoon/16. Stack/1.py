import sys
n = int(input())

arr = []

for _ in range(n):
    # 분기 처리
    arr_list= list(map(int, sys.stdin.readline().split()))
    
    if(len(arr_list) == 1):
        x = arr_list[0]
        y = None
    else:
        x, y = arr_list
        
    if (x==1):
        arr.append(y)
    elif (x==2):
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif (x==3):
        print(len(arr))
    elif (x==4):
        if not arr:
            print(1)
        else:
            print(0)
    elif(x==5):
        if not arr:
            print(-1)
        else:
            print(arr[-1])
