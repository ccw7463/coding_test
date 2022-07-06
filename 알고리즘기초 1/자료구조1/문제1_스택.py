'''
정수를 저장하는 스택을 구현한 다음
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
'''
'''
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
     만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 
    만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
# num = int(sys.stdin.readline())
num = int(input())

lst = []
for i in range(num):
    run_type = sys.stdin.readline()
    # run_type = input()
    if run_type.startswith('push'):
        lst.append(run_type.split()[-1]) 
        # split(' ') 하니까 출력형식 오류뜨고...
        # split() 하니까 정답이네.. 왜지? 공백으로 나누는거 동일한거아닌가?
    if run_type.startswith('pop'):
        try:
            print(lst.pop())
        except:
            print("-1")
    if run_type.startswith('size'):
        print(len(lst))
    if run_type.startswith('empty'):
        if len(lst)==0:
            print(1)
        else:
            print(0)
    if run_type.startswith('top'):
        if len(lst)==0:
            print("-1")
        else:
            print(lst[-1])

