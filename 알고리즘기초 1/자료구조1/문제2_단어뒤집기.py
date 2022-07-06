'''
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다
'''

# 왜 입력받는게 어떤거는 input() 하고 
# 어떤거는 sys.stdin.readline() 쓰는거지?
# 둘중 어떤걸 쓰느냐에 따라 정답/오답이 나뉘네...뭐지

# 위 이유 : 반복문으로 입력을 받을떄는 sys.stdin.readline()을 써야 시간단축됨!

import sys
n = int(input())
for i in range(n):
    str_name = sys.stdin.readline()
    str_lst = str_name.split()
    all_str = ''
    for j in str_lst:
        new_stack = []
        for idx in range(len(j)):
            new_stack.append(j[-(idx+1)])
        str_val = ''.join(new_stack)
        all_str = (all_str+str_val+' ')

    print(all_str)