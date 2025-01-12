n = int(input())

students = list(map(int, input().split()))

stack = []

cnt = 1

for student in students:
    stack.append(student)
    
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

if stack:
    print("Sad")
else:
    print("Nice")