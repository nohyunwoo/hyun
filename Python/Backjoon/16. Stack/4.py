import sys

while True:
    n = []
    stk = []
    count = 0
    n = sys.stdin.readline().rstrip()
    if n == ".":
        exit()
    else :
        for i in range(len(n)):
            if n[i] == "(" or n[i] == "[":
                stk.append(n[i])
            elif n[i] == ")" or n[i] == "]":
                if len(stk) == 0:
                    count += 1
                    break
                if n[i] == ")" and stk[-1] == "(":
                    stk.pop()
                elif n[i] == "]" and stk[-1] == "[":
                    stk.pop()
                else:
                    count += 1
                    break
    if len(stk) != 0 or count == 1:
        print("no")
    else:
        print("yes")