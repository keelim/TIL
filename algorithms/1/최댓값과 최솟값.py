
def solution(s):
    s=""
    a = map(int, s.split(' '))
    min_value, max_value = min(a), max(a)
    b =[min_value, max_value]
    print(b)
    return ' '.join(b)