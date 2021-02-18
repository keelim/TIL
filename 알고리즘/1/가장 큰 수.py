from itertools import permutations

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    list1 = list(permutations(numbers))
    list2 = [''.join(ele) for ele in list1 ]

    return sorted(list2, key=lambda x: int(x))[-1]
