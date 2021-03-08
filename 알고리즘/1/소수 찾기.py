from itertools import combinations


def solution(numbers: str):
    list1 = list(combinations(numbers, len(numbers)))
    answer = set()
    for ele in list1:
        answer.add(''.join(ele))
    print(answer)

    return len(answer)
