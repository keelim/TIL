
from itertools import combinations

def solution(number, k):
    list1 = list(combinations(number, len(number)-k))
    list2 = [''.join(ele) for ele in list1]
    # print(list2)
    return sorted(list2, key=lambda x: int(x))[-1]

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))