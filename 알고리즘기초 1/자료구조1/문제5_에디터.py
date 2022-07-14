from collections import deque


# in_str = deque([i for i in input()])
in_str = list(input())
in_str = in_str + ["cur"]
in_str = deque(in_str)
num = int(input())

for _ in range(num):
    command = input()
    if command.startswith("L"):
        if in_str[0]=="cur":
            pass
        else:
            in_str.rotate(-1)
            in_str.appendleft(in_str.pop())
        continue
    if command.startswith("D"):
        if in_str[-1]=="cur":
            pass
        else:
            in_str.rotate(1)
            in_str.append(in_str.popleft())
        continue
    if command.startswith("B"):
        idx = in_str.index("cur")
        in_str = in_str[:(idx-1)] + in_str[idx:]
        continue
    if command.startswith("P"):
        insert_str = command.split(" ")[-1]
        idx = in_str.index("cur")
        in_str = in_str[:idx]+[insert_str]+in_str[idx:]
        continue
answer = ''.join(in_str)
print(answer)