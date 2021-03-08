def solution(n):
    answer = 0
    s1 = bin(n).replace('ob', '')
    one = s1.count('1')

    i = 0
    while True:
        n1 = n+i
        if one == bin(n1).replace('0b', '').count('1'):
            return n1
            break

        i+=1