'''
괄호 짝맞추는 문제 (VPS 확인)
'''
import sys

# NUM = int(input())
NUM = 6
STA = [
'(())())',
'(((()())()',
'(()())((()))',
'((()()(()))(((())))()',
'()()()()(()()())()',
'(()((())()('
]
for i,sta in zip(range(NUM),STA):
    stack = []
    # str_val = sys.stdin.readline()
    str_val = sta
    for j in str_val:
        if j=="(":
            stack.append(j)
            continue
        if j==")" and stack and stack[-1]=="(":
            stack.pop()
        elif j==")" and stack and stack[-1]==")":
            print("NO")
            break
    if len(stack)==0:
        print("YES")

            