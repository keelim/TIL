from typing import Counter


def solution(s):
    answer = []
    zero = 0
    i = 0
    while True:
        i+=1
        zero+=s.count('0')
        s= bin(s.count('1')).replace('0b','')
        if(s=='1'):
            break
        
    return [i, zero]