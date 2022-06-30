
n = int(input())

cnt = 1
lst = [0,1]

def pivo(n):
    global cnt
    
    if n == 0:
        return lst[0]
    elif n == 1:
        return lst[1]
    else:
        result = lst[0]+lst[1]
        lst[0]=lst[1]
        lst[1]=result
        cnt += 1
        
        # print(lst)

        if cnt == n:
            return result
        else:
            return pivo(n)

    
print(pivo(n))
