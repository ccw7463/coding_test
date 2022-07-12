NUM = int(input())
num_string = [i+1 for i in range(NUM)]
stack = []
for i in range(NUM):
    num = int(input())
    
    if stack and stack[-1]==num:
        stack.pop()
        continue

    
    for j in num_string:
        stack.append(j+1)
    
    if stack and stack[-1]==num:
        stack.pop()
    