'''
괄호 짝맞추는 문제 (VPS 확인)
'''
import sys

NUM = int(input())

for i in range(NUM):
    print_str = []
    stack = []
    str_val = str_val = sys.stdin.readline()
    # str_val = sta
    for j in str_val:
        if j=="(":
            stack.append(j)
            continue
        if j==")" and stack:
            stack.pop()
            continue
        if j==")" and not stack:
            print_str.append("NO")
            break
    
    if len(print_str)==0 and not stack:
        print("YES")
    else:
        print("NO")

            
### 다른사람답
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')